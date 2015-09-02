class CapOpen(object):

  def __init__(self,fn,mode='r',buf=-1):
    self.file=open(fn,mode,buf)

  def __str__(self):
    return str(self.file)

  def __repr__(self):
    return `self.file`

  def write(file,line):
    self.file.write(line.upper())

  def __getattr__(self,attr):
    return getattr(self.file,attr)

  def get(self):
    return self.file

  def writelines(file,lines,isNewLine=False):
    for eachLine in lines:
      self.file.write(eachLine)
      if isNewLine:
        self.file.write('\n')

