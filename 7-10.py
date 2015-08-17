def rot13(istr):
  new=''
  for i in istr:
    if 65<=ord(i)<=77 or 97<=ord(i)<=109:
      new+=chr(ord(i)+13)
    elif 78<=ord(i)<=90 or 110<=ord(i)<=122:
      new+=chr(ord(i)-13)
    else:
      new+=i
  return new

if __name__=='__main__':
  istr=raw_input('string you want to enc: ')
  print 'enc: %s' % rot13(istr)
  print 'orignal: %s' % rot13(rot13(istr))
