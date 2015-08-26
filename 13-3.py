class MoneyFmt(object):
  def __init__(value):
    self.money=float(value)

  def update(self,value=None):
    if value:
      try:
        self.money=float(value)
      except TypeError,e
        print e

  def __str__(self):
    if self.money<0:
      symble=1
    else:
      symble=0
    val=str(round(abs(self.money),2)).split('.')
    valstring=list(str(val[0])[::-1])
    valstringNew=[]
    i=0
    count=len(valstring)/3
    while i<count:
      valstringNew.append(valstring[i])
      if i%3==0 and i!=0:
        valstringNew.append(',')
      i+=1
    return  '-'*symble + '$' + ''.join(valstringNew.reverse())

  def __repr__(self):
    return repr(self.money)

  def __nonzero__(self):
    return self.money

