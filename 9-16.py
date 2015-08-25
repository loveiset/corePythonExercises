def shorter(fileObject):
  new=[]
  fileAll=fileObject.readlines()
  for i in range(len(fileAll)):
    print '---',i
    if len(fileAll[i].strip())<=80:
      new.append(fileAll[i]+'\n')
    else:
      if i==len(fileAll)-1:
        temp=fileAll[i].strip()
        if len(temp)>80:
          while len(temp)>80:
            newline,nextline=shorterLine(temp.strip())
            new.append(newline.strip()+'\n')
            temp=nextline.strip()
          new.append(temp)
        else:
          new.append(temp.strip())
      else:
        newline,nextline=shorterLine(fileAll[i].strip())
        new.append(newline+'\n')
        fileAll[i+1]=nextline+' '+fileAll[i+1]
  return new
def shorterLine(istr):
  temp=istr[:82]
  words=temp.split(' ')
  newLine=' '.join(words[:len(words)-2])
  nextLine=istr[len(newLine):]
  return newLine,nextLine

if __name__=='__main__':
  f=open('test.txt','rw+')
  n=open('new.txt','w')
  n.writelines(shorter(f))
  f.close()
  n.close()
