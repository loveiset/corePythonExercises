def countString(istr):
  words=len(istr.split(' '))
  yuan=fu=0
  for s in istr:
    if s.isalpha():
      if s in 'aeiouAEIOU':
        yuan+=1
      else:
        fu+=1
  return (words,yuan,fu)

a=raw_input('enter a string: ')
print countString(a)
