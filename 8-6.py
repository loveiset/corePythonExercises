def isPrime(num):
  count=num/2
  while count>1:
    if num%count==0:
      return False
    count-=1
  else:
    return True

def getFactor(num):
  factors=[]
  count=1
  while count<=num:
    if num%count==0:
      factors.append(count)
    count+=1
  return factors

def primeFactors(num):
  result=[]
  if isPrime(num):
    result=[1,num]
  else:
   prime=2
   count=num/2
   while prime<=count:
     if num%prime==0:
       num/=prime
       result.append(prime)
       continue
     prime+=1
  return result
a=int(raw_input('enter a number: '))
print getFactor(a)
print primeFactors(a)
