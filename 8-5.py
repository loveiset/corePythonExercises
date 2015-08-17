def getFactor(num):
  count=num/2
  factors=[]
  while count>=1:
    if num%count==0:
      factors.append(count)
    count-=1
  return factors

num=int(raw_input('enter a number: '))
for i in getFactor(num):
  print i,
