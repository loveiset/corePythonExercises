class Queue(object):

  def __init__(self,size=20):
    self.__queue=[]
    self.size=size
    self.__index=-1

  def isEmpty(self):
    if len(self.__queue)<=0:
      return True
    else:
      return False

  def enqueue(self,element):
    if self.__index>=self.size-1:
      return False
    else:
      self.__queue.append(element)
      self.__index+=1
      return True

  def dequeue(self):
    if self.isEmpty():
      return False
    else:
      self.__index-=1
      return self.__queue.pop(0)

if __name__=='__main__':
  a=Queue(3)
  a.enqueue(1)
  a.enqueue(2)
  a.enqueue(3)
  print a.dequeue()
  print a.dequeue()
  print a.dequeue()
  print a.dequeue()
