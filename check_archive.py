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

f_login = open('logins.txt', 'r').read().splitlines()

def compute_authors(path, login):
    f = open(path + 'AUTHORS').read()
    if f == '* ' + login + '\r\n' or f == '* ' + login + '\n':
        print bc.OK + '> AUTHORS: OK' + bc.END
    elif f == '* ' + login:
        print bc.FAIL + '> AUTHORS: Missing second line' + bc.END
    else:
        print bc.FAIL + '> AUTHORS: Syntax error' + bc.END

def compute_test(path, login):
    if os.path.isfile(path + 'AUTHORS'):
        compute_authors(path, login)
    else:
        print bc.FAIL + '> missing AUTHORS' + bc.END

def unzip_archive(archive, login):
    path = 'unzip/' + login + '/'
    zipfile.ZipFile(archive + '.zip').extractall(path)
    path += login + '/'
    if os.path.exists(path):
        compute_test(path, login)
    else:
        print bc.FAIL + '> missing ' + login + '/ folder in archive'

def test_archive(login):
    archive = tppath + 'rendu-' + tpname + '-' + login
    print login + ':'
    if not os.path.isfile(archive+'.zip'):
        print bc.FAIL + '> missing rendu' + bc.END
    else:
        unzip_archive(archive, login)
    print ''

for line in f_login:
    test_archive(line)
