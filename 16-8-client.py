from socket import *
import select,sys

HOST='192.168.232.82'
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
inputSocks=[tcpCliSock,sys.stdin]

while True:
  readyInput,readyOutput,readyException=select.select(inputSocks,[],[])
  for indata in readyInput:
    if indata==tcpCliSock:
      data=tcpCliSock.recv(BUFSIZE)
      if not data:
        break
      print data
    else:
      data=raw_input('> ')
      if not data:
        break
      tcpCliSock.send(data)
tcpCliSock.close()
