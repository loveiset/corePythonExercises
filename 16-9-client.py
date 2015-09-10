from socket import *
import threading
from getopt import gnu_getopt,GetoptError
from sys import argv,exit,stdout

helpinfo=['cs.py [-h | --help | -u | --username] username',
  '\t-h or --help\t show helpinfo',
  '\t-u or --username\t define useranme',
  '\t-r or --room\t define room']

def help():
  for i in helpinfo:
    print i

def send(sock,test):
  while True:
    data=raw_input('> ')
    sock.send(data)
    if data == 'quit':
      break

def receive(sock,test):
  while True:
    data=sock.recv(BUFSIZE)
    if data=='quit':
      sock.close()
      break
    str='\n'+data+'\n>'
    stdout.write(str)

HOST='192.168.232.82'
PORT=21567
BUFSIZE=1024
ADDR=(HOST,PORT)
threads=[]

if __name__=='__main__':
  try:
    opts,args=gnu_getopt(argv[1:],'hu:r:',['help','username=','room='])
  except GetoptError,err:
    print str(err)
    help()
    exit(2)
  username=''
  room=''
  print opts
  for o,a in opts:
    print a
    if o in ('-h','--help'):
      help()
      exit(0)
    elif o in ('-u','--username'):
      username=a
    elif o in ('-r','--room'):
      room=a
    else:
      print 'unknown option'
      help()
      exit(2)
  if not username or not room:
    help()
    exit(2)

  chatCliSock=socket(AF_INET,SOCK_STREAM)
  chatCliSock.connect(ADDR)
  chatCliSock.send('%s %s' % (username,room))
  data=chatCliSock.recv(BUFSIZE)
  if data=='reuse':
    print 'user %s loginto %s' % (username,room)
    raw_input()
    exit(1)
  elif data=='success':
    print 'user %s login room %s' % (username,room)
    t=threading.Thread(target=send,args=(chatCliSock,None))
    threads.append(t)
    t=threading.Thread(target=receive,args=(chatCliSock,None))
    threads.append(t)
    for i in range(len(threads)):
      threads[i].start()
    threads[0].join()
