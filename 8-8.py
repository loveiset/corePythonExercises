def factorial(num):
  if num==0 or num==1:
    return 1
  else:
    return factorial(num-1)*num

a=int(raw_input('enter a number: '))
print factorial(a)
