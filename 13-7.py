import datetime,time

class MyTime(object):

  def __init__(self,t_string=None,fmt=None):
    self.update(t_string)
    self.mode={'MDY':self.__mdy,
      'MDYY':self.__mdyy,
      'DMY':self.__dmy,
      'DMYY':self.__dmyy,
      'MODYY':self.__modyy}

  def update(self,t_string=None):
    if t_string:
      self.date=datetime.datetime.strptime(t_string,'%d/%m/%Y %H:%M:%S')
      self.local=self.date.strftime('%a %b %d %H:%M:%S %Y')
    else:
      self.local=time.ctime()
      self.date=datetime.datetime.strptime(self.local,'%a %b %d %H:%M:%S %Y')
    return self.date

  def display(self,fmt=None):
    if fmt==None:
      print self.local
    else:
      print self.mode[fmt]()

  def __mdy(self):
    return self.date.strftime('%m/%d/%y')

  def __mdyy(self):
    return self.date.strftime('%m/%d/%Y')

  def __dmy(self):
    return self.date.strftime('%d/%m/%y')

  def __dmyy(self):
    return self.date.strftime('%d/%m/%Y')

  def __modyy(self):
    return self.date.strftime('%b %d,%Y %H:%M:%S')

if __name__=='__main__':
  date1=MyTime()
  date1.display()

  date2=MyTime('5/6/2014 12:34:54')
  date2.display()
  

  date3=MyTime(fmt='DMYY')
  date3.display('DMYY')
