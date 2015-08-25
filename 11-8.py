def isRunNian(year):
  if (year%4==0 and year%100!=0) or year%400==0:
    return True
  else:
    return False

years=[2004,2000,1000,2400,1989]
print filter(isRunNian,years)

print [x for x in years if isRunNian(x)==True]
