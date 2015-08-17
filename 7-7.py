def reverseDict(iDict):
  aDict={}
  for i in iDict:
    aDict[iDict[i]]=i
  return aDict

if __name__=='__main__':
  iDict={'abc':1,'cdd':2}
  print reverseDict(iDict)
