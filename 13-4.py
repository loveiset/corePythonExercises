import shelve
from time import ctime,time

class UserData(object):
  
  def __init__(self):
    self.db=shelve.open('userData')

  def __del__(self):
    self.db.close()

  def md5(self,str):
    import hashlib
    m = hashlib.md5()   
    m.update(str)
    return m.hexdigest()

  def manage(self):
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
        if user not in self.db.keys():
          print 'user not exists'
        else:
          del self.db[user]
          print '%s deleted' % user
      elif choice=='s':
        for key in self.db:
          print 'username=%s,password=%s' % (key,self.db[key][0])
      else:
        done=True

  def new_login(self):
    import re
    while True:
      user=raw_input('enter username: ').lower()
      if not re.match('^[0-9a-z]+$',user):
        print 'user wrong format'
      else:
        break
  
    password=raw_input('enter password: ')
    if self.db.has_key(user):
      passwd=self.db.get(user)[0]
      if passwd==self.md5(password):
        tempTime=time()
        if tempTime-self.db.get(user)[1]<60*4:
          print 'you already logged in at:',ctime(self.db.get(user)[1])
        else:
          self.db.[user]=[self.db[user][0],time()]
          print 'welcom back',user
          print 'you last logined in at',ctime(self.db.get(user)[1])
      else:
        print 'login incorrect'
    else:
      confirm=raw_input('user not exists, create it y/n? ').strip()[0].lower()
      if confirm=='y':
        self.db[user]=[self.md5(password),time()]
      else:
        print 'you cancled the create'

  def admin(self):
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
      for i in self.db.keys():
        f.write('%s:%s:%s\n' % (i,self.db[i][0],ctime(self.db[i][1])))
      f.close()
    elif a=='n':
      print 'you canceled'
    else:
      print 'error choice' 

  def updatePassword(self):
    print 'you must login to modify the infomation'
    while True:
      user=raw_input('enter username: ').strip()
      if self.db.has_key(user):
        passwd=raw_input('enter password: ').strip()
        if self.md5(passwd)==self.db[user][0]:
          print 'correct'
          newpass=raw_input('enter new password: ').strip()
          print self.db[user][0]
          self.db[user]=[self.md5(newpass),self.db[user][1]]
          print self.md5(newpass)
          print self.db[user][0]
        else:
          print 'wrong password'
        break
      else:
        choice=raw_input('user not exists,q to quit,c to continue: ').strip()[0].lower()
        if choice=='q':
          break

  def showmenu(self):
    prompt='''
(n)ew user login
(e)xisting user login
(q)uit
(l)ogin
(m)anage
(a)dmin
(u)pdate password
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
        if choice not in 'lneqmau':
          print 'invalid option,try again'
        else:
          chosen=True
      if choice=='q':done=True
      if choice=='n':self.newuser()
      if choice=='e':self.olduser()
      if choice=='m':self.manage()
      if choice=='l':self.new_login()
      if choice=='a':self.admin()
      if choice=='u':self.updatePassword()




if __name__=='__main__':
  a=UserData()
  a.showmenu()
