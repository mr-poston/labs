import check50

@check50.check()
def exists():
  """tracy.py exists."""
  check50.exists("tracy.py")
  
@check50.check(exists)
  def check_draw():
    """draws 5 circles spaced by 40"""
    grader = open("grader.py", "w")
    tracy = open("tracy.py", "r")
    for line in tracy:
      if line.strip() == "circle(35)":
        grader.write("print(circle(35))")
      elif line.strip() == "forward(40)":
        grader.write("print(forward(40))")
      else:
        grader.write(line)
    grader.close()
    tracy.close()
    check50.run("python grader.py").stdout("circle(35)\nforward(40)" + \
                                           "circle(35)\nforward(40)" + \
                                           "circle(35)\nforward(40)" + \
                                           "circle(35)\nforward(40)" + \
                                           "circle(35)\nforward(40)", regex=False).exit(0)

@check50.check()
def check_circles():
  """code creates 5 circles with radii of 35"""
  datafile = open("tracy.py", "r")
  count = 0
  for line in datafile:
    if line.strip() == "circle(35)":
      count += 1
  if count != 5:
    raise check50.Failure("5 circles with radii of 35 not found")

@check50.check()
def check_forward():
  """Tracy moves forward 40 after every circle"""
  datafile = open("tracy.py", "r")
  result = ""
  for line in datafile:
    if line.strip() == "circle(35)":
      result += "c"
    if line.strip() == "forward(40)":
      result += "f"
  if result != "cfcfcfcfcf":
    raise check50.Failure("Tracy did not move forward 40 after each circle")
