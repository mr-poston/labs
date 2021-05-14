import check50

@check50.check()
def exists():
  """tracy.py exists."""
  check50.exists("tracy.py")
  
@check50.check(exists)
def compiles():
  """no syntax errors in tracy.py"""
  check50.run("python -m py_compile tracy.py").exit(0)
