#  day 9 面向对象高级

##class Person:
##     def __init__(self,name,age):
##          self.name = name
##          self.age = age

#hasattr(实例名，'属性名') 判断属性存不存在
#getattr(实例名，'属性名')  获取属性的属性值
#实例和实例之间不互通
#setattr(实例名，'属性名',)  无则增，有则改
#delattr(实例名，'属性名') 删除属性
##
##class Person:
##     def __init__(self,name,age):
##          self.name = name
##          self.age = age
##Mrr = Person('Mrr',18)

##if  hasattr(Mrr,'sex'):
##     a = getattr(Mrr,'sex')
##else:
##     setattr(Mrr,'sex','Female')
##
##a =  getattr(Mrr,'sex') if hasattr(Mrr,'sex') else setattr(Mrr,'sex','Female')

##class Shanghai(Person):
##     pass
##issubclass(Shanghai,Person)  判断前面的类是不是后面类的子类
##issubclass(Shanghai,object)
##isinstance(1,int) 判断前面的实例是不是属于后面实例出来的实例
##前面的参数是不是后面参数的类型
## type(1) == int 判断数据类型，只能判断单个



##属性调用过程
##重写底层方法，让当前不存在的属性不会报错
##class Person:
##     def __init__(self,name,age):
##          self.name = name
##          self.age = age
##          
###item 接受实例的属性
##     def __getattr__(self,item):
##          print(f'{item}该属性不存在')
          

##class Person:
##     def __init__(self,name,age):
##          print('调用初始化方法')
##          self.name = name
##          self.age = age
##     #__new__用来创建实例对象
##     # cls代表类本身
##     # Mr 就是创建出来的实例对象
##     def __new__(cls,*args,**kwargs):
##          print('调用实例对象')
##          Mr = super().__new__(cls)
##          return Mr
##
##Mrr =  Person('Mrr',18)
##          

## 单例模式  :类里面始终存在一个实例，不会同时出现多个实例
##class Person:
##     def __init__(self,name,age):
##          self.name = name
##          self.age = age
##     def __new__(cls,*args,**kwargs):
##          ##如果类里面没有_instance这个属性
##          if not hasattr(cls,'_instance'):
##               cls._instance = super().__new__(cls)
##          return cls._instance
##
##Mrr =  Person('Mrr',18)
##zpp =  Person('zpp',38)
##          

##输出魔法方法
##__str__ 是修改print打印时的样子
##__repr__是修改直接打印时的样子
##class Person:
##     def __init__(self,name,age):
##          self.name = name
##          self.age = age
##     def __str__(self):
##          return 'this is str'
##     def __repr__(self):
##          return 'this is repr'
##
##Mrr =  Person('Mrr',18)
##zpp =  Person('zpp',38)
##
##Mrr --> this is  repr
##print(Mrr) -- >this is str

##class Person:
##     def __init__(self,name,age):
##          self.name = name
##          self.age = age
##     #将实例对象变成可调用对象
##     def __call__(self,num):
##          num= num*10
##          print(num)


###  序列协议 ：__getitem__,__len__
##class IndexTuple:
##     def __init__(self,*args):
##          self.values = tuple([i for i in args])
##          # 通过枚举法获取下标值
##          # enumerate()函数可以将一个可遍历对象组合成一个索引序列
##          # 同事列出数据下标和数据值
##          self.index =  enumerate(self.values)
##      #长度方法，返回长度
##     def __len__(self):
##          return len(self.values)
##
##     def __getitem__(self,key):
##          return self.index[key][1]
##
##     def __repr__(self):
##          return str(self.values)
          

##迭代器协议:__iter__,__next__

##class Number:
##     def __init__(self,end=10):
##          self.start = 0
##          self.end = end
##     #通过__iter__方法把类对象变成可迭代对象
##     def __iter__(self):
##          return self
##     #通过__next__方法把可迭代对象变成迭代器
##     def __next__(self):
##          a = self.start
##          if self.start >=self.end:
##               raise StopIteration # 主动抛出异常
##          self.start +=1
##          return a
     

#上下文协议:__enter__,__exit__


import time
class RunTime:
     #只要with 语句一出现，enter方法就会被触发
     def __enter__(self):
          #time.time()返回当前时间的时间戳
          self.start_time=time.time()
     #当__enter__方法执行完毕就会执行__exit__方法
     #exc_type:异常类型
     #exc_val:异常值
     #exc_tb:追踪信息
     #只有当__enter__方法或者with下的代码块出现异常才会有值，
     #否则都为Null
     def __exit__(self,exc_type,exc_val,exc_tb):
          self.end_time = time.time()
          self.run_time = self.end_time - self.start_time
          print(f'运行时间为：{self.run_time}')


with RunTime():
     for i in range(10000000):
          pass
          
          
     
          












     
