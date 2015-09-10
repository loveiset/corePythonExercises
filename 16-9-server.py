from socket import *
from time import ctime
import threading

HOST=''
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)

def deal(sock,username,room):
  while True:
    data=sock.recv(BUFSIZE)
    for i in clients[room].iterkeys():
      if i != username:
        if data !='quit':
          clients[room][i].send('[%s] %s: %s' % (ctime(),username,data))
        else:
          clients[room][i].send('user %s at %s quit room %s' % (username,ctime(),room))
    if data=='quit':
      del clients[room][username]
      sock.send(data)
      sock.close()
      break

clients={'':{},}
chatSerSock=socket(AF_INET,SOCK_STREAM)
chatSerSock.bind(ADDR)
chatSerSock.listen(5)

while True:
  print 'waiting connections'
  chatCliSock,addr=chatSerSock.accept()
  print 'connected from: ',addr
  data=chatCliSock.recv(BUFSIZE)
  username,room=split(data)
  print username
  if not clients.has_key(room):
    clients[room]={}
  if clients[room].has_key(username):
    chatCliSock.send('reuse')
    chatCliSock.close()
  else:
    chatCliSock.send('success')
    clients[room][username]=chatCliSock
    t=threading.Thread(target=Deal,args=(chatCliSock,username,room))
    t.start()

chatSerSock.close()
