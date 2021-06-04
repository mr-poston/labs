import check50

@check50.check()
def exists():
    """main.py exists"""
    check50.exists("main.py")

@check50.check(exists)
def compiles():
    """No syntax errors in main.py"""
    check50.run("python3 -m py_compile main.py").exit(0)
