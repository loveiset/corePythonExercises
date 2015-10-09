import datetime
from dateutil import rrule,easter
try: set
except NameError:from sets import Set as set
def all_easter(start,end):
  easters=[easter.easter(y) for y in xrange(start.year,end.year+1)]
  return [d for d in easters if start<=d<=end]
def all_boxing(start,end):
  one_day=datetime.timedelta(days=1)
  boxings=[easter.easter(y)+one_day for y in xrange(start.year,end.year+1)]
  return [d for d in boxings if start<=d<=end]
def all_christmas(start,end):
  christmases=[datetime.date(y,12,25) for y in xrange(start.year,end.year+1)]
  return [d.date() for d in christmases if start<=d<=end]
def all_labor(start,end):
  labors=rrule.rrule(rrule.YEARLY,bymonth=9,byweekday=rrule.MO(1),dtstart=start,until=end)
  return [d.date() for d in labors]
def read_holidays(start,end,holidays_file='holidays.txt'):
  try:
    holidays_file=open(holidays_file)
  except IOError,err:
    print 'can not read (%r):'%(holidays_file,),err
    return []
  holidays=[]
  for line in holidays_file:
    if line.isspace() or line.startswith('#'):
      continue
    try:
      y,m,d=[int(x.strip()) for x in line.split(',')]
      date=datetime.date(y,m,d)
    except ValueError:
      print 'invalid line %r in file %r'%(line,holidays_file)
      continue
    if start<=date<=end:
      holidays.append(date)
  holidays_file.close()
  return holidays
holidays_by_country={
  'US':(all_easter,all_christmas,all_labor),
  'IT':(all_easter,all_boxing,all_christmas),
}
def holidays(cc,start,end,holidays_file='holidays.txt'):
  all_holidays=read_holidays(start,end,holidays_file)
  functions=holidays_by_country.get(cc,())
  for function in functions:
    all_holidays+=function(start,end)
  #all_holidays.sort()
  #return all_holidays
  return len(all_holidays)

if __name__=='__main__':
  test_file=open('test_holidays.txt','w')
  test_file.write('2004,9,6\n')
  test_file.close()
  testdates=[(datetime.date(2004,8,1),datetime.date(2004,11,14)),
    (datetime.date(2003,2,28),datetime.date(2003,5,30)),
    (datetime.date(2004,2,28),datetime.date(2004,5,30)),]
  def test(cc,testdates,expected):
    for (s,e),expect in zip(testdates,expected):
      print 'total %s from %s to %s is %d(exp %d)'%(
      cc,s,e,holidays(cc,s,e,test_file.name),expect)
      print
  test('US',testdates,(1,1,1))
  test('IT',testdates,(1,2,2))
  import os
  os.remove(test_file.name)
