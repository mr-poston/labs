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
def check_draw():
    """Drawing looks correct"""
    turtle = ["from __setup import *", "begin()", "end()"]
    grader = open("grader.py", "w")
    tracy = open("main.py", "r")
    for line in tracy:
        if line.strip() in turtle:
            grader.write("#" + line)
        elif "radius" in line and "+" in line:
            grader.write(line + "\n\tprint(radius)")
        elif "radius" in line and "circle" not in line:
            grader.write(line)
        elif "def " not in line:
            grader.write("#" + line)
        elif "for " not in line:
            grader.write("#" + line)
        else:
            grader.write(line)
    grader.close()
    tracy.close()
    check50.run("python3 grader.py").stdout("25\n50\n75\n100", regex=False).exit(0)

@check50.check(compiles)
def check_function():
    """You have a function in your code"""
    turtle = ["from __setup import *", "begin()", "end()"]
    grader = open("grader.py", "w")
    tracy = open("main.py", "r")
    for line in tracy:
        if "def " in line:
            grader.write('print("' + line.strip() + '")')
    grader.close()
    tracy.close()
    check50.run("python3 grader.py").stdout("^def [a-z].*\(\):$", regex=True).exit(0)

@check50.check(compiles)
def check_for():
    """You have a for loop in your code"""
    turtle = ["from __setup import *", "begin()", "end()"]
    grader = open("grader.py", "w")
    tracy = open("main.py", "r")
    for line in tracy:
        if "for " in line:
            grader.write('print("' + line.strip() + '")')
    grader.close()
    tracy.close()
    check50.run("python3 grader.py").stdout("^for [a-z].*\(4\):$", regex=True).exit(0)