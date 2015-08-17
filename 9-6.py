def fileCompare(a,b):
  try:
    fa=open(a,'r')
    fb=open(b,'r')
  except IOError:
    print 'file open error'

  i=0
  while True:
    i+=1
    linea=fa.readline()
    lineb=fb.readline()
    if linea and lineb:
      if linea==lineb:
        continue
      else:
        for j in range(len(linea)):
          if linea[j]!=lineb[j]:
            return (i,j+1)

    elif linea or lineb:
      return (i,1)
    else:
      return (0,0)

a=raw_input('enter file a: ')
b=raw_input('enter file b: ')

print fileCompare(a,b)
