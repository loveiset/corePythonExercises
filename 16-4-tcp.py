from socket import *

host=raw_input('enter server ip(default 192.168.232.70): ').strip()
if host=='':
  host='192.168.232.70'

port=raw_input('enter port(default 21567): ').strip()
if port=='':
  port=21567
else:
  port=int(port)

BUFSIZE=1024
ADDR=(host,port)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
  data=raw_input('> ')
  if not data:
    break
  tcpCliSock.send(data)
  data=tcpCliSock.recv(BUFSIZE)
  if not data:
    break
  print data

tcpCliSock.close()
