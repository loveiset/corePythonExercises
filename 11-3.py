def my_max(a,b):
  return max(a,b)

def my_min(a,b):
  return min(a,b)

print 'a=3,b=8'
a=3
b=8
print 'max',my_max(a,b)
print 'min',my_min(a,b)

print 'a=abc b=def'
a='abc'
b='def'
print 'max',my_max(a,b)
print 'min',my_min(a,b)

def max2(a,b,*nkw):
  new=[]
  new.append(a)
  new.append(b)
  for i in nkw:
    new.append(i)
  return max(new)

print '(3,6.2,-5,33,53,6,-8.4)'
print max2(3,6.2,-5,33,53,6,-8.4)

print 'abc,ade,bab,dae,baf'
print max2('abc','ade','bab','dae','baf')
