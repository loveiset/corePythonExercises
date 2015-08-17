a=raw_input('enter from to and increment(usr "," to splt): ').split(',')

fromNumber=int(a[0])
toNumber=int(a[1])+1
increment=int(a[2])

aList=range(fromNumber,toNumber,increment)
for i in aList:
  print i,
