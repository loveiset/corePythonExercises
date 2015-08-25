import time

def timeit(func,*nkw,**kw):
  try:
    start=time.time()
    retval=func(*nkw,**kw)
    end=time.time()
    wasteTime=end-start
    result=(True,retval,wasteTime)
  except Exception,e:
    end=time.time()
    wasteTime=end-start
    result=(False,str(e),wasteTime)
  return result

def test():
  funcs=(int,long,float)
  vals=(1234,12.34,'1234','12.34')
  for eachfun in funcs:
    print '_'*20
    for eachval in vals:
      retval=timeit(eachfun,eachval)
      if retval[0]:
        print '%s(%s)= '%(eachfun.__name__,'eachval'),retval[1]
        print 'time is',retval[2]
      else: 
        print '%s(%s)= failed:'%(eachfun.__name__,'eachval'),retval[1]
        print 'time is',retval[2]
  
if __name__=='__main__':
  test()
