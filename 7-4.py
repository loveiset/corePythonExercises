def combine(aList,bList):
  iDict={}
  if len(aList)!=len(bList):
    return  'error: length must the same'
  else:
    for i in range(len(aList)):
      iDict[aList[i]]=bList[i]
  return iDict

if __name__=='__main__':
  aList=['abc','def','agc']
  bList=[1,'ddd',2.3]
  print combine(aList,bList)
