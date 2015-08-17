filename=raw_input('enter a file: ').strip()

try:
  f=open(filename,'r')
except IOError:
  print 'file not exists'

lines=len(f.readlines())
print 'your file length is: %d' % lines
