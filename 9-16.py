def shorter(fileObject):
  new=[]
  fileAll=fileObject.readlines()
  for i in range(len(fileAll)):
    if len(fileAll[i])<=80:
      new.append(fileAll[i])
    else:
      temp=fileAll[i][:80]
      words=temp.split(' ')
      newLine=' '.join(words[:len(words)-1])
      nextLine=temp[len(newLine):]
      new.append(newLine)
      if i == len(fileAll)-1:
        
def shorterLine(istr):
  

