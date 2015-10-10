import httplib
import smtplib
thresholdRate=1.30
smtpServer='smtp.www.com'
fromaddr='foo@q.com'
toaddrs='your@corp.com'

url='/en/financial_markets/csv/exchange_eng.csv'
conn=httplib.HTTPConnection('www.bankofcanada.ca')
conn.request('GET',url)
response=conn.getresponse()
date=response.read()
start=data.index('United States Dollar')
line=date[start:data,index('\n',start)]
rate=line.split(',')[-1]
if float(rate)<thresholdRate:
  msg='Subject: alert %s'%rate
  server=smtplib.SMTP(smtpServer)
  server.sendmail(fromaddr,toaddrs,msg)
  server.quit()
conn.close()
