def fab(n):
  if n==1 or n==2:
    return 1
  else:
    return fab(n-1)+fab(n-2)

a=int(raw_input('enter a number: '))
print fab(a)
