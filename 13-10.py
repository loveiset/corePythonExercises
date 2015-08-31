class StackAndQueue(object):

  def __init__(self,size=20):
    self.__sequence=[]
    self.size=size
    self.__index=-1

  def isEmpty(self):
    if len(self.__sequence)<=0:
      return True
    else:
      return False

  def shift(self):
    if self.isEmpty():
      return False
    else:
      self.__index-=1
      return self.__sequence.pop(0)

  def unshift(self,element):
    if self.__index>=self.size-1:
      return False
    else:
      self.__sequence.insert(0,element)
      self.__index+=1
      return True

  def push(self,element):
    if self.__index>=self.size-1:
      return False
    else:
      self.__sequence.append(element)
      self.__index+=1
      return True

  def pop(self):
    if self.isEmpty():
      return False
    else:
      self.__index-=1
      return self.__sequence.pop()
