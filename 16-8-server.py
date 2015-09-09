from socket import *
import select
import sys

HOST=''
PORT=21567
ADDR=(HOST,PORT)
BUFSIZE=1024

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
inputSocks=[tcpSerSock,sys.stdin]

while True:
  tcpCliSock,addr=tcpSerSock.accept()
  inputSocks.append(tcpCliSock)

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
