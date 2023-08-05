from setuptools import setup, Extension
from ctypes.util import find_library
import sys
OPT_SOLID = "--solid"

if (passwdqclib := find_library("passwdqc") and OPT_SOLID not in sys.argv):
    passwdqc = Extension('passwdqc',
                        define_macros = [('MAJOR_VERSION', '1'),
                                         ('MINOR_VERSION', '0')],
                        include_dirs = ['/usr/include'],
                        libraries = ['passwdqc'],
                        sources = ['passwdqc.c'])
else:
    import re
    import os
    if OPT_SOLID in sys.argv:
        sys.argv.remove(OPT_SOLID)
    srcdir = 'passwdqc'
    with open(os.path.join(srcdir, "Makefile")) as M:
        objs = re.findall(r"^OBJS_LIB = (.*)", M.read(), re.M)[0]
        sources = [os.path.join(srcdir, s.replace(".o",".c")) for s in objs.split()]
    passwdqc = Extension('passwdqc',
                        define_macros = [('MAJOR_VERSION', '1'),
                                         ('MINOR_VERSION', '0')],
                        include_dirs = ['/usr/include', srcdir],
                        sources = ['passwdqc.c'] + sources)

setup (name = 'passwdqc',
       version = '0.0.1',
       description = 'PasswdQC python wrapper',
       author = 'Fr. Br. George',
       author_email = 'george@altlinux.org',
       url = 'https://sr.ht/~frbrgeorge/PasswdqcPython/',
       long_description = '''
PasswdQC is a simple password strength checking PAM module,
and this Python module provides high-level bindings for libpasswdqc.
''',
       classifiers = [  'Programming Language :: C',
                        'License :: OSI Approved :: BSD License',
                        'Operating System :: POSIX :: Linux',
                     ],
       ext_modules = [passwdqc])
