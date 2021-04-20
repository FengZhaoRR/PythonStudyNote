##day6 --- 函数

##函数的定义和调用
##while True:
##     phone = input('请输入一个手机号：')
##     if phone.isdigit()   adn len(phone)==1:
##          print('这是一个正确的手机号')
##     else:
##          print('这不是一个手机号')


##dir(__builtins__) 查看python 内置函数
##自定义函数  函数就是自定义一段代码
##def 是定义函数的关键字
##isPhone是函数名（自定义）
##括号里的phone是参数
##函数调用：函数名（参数值）
##def isPhone(phone):
##     if phone.isdigit()   adn len(phone)==1:
##          print('这是一个正确的手机号')
##     else:
##          print('这不是一个手机号')


##返回值 return
##当不存在返回值的时候，默认返回None
##当存在返回值的时候，返回具体的数据
##返回值后面的代码不会执行，相当于结束本次函数
##def func(x,y):
##     print(x)
##     print(y)
##     return x+y
##res = func(1,2)   # res得到返回出去的结果(x,y)


##func函数名，代表函数体，也就是函数本身
##func(1,2)  代表函数调用，type返回的结果是函数执行之后的结果

##函数的参数
##顺序：先必备，再默认，最后不定长
##1.必备参数(x)，定义了几个必备参数，函数调用就需要传几个参数值，一个也不能多，一个也不能少
##2.默认参数(y)，当不给默认参数传值的时候，会把默认值给默认参数接收，当传值是我们传进去的时候
##3.不定长参数(*args,**kwargs)
##args是不定长参数，数据放在元组里
##kwargs也是不定长参数，数据放在字典里，必须以键值对的形式，键只能是字符串类型，其他会报错
##args和kwargs都不是规定写法，但是是规范写法
##def func(x,y=2,*args,**kwargs):
##     print(x)
##     print(y)
##     print(args)
##     print(kwargs)
##     





##-> str这种语法指明这个函数的返回值是什么数据类型
##def func(x,y=2,*args,**kwargs)  -> str:
##     print(x)
##     print(y)
##     print(args)
##     print(kwargs)
##     return 'abc'


##拆包
##def func(x,y=2,*args,**kwargs):
##     print(x)
##     print(y)
##     print(args)
##     print(kwargs)
##   



##函数的作用域
##x=100  #全局变量
##def func():
##     #在函数里面对外部定义的x进行修改
##     y=200  #局部变量
##     x=x+1
##     print(x)

##x=100
##def func():
##     global x #声明全局变量
##     x=200
##     print(x)
##
##print(x)   #100
##func()     #200
##print(x)   #100



##def func1():
##     x = 100
##     def func2():
##          nolocal x # 声明局部变量
##          x=x+1
##          print(x)
##          return func2()



##闭包
##def func():
##     lv = 5
##     #增加血量
##     def func1():
##          nonlocal lv 
##          lv +=1
##          print(lv)
##     #减少血量
##     def func2():
##          nonlocal lv
##          lv -= 1
##          print(lv)
##     # 外层函数返回内层函数的函数体，就是闭包
##     return func1


##递归函数
##def func(n):
##     if n==1:
##          return 1
##     else:
##          return func(n-1)*n

##匿名函数
##通过lambda 关键字定义
##匿名函数会自动返回，所以可以通过变量去接收
##a = lambda x:x+1
##上面的匿名函数相当于下面的有名函数
##def a(x):
##     return x+1


##li = [2,4,6,8,10]
##def func(x):
##     if x>5:
##          return x
### filter:过滤器
####第一个参数是函数体，第二个参数是可迭代对象
##print(list(filter(func,li)))

##print(list(filter(lambda x:x>5,li)))

##map()   对于元素进行统一操作
## 第一个参数是函数体，后面可以是一个或者多个可迭代对象
##print(list(map(lambda x:x-1,li)))

##zip(key,value)  把两个可迭代对象合成一个字典，实现数据配对
##tu =('a','b','c')
##li = [2,4,6]
##print(dict(zip(tu,li)))



##回调函数  ： 把一个函数的函数体当做参数传递给另外的一个函数去使用
##def func1(f):
##     f()
##     print(111)
##def func2():
##     print(222)
##
##func1(func2)

li=[(1,5,7,3),(3,7,2,1),(2,6,3,1),(7,2,1,3)]
li.sort()
sort(key=每个元组的第二个元素)
##












