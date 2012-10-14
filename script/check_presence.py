#! /usr/bin/python -B

import subprocess
import re

from prints import bc
from prints.print_color import *

f_login = open('logins.txt', 'r').read().splitlines()
proc = subprocess.Popen(["ns_who"], stdout=subprocess.PIPE)
ns_who = proc.stdout
ns_who = ns_who.read()

for line in f_login:
    match = re.search( line, ns_who, re.I)
    if match:
        print_ok(line)
    else:
        print_fail(line + ': not found')
