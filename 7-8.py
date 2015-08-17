def showName(idict):
  for k,v in sorted(idict.items()):
    print k,v

def showNum(idict):
  for k,v in sorted(idict.items(),key=lambda x:x[1]):
    print k,v

if __name__=='__main__':
  db={}
  while True:
    userid=int(raw_input('enter id(0 to exit): ').strip())
    if userid==0:
      break
    if userid in db.keys():
      print 'userid already exists'
    else:
      name=raw_input('enter name: ')
      db[userid]=name
  showName(db)
  showNum(db)


