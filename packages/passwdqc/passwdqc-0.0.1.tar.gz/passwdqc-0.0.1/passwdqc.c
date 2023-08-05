#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <passwdqc.h>

typedef struct {
	PyObject_HEAD
	passwdqc_params_t params;
} ConfigObject;

static int
Config_init(ConfigObject *self, PyObject *args, PyObject *kwargs)
{
	char *reason = NULL;
	const char **argv = NULL;
	int i, fail = 0;
	PyObject *item;

	passwdqc_params_reset(&self->params);

	if (PyTuple_Size(args) > 0) {
		if ((fail = !(argv = PyMem_Calloc(PyTuple_Size(args), sizeof(char *))))) {
			PyErr_SetString(PyExc_MemoryError, "cannot allocate buffer");
			goto fin;
		}

		for (i=0; i<PyTuple_Size(args); i++) {
			item = PyTuple_GetItem(args, i);
			if ((fail = !PyUnicode_Check(item))) {
				PyErr_SetString(PyExc_TypeError, "all arguments must be strings");
				goto fin;
			}
			argv[i] = PyUnicode_AsUTF8(item);
		}

		if ((fail = passwdqc_params_parse(&self->params, &reason, PyTuple_Size(args), argv))) {
			PyErr_SetString(PyExc_KeyError, reason);
			goto fin;
		}
	}
fin:
	PyMem_Free(argv);
	free(reason);
	return fail ? -1 : 0;
}

static void
Config_del(ConfigObject *self)
{
	//fprintf(stderr, "QQ %p\n", &self->params);
	passwdqc_params_free(&self->params);
}

static PyObject *
Config_str(ConfigObject * obj)
{
	return PyUnicode_FromFormat(
	"PasswdQC(min=<%d %d %d %d %d> max=%d pass=%d match=%d sim=%d bits=%d)", 
			obj->params.qc.min[0], obj->params.qc.min[1], obj->params.qc.min[2],
			obj->params.qc.min[3], obj->params.qc.min[4], obj->params.qc.max,
			obj->params.qc.passphrase_words, obj->params.qc.match_length,
			obj->params.qc.similar_deny, obj->params.qc.random_bits);
}

static PyTypeObject ConfigType = {
	PyVarObject_HEAD_INIT(NULL, 0)
	.tp_name = "passwdqc.config",
	.tp_doc = "Passwdqc configuration block.\n\
		   \n\
		   config([\"field1=value1\", \"field2=value2\", …])\n\
		   \n\
		   If no arguments are provided, default configuration block is used.\n\
		   \n\
		   See passwdqc.conf(5) for \"field1=value1\" syntax.\n\
		   \n\
		   E. g. use \"config=/path/to/file\" to read configuration from the file.",
	.tp_basicsize = sizeof(ConfigObject),
	.tp_itemsize = 0,
	.tp_flags = Py_TPFLAGS_DEFAULT,
	.tp_new = PyType_GenericNew,
	.tp_free = (freefunc) Config_del,
	.tp_init = (initproc) Config_init,
	.tp_str = (reprfunc) Config_str,
};

static PyObject *
generate(PyObject *self, PyObject *args)
{
	char *result;
	PyObject *pyresult = Py_None;
	ConfigObject *cfg = NULL, *tmp = NULL;

	if (!PyArg_ParseTuple(args, "|O!", &ConfigType, &cfg))
		return NULL;

	if (cfg == NULL)
		tmp = cfg = (ConfigObject *)PyObject_CallNoArgs((PyObject *)&ConfigType);

	result = passwdqc_random(&cfg->params.qc);
	if (result)
		pyresult = PyUnicode_Decode(result, strlen(result), NULL, NULL);

	free(result);
	Py_XDECREF(tmp);
	Py_XINCREF(pyresult);
	return pyresult;
}

//extern const char *passwdqc_check(const passwdqc_params_qc_t *params,
//    const char *newpass, const char *oldpass, const struct passwd *pw);

static PyObject *check(PyObject *self, PyObject *args, PyObject *kwargs) {

	struct passwd pw = {
		.pw_name = NULL,
		.pw_passwd = NULL,
		.pw_gecos = NULL,
		.pw_dir = NULL,
		.pw_shell = NULL,
	};
	static char *kwlist[] = { "newpass", "config", "oldpass", "pwentry", NULL };
	ConfigObject *cfg = NULL;
	char *newpass, *oldpass = NULL;
	const char *result = NULL;
	PyObject *pyresult = Py_None;
	PyObject *tmp;

	if (!PyArg_ParseTupleAndKeywords(args, kwargs, "s|O!s(ssOOsss)", kwlist,
				&newpass, &ConfigType, &cfg, &oldpass,
				&pw.pw_name, &pw.pw_passwd, &tmp, &tmp,
				&pw.pw_gecos, &pw.pw_dir, &pw.pw_shell))
		return NULL;

	if (cfg == NULL)
		cfg = (ConfigObject *)PyObject_CallNoArgs((PyObject *)&ConfigType);

	if ((result = passwdqc_check(&cfg->params.qc, newpass, oldpass, pw.pw_name? &pw : NULL)))
		pyresult = PyUnicode_Decode(result, strlen(result), NULL, NULL);

	Py_INCREF(pyresult);
	return pyresult;
}

static PyMethodDef PWQC_Methods[] = {
	{"generate", generate, METH_VARARGS,
	 "Generate a random passphrase.\n\
	 \n\
	 generate() -> str: use default passwdqc settings\n\
	 generate(cfg: config) -> str: — use custom config object"
	},
	{"check", (PyCFunction) check, METH_VARARGS | METH_KEYWORDS,
	 "Check if new password is valid.\n\
	 \n\
	 check(newpass: str[, config: str, oldpass: str, pwentry: tuple]) -> str\n\
	 \n\
	 If `config=` argument is not provided, default configuration block is used.\n\
	 If `oldpass=` argument is provided, check for old password based newpass.\n\
	 If `pwentry=` argument is provided, check for pwentry based newpass.\n\
	 `pwentry` can be pwd.getpwnam()-like tuple or 7-string tuple.\n\
	 \n\
	 On successful check return None, otherwise return error string.\n\
	 \n\
	 See passwdqc_check(3) for more information."
	},
	{NULL, NULL, 0, NULL}	/* Sentinel */
};

static struct PyModuleDef passwdqc = {
	PyModuleDef_HEAD_INIT,
	.m_name = "passwdqc",
	.m_doc = "High-level libpasswdqc bindings",
	.m_size = -1,	/* size of per-interpreter state of the module,
		or -1 if the module keeps state in global variables. */
	PWQC_Methods
};

PyMODINIT_FUNC
PyInit_passwdqc(void)
{
	PyObject *m;
	if (PyType_Ready(&ConfigType) < 0)
		return NULL;

	m = PyModule_Create(&passwdqc);
	if (m == NULL)
		return NULL;

	Py_INCREF(&ConfigType);
	if (PyModule_AddObject(m, "config", (PyObject *) &ConfigType) < 0) {
		Py_DECREF(&ConfigType);
		Py_DECREF(m);
		return NULL;
	}

	return m;
}
