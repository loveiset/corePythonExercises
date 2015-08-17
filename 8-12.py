def printTable(start,end):
  hasASCII=False
  for i in range(start,end+1):
    if i in range(32,127):
      hasASCII=True
      break
  if hasASCII:
    print 'dec'.ljust(10)+'bin'.ljust(10)+'oct'.ljust(10)+'hex'.ljust(10)+'ascii'.ljust(10)
    print '-'*50
    for i in range(start,end+1):
      if 32<=i<=127:
        print str(i).ljust(10)+str(bin(i)).ljust(10)+str(oct(i)).ljust(10)+str(hex(i)).ljust(10)+chr(i).ljust(10)
      else:
        print str(i).ljust(10)+str(bin(i)).ljust(10)+str(oct(i)).ljust(10)+str(hex(i)).ljust(10)
  else:
    print 'dec'.ljust(10)+'bin'.ljust(10)+'oct'.ljust(10)+'hex'.ljust(10)
    print '-'*40
    for i in range(start,end+1):
      print str(i).ljust(10)+str(bin(i)).ljust(10)+str(oct(i)).ljust(10)+str(hex(i)).ljust(10)

a=int(raw_input('enter start: '))
b=int(raw_input('enter end: '))
printTable(a,b)
