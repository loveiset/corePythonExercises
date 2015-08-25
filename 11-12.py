import time()

def timeit(func,*nkw,**kw):
  try:
    retval=func(*nkw,**kw)
    result=(True
