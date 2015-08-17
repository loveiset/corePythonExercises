def tr(srcstr,dststr,string,tag=False):
  if tag:
    stringLower=string.lower()
    srcstrLower=srcstr.lower()
    lens=len(srcstr)
    index=stringLower.find(srcstrLower)
    retval=''
    while index >= 0:
      retval+=string[:index]+dststr
      stringLower=stringLower[index+lens:]
      string=string[index+lens:]
      index=stringLower.find(srcstrLower)
    retval+=string
    return retval
  else:
    a=string.split(srcstr)
    return dststr.join(a)

if __name__=='__main__':
  print tr('abc','mno','abcdef')
  print tr('Abc','mno','abcdef',True)
  print tr('Abc','123','3ABC34aBC3444daabc000',True)

