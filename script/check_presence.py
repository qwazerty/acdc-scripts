#! /usr/bin/python -B

import subprocess
import re

from prints import bc
from prints.print_color import *

total = 0
ok = 0

f_login = open('logins.txt', 'r').read().splitlines()
proc = subprocess.Popen(["ns_who"], stdout=subprocess.PIPE)
#proc = subprocess.Popen(["cat", "ns_who"], stdout=subprocess.PIPE)
ns_who = proc.stdout
ns_who = ns_who.read()

for line in f_login:
    match = re.search( line, ns_who, re.I)
    total += 1
    if match:
        print_ok(line)
        ok += 1
    else:
        print_fail(line + ': not found')

print ''
print_header('Total:   ' + str(total))
print_ok(    'OK:      ' + str(ok))
print_fail(  'Missing: ' + str(total - ok))
