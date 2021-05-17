import check50

@check50.check()
def exists():
    """tracy.py exists"""
    check50.exists("tracy.py")

@check50.check(exists)
def compiles():
    """No syntax errors in tracy.py"""
    check50.run("python3 -m py_compile tracy.py").exit(0)

@check50.check(compiles)
def check_draw():
    """Drawing looks correct"""
    turtle = ["from turtle import *", 'shape("turtle")', "screensize(400, 400)", \
        "setup(410, 410)", 'title("Shorter Dashed Line")', "exitonclick()"]
    grader = open("grader.py", "w")
    tracy = open("tracy.py", "r")
    for line in tracy:
        if line.strip() in turtle:
            grader.write("#" + line)
        elif line.strip() == 'penup()':
            grader.write(line.replace('penup()', 'print("penup()")'))
        elif line.strip() == 'backward(200)':
            grader.write(line.replace('backward(200)', 'print("backward(200)")'))
        elif line.strip() == 'backward(200)':
            grader.write(line.replace('forward(50)', 'print("forward(50)")'))
        elif line.strip() == 'pendown()':
            grader.write(line.replace('pendown()', 'print("pendown()")'))
        else:
            grader.write(line)
    grader.close()
    left = False
    lines = False
    for line in tracy:
        if "backward(200)" in line:
            left = True
        if "forward(50)" in line:
            spaces = True
    tracy.close()
    if not left:
        raise check50.Failure("Did you move Tracy backwards 200?")
    if not lines:
        raise check50.Failure("Did you draw both lines and spaces 50 pixels long?")
    check50.run("python3 grader.py").stdout("penup()\nbackward(200)\n" + \
        "pendown()\nforward(50)\npenup()\nforward(50)\n" + \
        "pendown()\nforward(50)\npenup()\nforward(50)\n" + \
        "pendown()\nforward(50)\npenup()\nforward(50)\n" + \
        "pendown()\nforward(50)\npenup()\nforward(50)\n", regex=False).exit(0)