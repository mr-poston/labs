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
def check_circle():
  """circle radius is 35"""
  datafile = file('tracy.py')
  found = False
  for line in datafile:
    if "circle(35)" in line:
      found = True
      break
  if not found:
    raise check50.Mismatch("","")
