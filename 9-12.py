from time import ctime,time

db={}
def newuser():
  prompt='login desired: '
  while True:
    name=raw_input(prompt).lower()
    if db.has_key(name):
      prompt='name taken, try another: '
      continue
    else:
      break
  pwd=raw_input('passwd: ')
  db[name]=[md5(pwd),time()]

def olduser():
  name=raw_input('login: ').lower()
  pwd=raw_input('passwd: ')
  passwd=db.get(name)[0]
  if passwd==md5(pwd):
    tempTime=time()
    if tempTime-db.get(name)[1]<60*4:
      print 'you already logged in at:',ctime(db.get(name)[1])
    else:
      db.get(name)[1]=time()
      print 'welcom back',name
      print 'you last logined in at',ctime(db.get(name)[1])
  else:
    print 'login incorrect'

def md5(str):
  import hashlib
  m = hashlib.md5()   
  m.update(str)
  return m.hexdigest()

def manage():
  prompt='''
(d)eleter a user
(s)how all users
(r)eturn to main menu

your choice: '''

  done=False
  while not done:
    chosen=False
    while not chosen:
      choice=raw_input(prompt).strip()[0].lower()
      if choice not in 'dsr':
        print 'not valid option'
        break
      else:
        chosen=True
    if choice=='d':
      user=raw_input('enter the user you want to delete: ')
      if user not in db.keys():
        print 'user not exists'
      else:
        del db[user]
        print '%s deleted' % user
    elif choice=='s':
      for key in db:
        print 'username=%s,password=%s' % (key,db[key][0])
    else:
      done=True

def new_login():
  import re
  while True:
    user=raw_input('enter username: ').lower()
    if not re.match('^[0-9a-z]+$',user):
      print 'user wrong format'
    else:
      break
  
  password=raw_input('enter password: ')
  if db.has_key(user):
    passwd=db.get(user)[0]
    if passwd==md5(password):
      tempTime=time()
      if tempTime-db.get(user)[1]<60*4:
        print 'you already logged in at:',ctime(db.get(user)[1])
      else:
        db.get(user)[1]=time()
        print 'welcom back',user
        print 'you last logined in at',ctime(db.get(user)[1])
    else:
      print 'login incorrect'
  else:
    confirm=raw_input('user not exists, create it y/n? ').strip()[0].lower()
    if confirm=='y':
      db[user]=[md5(password),time()]
    else:
      print 'you cancled the create'

def admin():
  done=False
  while not done: 
    user=raw_input('enter admin username: ')
    if user!='admin':
      print 'admin username wrong'
    else:
      password=raw_input('enter admin passwd: ')
      if password!='admin':
        print 'admin passwd wrong'
      else:
        done=True
  a=raw_input('export user list? y/n :').strip().lower()
  if a=='y':
    f=open('user.txt','w')
    for i in db.keys():
      f.write('%s:%s:%s\n' % (i,db[i][0],ctime(db[i][1])))
    f.close()
  elif a=='n':
    print 'you canceled'
  else:
    print 'error choice'


def showmenu():
  prompt='''
(n)ew user login
(e)xisting user login
(q)uit
(l)ogin
(m)anage
(a)dmin

enter choice: '''
  done=False
  while not done:
    chosen=False
    while not chosen:
      try:
        choice=raw_input(prompt).strip()[0].lower()
      except (EOFError,KeyboardInterrupt):
        choice='q'
      print '\nyou picked: [%s]\n' % choice
      if choice not in 'lneqma':
        print 'invalid option,try again'
      else:
        chosen=True
    if choice=='q':done=True
    if choice=='n':newuser()
    if choice=='e':olduser()
    if choice=='m':manage()
    if choice=='l':new_login()
    if choice=='a':admin()


if __name__=='__main__':
  showmenu()
