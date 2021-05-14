import check50

@check50.check()
def exists():
  """tracy.py exists."""
  check50.exists("tracy.py")
  
@check50.check(exists)
def compiles():
  """no syntax errors in tracy.py"""
  check50.run("python -m py_compile tracy.py").exit(0)

@check50.check(compiles)
def check_circles():
  """code creates 5 circles with radii of 35"""
  datafile = open("tracy.py", "r")
  count = 0
  for line in datafile:
    if line.strip() == "circle(35)":
      count += 1
  if count != 5:
    raise check50.Failure("5 circles with radii of 35 not found")

@check50.check(compiles)
def check_forward():
  """Tracy moves forward 40 after every circle"""
  datafile = open("tracy.py", "r")
  count = 0
  for line in datafile:
    if line.strip() == "circle(35)":
      if datafile.next().strip() == "forward(40)":
        count +=1
  if count != 5:
    raise check50.Failure("Tracy did not move forward 40 after each circle")
