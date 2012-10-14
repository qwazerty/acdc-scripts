import bc

def print_ok(string):
    print bc.OK + string + bc.END

def print_fail(string):
    print bc.FAIL + string + bc.END

def print_warning(string):
    print bc.WARNING + string + bc.END

def print_header(string):
    print bc.HEADER + string + bc.END
