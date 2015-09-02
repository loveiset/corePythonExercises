class Time60(object):

#  def __init__(self,hr=0,min=0):
#    self.hr=hr
#    self.min=min

  def __str__(self):
    return '%02d:%02d' % (self.hr,self.min)

  def __repr__(self):
    return '%s("%02d:%02d")' % self.__class__,self.hr,self.min

  def __init__(self,*val):
    if type(val[0]) is tuple:
      self.hr=val[0][0]
      self.min=val[0][1]
    elif type(val[0]) is str:
      self.hr=int(val[0].split(':')[0])
      self.min=int(val[0].split(':')[1])
    elif type(val[0]) is dict:
      self.hr=val[0]['hr']
      self.min=val[0]['min']
    elif type(val) is tuple:
      self.hr=val[0]
      self.min=val[1]

  def __add__(self,other):
    hour=self.hr+other.hr
    min=self.min+other.min
    if min>=60:
      min-=60
      hour+=1
    return self.__class__(hour,min)

  def __iadd__(self,other):
    self.hr+=other.hr
    self.min+=other.min
    if self.min>=60:
      self.min-=60
      self.hr+=1
    return self


if __name__=='__main__':
  time1=Time60(10,30)
  time2=Time60({'hr':10,'min':30})
  time3=Time60('10:30')
  time4=Time60('12:5')

  time5=Time60(8,45)

  print time1
  print time2
  print time3
  print time4
  print time5

  print time1+time5
  time1+=time5
  print time1
