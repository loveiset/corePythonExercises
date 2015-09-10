from socket import *

HOST='www.baidu.com'
PORT=80
ADDR=(HOST,PORT)

cliSock=socket(AF_INET,SOCK_STREAM)
cliSock.connect(ADDR)

cliSock.send('GET /index.html HTTP/1.0\r\n\r\n')
data=cliSock.recv(100000)
print data
