import check50

@check50.check()
def exists():
  """tracy.py exists."""
  check50.exists("tracy.py")

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
