class MoneyFmt(float):
  def __new__(cls,value):
    return super(MoneyFmt,cls).__new__(cls,value)

  def __init__(self,value=0.0):
    self.money=float(value)

  def update(self,value=None):
    if value:
      try:
        self.money=float(value)
      except TypeError,e:
        print e

  def __str__(self):
    if self.money<0:
      symble=1
    else:
      symble=0
    val=str(round(abs(self.money),2)).split('.')
    valstring=list(str(val[0])[::-1])
    valstringNew=[]
    i=1
    count=0
    while i<=len(valstring):
      valstringNew.append(valstring[i-1])
      if i%3==0 and i!=0:
        count+=1
        if count<len(valstring)/3.0:
          valstringNew.append(',')
      i+=1
    print valstringNew
    valstringNew.reverse()
    return  '-'*symble + '$' + ''.join(valstringNew)+'.'+val[1]

  def __repr__(self):
    return repr(self.money)

  def __nonzero__(self):
    return self.money

a=MoneyFmt('-9824365.59')
b=MoneyFmt('234567.3423')
print b
print a
