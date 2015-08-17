def factor(num):
  factors=[]
  count=1
  while count<num:
    if num%count==0:
      factors.append(count)
    count+=1
  return factors

def isPerfect(num):
  if sum(factor(num))==num:
    return True
  return False

a=int(raw_input('enter a number: '))
print factor(a)
print isPerfect(a)
