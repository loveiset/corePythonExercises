#-*- coding:utf-8 –*-
import decimal
def italformat(value,places=2,curr='EUR',sep='.',dp=',',pos='',neg='-',
  overall=10):
  """
    places:十进制小数点后面的位数
    curr:可选的货币符号
    sep:可选的分组分隔符
    dp:小数点指示符
    pos:正数的可选符号
    neg:负数的可选符号
    overall:最终结果的可选总长度
  """

  q=decimal.Decimal((0,(1,),-places))
  sign,digits,exp=value.quantize(q).as_tuple()
  result=[]
  digits=map(str,digits)
  append,next=result.append,digits.pop
  for i in range(places):
    if digits:
      append(next())
    else:
      append('0')
  append(dp)
  i=0
  while digits:
    append(next())
    i+=1
    if i==3 and digits:
      i=0
      append(sep)
  while len(result)<overall:
    append(' ')
  append(curr)
  if sign:append(neg)
  else:append(pos)
  result.reverse()
  return ''.join(result)

def getsubtotal(subtin=None):
  if subtin==None:
    subtin=input('enter the subtotal: ')
  subtotal=decimal.Decimal(str(subtin))
  print '\nsubtotal: ',italformat(subtotal)
  return subtotal

def cnpcalc(subtotal):
  contrib=subtotal*decimal.Decimal('.02')
  print '+contributo integrativo 2%: ',italformat(contrib,curr='')
  return contrib

def vatcalc(subtotal,cnp):
  vat=(subtotal+cnp)*decimal.Decimal('.20')
  print '+iva 20%: ',italformat(vat,curr='')
  return vat

def ritacalc(subtotal):
  rit=subtotal*decimal.Decimal('.20')
  print '-ritenuta dacconto 20%: ',italformat(rit,curr='')
  return rit

def dototal(subtotal,cnp,iva=0,rit=0):
  totl=(subtotal+cnp+iva)-rit
  print 'total: ',italformat(totl)
  return totl

def invoicer(subtotal=None,context=None):
  if context is None:
    decimal.getcontext().rounding='ROUND_HALF_UP'
  else:
    decimal.setcontext(context)
  subtot=getsubtotal(subtotal)
  contrib=cnpcalc(subtot)
  dototal(subtot,contrib,vatcalc(subtot,contrib),ritacalc(subtot))

if __name__=='__main__':
  tests=[100,1000.00,'10000',555.55]
  print 'euro context'
  for test in tests:
    invoicer(test)
  print 'default context'
  for test in tests:
    invoicer(test,context=decimal.DefaultContext)
