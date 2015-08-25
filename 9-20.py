import gzip
import shutil

fin=open('test.txt','rb')
fout=gzip.open('file.txt.gzip','wb')
shutil.copyfileobj(fin,fout)
fin.close()
fout.close()



f=gzip.open('file.txt.gzip','rb')
filecontent=f.read()
print filecontent
f.close()
