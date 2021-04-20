##  面向对象

##面向对象介绍

##name = ' MRR'
##age = 18
##sex = 'F'
##def do():
##     print(f'{name}会敲代码')

##class 关键字用来定义类
##类的命名：以驼峰命名法进行命名
## 类里面的变量叫做类的属性，通过名词去表示属性
## 类里面的函数叫做类的方法，通过动词去表示方法
##class  Person:
####     相当于一个模板
##     name = 'ZPP'
##     age= 18
##     sex = 'M'
##     def eat():
##          print('干饭')
##
##MRR =  Person()  # 实例化一个对象

##类定义和使用
##class  Person:
####     相当于一个模板
####     name = 'ZPP'
####     age= 18
####     sex = 'M'
##     #__init__是初始化方法，在实例化时会自动调用
##     #self 代表实例本身
##     def __init__(self,name,age,sex):
##          self.name = name
##          self.age = age
##          self.sex=sex
####          通过del关键字用来删除实例对象
####          __del__表示析构函数，当删除实例时，就会自动调用此方法
##     def __del__(self):
##          print(f'{self.name}被析构了')
##               
##     def eat(self):
##          print('干饭')

class  Person:
     def __init__(self,name,age,sex):
          self.name = name
          self.age = age
          self.sex=sex
     def __del__(self):
          print(f'{self.name}被析构了')
               
     def eat(self):
          print(f'{self.name}干饭')

# 括号里的类，表示继承的是哪个类
# 继承Person类之后，就拥有Person类里面所有的属性和方法
# 重用： 子类重新定义父类的方法，让同一种方法，具有不同的行为
##class SiChuan(Person):
##     def play(self):
##          print('四川人爱打麻将')
##          
##     def eat(self):
####方法一,不推荐
##          Person.eat(self)
##          print(f'{self.name}爱吃火锅')
##
##class GuangDong(Person):
##     def play(self):
##          print('广东人爱吃')
##     def eat(self):
##          #方法二，推荐
##          #super()表示使用父类的方法
##          super().eat()
##          print(f'{self.name}爱吃肠粉')

#多继承，就近继承
##class SiChuan(Person):
##     def play(self):
##          print('四川人爱打麻将')
##          
##     def eat(self):
##          Person.eat(self)
##          print(f'{self.name}爱吃火锅')
##
##class GuangDong(Person):
##     def play(self):
##          print('广东人爱吃')
##     def eat(self):
##          super().eat()
##          print(f'{self.name}爱吃肠粉')
##
##class HunXue(SiChuan,GuangDong):
##     #pass代表类里没有任何属性和方法 只是把结构写完整
##     pass
####
####HunXue.__base__  查看类继承的第一个类
####HunXue.__bases__查看类继承的所有类
####HunXue.mro()  查看类继承的继承顺序
##
##class  Base:
##     def eat(self):
##          print('base')
 




























