#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''一个反应键到分数映射的字典'''
from bisect import bisect_left,insort_left
import UserDict
class Ratings(UserDict.DictMinxin,dict):
  """Ratings类很像一个字典，但是有一些额外的特性：每个键
     的对应值都是该键的分数，所有键根据他们的分数排名，
     对应值必须是可比较的，同样，键必须是可哈希的
     所有关于映射的行为都和预期一直
     >>> r=Ratings({'bob':30,'john':30})
     >>> len(r)
     2
     >>> r.has_key('paul'),'paul' in r
     (False,False)
     >>> r["john"] = 20
     >>> r.update({"paul": 20, "tom": 10})
     >>> len(r)
     4
     >>> r.has_key("paul"), "paul" in r
     (True, True)
     >>> [r[key] for key in ["bob", "paul", "john", "tom"]]
     [30, 20, 20, 10]
     >>> r.get("nobody"), r.get("nobody", 0)
     (None, 0)
     
     除了映射接口，还提供了排名的相关方法
     r.rating(key)返回了某个键的排名，其中排名为0的是
     最低的分数（）4如果键的分数相同，则直接比较，较小的键
     排名更低。
     >>> [r.rating(key) for key in ["bob", "paul", "john", "tom"]]
     [3, 2, 1, 0]
     
     
     getValueByRating(ranking) 和 getKeyByRating(ranking) 
     对于给定的排名索引分别返回分数和键
     >>> [r.getValueByRating(rating) for rating in range(4)]
     [10, 20, 20, 30]
     >>> [r.getKeyByRating(rating) for rating in range(4)]
     ['tom', 'john', 'paul', 'bob']
     
     一个重要的特性是keys()返回的键是以排名升序排列的
     而其他所有返回的相关的列表或迭代器都遵循这个顺序
     >>> r.keys( )
     ['tom', 'john', 'paul', 'bob']
     >>> [key for key in r]
     ['tom', 'john', 'paul', 'bob']
     >>> [key for key in r.iterkeys( )]
     ['tom', 'john', 'paul', 'bob']
     >>> r.values( )
     [10, 20, 20, 30]
     >>> [value for value in r.itervalues( )]
     [10, 20, 20, 30]
     >>> r.items( )
     [('tom', 10), ('john', 20), ('paul', 20), ('bob', 30)]
     >>> [item for item in r.iteritems( )]
     [('tom', 10), ('john', 20), ('paul', 20), ('bob', 30)]
     
     实例可以被修改（添加，改变，删除键-分数的对应关系）
     而且实例的每个方法都反映了实例的当前状态：
     >>> r["tom"] = 100
     >>> r.items( )
     [('john', 20), ('paul', 20), ('bob', 30), ('tom', 100)]
     >>> del r["paul"]
     >>> r.items( )
     [('john', 20), ('bob', 30), ('tom', 100)]
     >>> r["paul"] = 25
     >>> r.items( )
     [('john', 20), ('paul', 25), ('bob', 30), ('tom', 100)]
     >>> r.clear( )
     >>> r.items( )
     [ ]
     """
  '''这个实现混合了继承和托管，因此在尽量减少代码冗余
     的前提下获得了不错的性能，当然也保证了语义的正确，
     所有未被实现的方法通过继承来获得，大多来自于DictMinxin，
     关键的__getitem__来自于dict'''
  def __init__(self,*args,**kwds):
    '''这个类像dict一样被实例化'''
    dict.__init__(self,*args,**kwds)
    # self._rating是关键的辅助数据结构，一个所有（键，值）
    # 的列表，并保有自然的排序状态
    self._rating=[(v,k) for k,v in dict.iteritems(self)]
    self._rating.sort()
  def copy(self):
    '''提供一个完全相同但是独立的拷贝'''
    return Ratings(self)
  def __setitem__(self,k,v):
    '''除了把主要的任务委托给dict，还维护self._rating'''
    if k in self:
      del self._rating[self.rating(k)]
    dict.__setitem__(self,k,v)
    insort_left(self._rating,(v,k))
  def __delitem__(self,k):
    del self._rating[self.rating(k)]
    dict.__delitem__(self,k)
  '''显式的将某些方法委托给dict的对应方法，以免继承了
     DictMinxin的较慢的方法'''
  __len__=dict.__len__
  __contains__=dict.__contains__
  has_key=__contains__
  def __iter__(self):
    for v,k in self._rating:
      yield k
  iterkeys=__iter__
  def keys(self):
    return list(self)
  '''三个排名相关算法'''
  def rating(self,key):
    item=self[key],key
    i=bisect_left(self._rating,item)
    if item==self._rating[i]:
      return i
    raise LookupError,'item not found in rating'
  def getValueByRating(self,rating):
    return self._rating[rating][0]
  def getKeyByRating(self,rating):
    return self._rating[rating][1]

def _test():
  import doctest,rating
  doctest.testmod(rating)

if __name__=='__main__':
  _test()
