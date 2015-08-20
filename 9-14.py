import sys

if sys.argv[1]=='print':
  f=open('caculate.txt','rw+')
  for i in f:
    print i,
  f.seek(0)
  f.truncate()
  f.close()
else:
  f=open('caculate.txt','aw')
  if sys.argv[2] in ('+','*','/','**','%','-'):
    istr=' '.join(sys.argv[1:])
    f.write(istr+'\n')
    print eval(istr)
    f.write(str(eval(istr))+'\n')
  else:
    print 'error oprator'
  f.close()

