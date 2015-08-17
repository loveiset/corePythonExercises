filename=raw_input('enter a file: ').strip()

try:
  f=open(filename,'r')
except IOError:
  print 'file not exists'

i=0
while i<5:
  line=f.readline()
  if line:
    print line,
    i+=1
  else:
    print 'file end'
    break
  if i==5:
    if raw_input('anykey to continue'):
      i=0
