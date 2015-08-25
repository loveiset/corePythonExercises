def mix(a,b):
  if len(a)!=len(b):
    return None
  else:
    return map(lambda x,y:(x,y),a,b)


print mix([1,2,3],['a','b','c'])
