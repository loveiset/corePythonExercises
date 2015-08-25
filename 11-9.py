def average(seq):
  return float(reduce(lambda x,y:x+y,seq))/len(seq)

print average(range(10))
