class Stack(object):

  def __init__(self,size=20):
    self.__stack=[]
    self.size=size
    self.__index=-1

  def push(self,element):
    if self.__index>=self.size-1:
      raise IndexError,'data overflow'
      return
    self.__index+=1
    self.__stack.append(element)

  def isEmpty(self):
    if len(self.__stack)<=0:
      return True
    else:
      return False

  def peek(self):
    if self.isEmpty():
      return False
    else:
      return self.__stack[self.__index]

  def pop(self):
    if self.isEmpty():
      return None
    else:
      if 'pop' in  dir(self.__stack):
        self.__index-=1
        return self.__stack.pop()
      else:
        retval=self.__stack[self.__index]
        del self.__stack[self.__index]
        self.__index-=1
        return retval

if __name__=='__main__':
  a=Stack(5)
  a.push(1)
  print a.peek()
  a.push(2)
  print a.peek()
  a.push(3)
  print a.peek()
  a.push(5)
  print a.peek()
  a.push(6)
  print a.peek()
  print a.pop()
  print a.pop()
  print a.pop()
  print a.pop()
  print a.pop()
  print a.pop()
  print a.pop()
  print a.pop()


  
      
