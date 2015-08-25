import os
folder='/home/layasa'
files=filter(lambda x:x and x[0]!='.',os.listdir(folder))
files2=os.listdir(folder)
print ' '.join(files)
print ' '.join(files2)
