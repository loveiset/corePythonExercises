import os

filename=''
filecontent=[]

def createFile():
  global filename
  done=False
  while not done:
    filename=raw_input('enter a filename: ').strip()
    if os.path.exists(filename):
      print 'file already exists'
    else:
      done=True

  f=open(filename,'w')

  while True:
    line=raw_input('enter content("." to quit): ').strip()
    if line!='.':
      f.write(line+'\n')
    else:
      break
  f.close()

def showFile():
  global filename,filecontent
  if filename=='':
    filename=raw_input('enter filename: ')
  f=open(filename,'r')
  filecontent=f.readlines()
  for i,j in enumerate(filecontent):
    print 'line %d: %s' % (i+1,j.strip())
  f.close()

def editFile():
  global filename,filecontent
  f=open(filename,'rw+')
  while True:
    lineNumber=int(raw_input('enter line you want to edit: ').strip())
    if lineNumber>len(filecontent):
      print 'max line is: %d' % len(filecontent)
    else:
      break
  print 'you choosed line: %s' % filecontent[lineNumber-1]
  newline=raw_input('enter newline: ').strip()
  filecontent[lineNumber-1]=newline+'\n'
  f.close()

def saveFile():
  global filename,filecontent
  f=open(filename,'w')
  f.writelines(filecontent)
  f.close()

def showmenu():
  prompt='''
(c)reate file
(s)how file
(e)dit file
(ss)ave file
(q)uit

you choice: '''

  done=False
  while not done:
    choosen=False
    while not choosen:
      try:
        choice=raw_input(prompt).strip().lower()
      except IOError,KeyboardInterrupt:
        choice='q'
      if choice not in ['c','s','e','ss','q']:
        print 'invalid option'
      else:
        choosen=True
    if choice=='q':done=True
    if choice=='c':createFile()
    if choice=='s':showFile()
    if choice=='e':editFile()
    if choice=='ss':saveFile()

if __name__=='__main__':
  showmenu()

