#! /usr/bin/python
import os.path
import zipfile

tppath = 'rendu/'
tpname = 'tp'

class bc:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    OK = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'

def print_ok(string):
    print bc.OK + string + bc.END

def print_fail(string):
    print bc.FAIL + string + bc.END

def print_warning(string):
    print bc.WARNING + string + bc.WARNING

f_login = open('logins.txt', 'r').read().splitlines()

def compute_authors(path, login):
    f = open(path + 'AUTHORS').read()
    if f == '* ' + login + '\r\n' or f == '* ' + login + '\n':
        print_ok('> AUTHORS: OK')
    elif f == '* ' + login:
        print_fail('> AUTHORS: Missing second line')
    else:
        print_fail('> AUTHORS: Syntax error')

def compute_test(path, login):
    if os.path.isfile(path + 'AUTHORS'):
        compute_authors(path, login)
    else:
        print_fail('> missing AUTHORS')

def unzip_archive(archive, login):
    path = 'unzip/' + login + '/'
    zipfile.ZipFile(archive + '.zip').extractall(path)
    path += login + '/'
    if os.path.exists(path):
        print_ok('> Directory: OK')
        compute_test(path, login)
    else:
        print_fail('> missing ' + login + '/ folder in archive')

def test_archive(login):
    archive = tppath + 'rendu-' + tpname + '-' + login
    print login + ':'
    if not os.path.isfile(archive+'.zip'):
        print_fail('> missing rendu')
    else:
        unzip_archive(archive, login)
    print ''

for line in f_login:
    test_archive(line)
