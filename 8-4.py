def isPrime(num):
  count=num/2
  while count>1:
    if num%count==0:
      return False
    count-=1
  else:
    return True

num=int(raw_input('enter a number: '))
print isPrime(num)
