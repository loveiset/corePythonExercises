from random import randint
def createSet():
  setLen=randint(1,10)
  numbers=set()
  for i in range(setLen):
    number=randint(0,9)
    numbers.add(number)
  return numbers

if __name__=='__main__':
  a=createSet()
  b=createSet()
  print 'a is',a
  print 'b is',b

  print '----or exercise----'
  for i in range(3):
    numbers=raw_input('enter numbers (use ","): ').split(',')
    userSet=set([int(x) for x in numbers])
    if userSet==a|b:
      print 'you win'
      break
    else:
      print 'wrong answer'
  else:
    print 'actual result is:',a|b

  print '----and exercise----'
  for i in range(3):
    numbers=raw_input('enter number (use ","): ').split(',')
    userSet=set([int(x) for x in numbers])
    if userSet==a&b:
      print 'you win'
      break
    else:
      print 'wrong answer'
  else:
    print 'actual result is:',a&b
