f=open('test.txt','r')
for eachLine in f:
  if eachLine[0]!='#':
    print eachLine,

f.seek(0)
for eachLine in f:
  count=eachLine.find('#')
  if count==-1:
    print eachLine,
  elif count==0:
    pass
  else:
    print eachLine[:count]

f.close()
