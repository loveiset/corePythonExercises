from random import randint

def createFile(ichr,count,totalLength):
  positions=[]
  new=[]

  i=1
  while i<=count:
    tempPosition=randint(0,totalLength)
    if tempPosition not in positions:
      positions.append(tempPosition)
      i+=1

  for j in range(totalLength):
    if j in positions:
      new.append(ichr)
    else:
      while True:
        temp=randint(0,256)
        if temp!=chr:
          new.append(temp)
          break
  return new

if __name__=='__main__':
  a=int(raw_input('enter a char(0-255): '))
  b=int(raw_input('enter count: '))
  c=int(raw_input('enterl length: '))

  chrs=createFile(a,b,c)
  f=open('binary.txt','wb')
  for i in chrs:
    f.write(bin(i)[2:].zfill(8))
  f.close()
    
