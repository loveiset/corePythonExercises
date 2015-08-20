import os
def copyFile(a,b):
  for i in a:
    b.write(i)

if __name__=='__main__':
  done=False
  while not done:
    filea=raw_input('enter filea: ')
    if not os.path.exists(filea):
      print 'file not exiest'
    else:
      done=True
  fileb=raw_input('enter fileb: ')
  a=open(filea,'r')
  b=open(fileb,'w')
  copyFile(a,b)
  a.close()
  b.close()
