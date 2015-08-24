import math

def safe_sqrt(num):
  try:
    retval=math.sqrt(num)
  except ValueError:
    retval=complex(0,math.sqrt(abs(num)))
  return retval

a=raw_input('enter a number: ')
print safe_sqrt(float(a))
