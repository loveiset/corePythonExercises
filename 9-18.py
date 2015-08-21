def countNum(fileObject,char):
  origin=[]
  while True:
    temp=fileObject.read(8)
    if temp=='':
      break
    else:
      origin.append(int(temp,2))

  print 'total length:',len(origin) 
  count=0
  for i in origin:
    if i==char:
      count +=1
  return count

if __name__=='__main__':
  filename=raw_input('enter a filename: ')
  char=int(raw_input('enter a char: ').strip())
  f=open(filename,'rb')
  print countNum(f,char)
  f.close()
