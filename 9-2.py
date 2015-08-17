filename=raw_input('enter file name: ').strip()
line=int(raw_input('enter lines: '))

try:
  f=open(filename,'r')
except IOError:
  print 'file not exists'

lines=f.readlines()

for i in lines[:line]:
  print i,
