#! /usr/bin/python -B

# Import libs
import os.path
import zipfile

# Import custom modules
from check_archive import var
from prints import bc
from prints.print_color import *

# Config variables
tppath = 'rendu/'
tpname = 'tp'

f_login = open('logins.txt', 'r').read().splitlines()

def compute_authors(path, login):
    f = open(path + 'AUTHORS').read()
    if f == '* ' + login + '\r\n' or f == '* ' + login + '\n':
        print_ok('> AUTHORS: OK')
    elif f == '* ' + login:
        print_fail('> AUTHORS: Missing second line')
        var.curr_valid = 0
        var.fail_authors += 1
    else:
        print_fail('> AUTHORS: Syntax error')
        var.curr_valid = 0
        var.fail_authors += 1

def compute_test(path, login):
    global curr_valid
    global fail_authors
    if os.path.isfile(path + 'AUTHORS'):
        compute_authors(path, login)
    else:
        print_fail('> missing AUTHORS')
        var.curr_valid = 0
        var.fail_authors += 1

def unzip_archive(archive, login):
    global curr_valid
    global fail_directory
    path = 'unzip/' + login + '/'
    zipfile.ZipFile(archive + '.zip').extractall(path)
    path += login + '/'
    if os.path.exists(path):
        print_ok('> Directory: OK')
        compute_test(path, login)
    else:
        print_fail('> missing ' + login + '/ folder in archive')
        var.curr_valid = 0
        var.fail_directory += 1

def test_archive(login):
    global curr_valid
    global missing_rendu
    archive = tppath + 'rendu-' + tpname + '-' + login
    print login + ':'
    if not os.path.isfile(archive+'.zip'):
        print_fail('> missing rendu')
        var.curr_valid = 0
        var.missing_rendu += 1
    else:
        unzip_archive(archive, login)
    print ''

for line in f_login:
    var.total += 1
    var.curr_valid = 1
    test_archive(line)
    if var.curr_valid == 1:
        var.ok += 1

print_header( 'Total:          ' + str(var.total))
print_ok(     'OK:             ' + str(var.ok))
print_warning('Fail AUTHORS:   ' + str(var.fail_authors))
print_warning('Fail Directory: ' + str(var.fail_directory))
print_fail(   'Missing rendu:  ' + str(var.missing_rendu))
