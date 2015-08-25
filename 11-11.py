import os.path
def clean(fileobject):
  return map(lambda x:x.strip()+'\n',fileobject)

a=raw_input('enter a filename: ').strip()
if os.path.exists(a):
  choice=raw_input('enter choice(r to replace and n to new file): ').strip()[0]
  if choice in 'rn':
    if choice=='r':
      f1=open(a,'r')
      filelines=f1.readlines()
      f1.close()
      f1=open(a,'w')
      f1.writelines(clean(filelines))
      f1.close()
    else:
      filename=raw_input('enter new filename: ').strip()
      f1=open(a,'r')
      filelines=f1.readlines()
      f2=open(filename,'w')
      f2.writelines(clean(filelines))
      f1.close()
      f2.close()
else:
  print 'file not exists'
