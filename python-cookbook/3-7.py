import datetime
import dateutil.parser
def tryparse(date):
  kwargs={}
  if isinstance(date,(tuple,list)):
    date=''.join([str(x) for x in date])
  elif isinstance(date,int):
    date=str(date)
  elif isinstance(date,dict):
    kwargs=date
    date=kwargs.pop('date')
  try:
    try:
      parsedate=dateutil.parser.parse(date,**kwargs)
      print 'sharp %r->%s'%(date,parsedate)
    except ValueError:
      parsedate=dateutil.parser.parse(date,fuzzy=True,**kwargs)
      print 'fuzzy %r->%s'%(date,parsedate)
  except Exception,err:
    print 'can not parse %r (%s)'%(date,err)

if __name__=='__main__':
  tests=(
    'January 3,2003',
    (5,"oct",55),
    'Thursday,November 18',
    '7/24/04',
    '24-7-2004',
    {'date':'5-10-1955','dayfirst':True},
    '5-10-1955',
    19950317,
    '11AM on the 11th day of 11th month,in the year of our Lord 1945',)

  for test in tests:
    tryparse(test)
