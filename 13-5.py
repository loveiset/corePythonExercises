import math
class Point(object):

  def __init__(self,x=0.0,y=0.0):
    self.X=x
    self.Y=y

class Line(object):

  def __init__(self,startPoint,endPoint):
    self.start=startPoint
    self.end=endPoint

  def length(self):
    length=math.sqrt((self.end.X-self.start.X)**2 + (self.end.Y-self.start.Y)**2)
    return length

  def __repr__(self):
    return '((%f,%f),(%f,%f))' % (self.start.X,self.start.Y,self.end.X,self.end.Y)

  def slope(self):
    if self.start.X==self.end.X:
      return None
    else:
      return (self.end.Y-self.start.Y)/(self.end.X-self.start.X)

if __name__=='__main__':
  p1=Point(3,5)
  p2=Point(2,4)
  l=Line(p1,p2)
  print l.length()
  print l.slope()
  print l
