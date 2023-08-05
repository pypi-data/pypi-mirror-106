#!/usr/bin/env python3
'''
'''
import sys
import os
import pwd

sys.path.append(os.path.join(os.getcwd(), "build/lib.linux-x86_64-3.9"))

import passwdqc
c0 = passwdqc.config()
c1 = passwdqc.config("config=/etc/passwdqc.conf")
c2 = passwdqc.config("min=16,8,7,6,5", "max=38", "random=27")

inpass = "wyr", "WERsfWas", "WsBgUUzz", "!QAWS@E#D$RF", "WsBgUUzz", "WsBgUUzz", "qee mooo boo"

for c in c0, c1, c2:
    print(c, c is c0 and "(default)" or "")
    print("  Generate", passwdqc.generate(c))
    for i, p in enumerate(inpass):
        print(f"    '{p}'")
        print(f"      Default:", passwdqc.check(p) or "OK")
        print(f"      Single:", passwdqc.check(p, config=c) or "OK")
        print(f"      History:", passwdqc.check(p, config=c, oldpass=inpass[i-1]) or "OK")
        print(f"      Full:", passwdqc.check(p, config=c, oldpass=inpass[i-1], pwentry=inpass[:7]) or "OK")
        print(f"      pwent:", passwdqc.check(p, config=c, oldpass=inpass[i-1], pwentry=pwd.getpwnam("root")) or "OK")

if sys.argv[1:2] == ["-"]:
    help(passwdqc)
