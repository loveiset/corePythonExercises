errors=0
nameCount=int(raw_input('enter total names: '))
i=0
names=[]
while i<nameCount:
  name=raw_input('enter name %d (format: lastname,firstname): ' % i)
  if ',' in name[:len(name)-1]:
    names.append(name)
    i+=1
  else:
    errors+=1
    print 'you have done this %d time(s)' % errors

for i in sorted(names):
  print i
