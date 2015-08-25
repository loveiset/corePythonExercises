import time
def timeit(func,*nkw,**kw):
  start=time.time()
  retval=func(*nkw,**kw)
  end=time.time()
  wasteTime=end-start
  result=(retval,wasteTime)
  return result

def fab3(x):
  if x==0 or x==1:
    return 1
  else:
    return x*fab3(x-1)

def mult(x,y):
  return x*y

def fab(x):
  if x==1 or x==0:
    return 1
  else:
    return reduce(mult,range(x+1)[1:])

def fab2(x):
  if x==1 or x==0:
    return 1
  else:
    return reduce(lambda x,y:x*y,range(x+1)[1:])




def test():
  funcs=(fab,fab2,fab3)
  vals=(7,30,40)
  for eachfun in funcs:
    print '_'*20
    for eachval in vals:
      retval=timeit(eachfun,eachval)
      print '(%s) value is =' % (eachfun.__name__),retval[0]
      print 'time is',retval[1]
  
if __name__=='__main__':
  test()
