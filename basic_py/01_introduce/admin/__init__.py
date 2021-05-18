import check50

@check50.check()
def exists():
    """main.py exists"""
    check50.exists("main.py")

@check50.check(exists)
def compiles():
    """No syntax errors in main.py"""
    check50.run("python3 -m py_compile main.py").exit(0)

@check50.check(compiles)
def check_lines():
    """Your program should print at least two lines of code"""
    check50.run("python3 main.py").stdout(".+\n.+", regex=True).exit(0)

@check50.check(compiles)
def check_name():
    """Your first line should contain 'name'"""
    check50.run("python3 main.py").stdout(".+name.*\n.+", regex=True).exit(0)

@check50.check(compiles)
def check_like():
    """Your first line should contain 'like'"""
    check50.run("python3 main.py").stdout(".+\n.+like.*", regex=True).exit(0)