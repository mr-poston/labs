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
    """drawing matches description"""
    grader = open("grader.py", "w")
    tracy = open("tracy.py", "r")
    for line in tracy:
        if line.strip() == "from turtle import *":
            grader.write("#" + line)
        elif line.strip() == 'shape("turtle")':
            grader.write("#" + line)
        elif line.strip() == "mainloop()":
            grader.write("#" + line)
        elif line.strip() == "circle(35)":
            grader.write(line.replace("circle(35)", "print('circle(35)')"))
        elif line.strip() == "forward(40)":
            grader.write(line.replace("forward(40)", "print('forward(40)')"))
        else:
            grader.write(line)
    grader.close()
    tracy.close()
    check50.run("python3 grader.py").stdout("circle(35)\nforward(40)\n" + \
    "circle(35)\nforward(40)\n" + \
    "circle(35)\nforward(40)\n" + \
    "circle(35)\nforward(40)\n" + \
    "circle(35)\nforward(40)", regex=False).exit(0)
