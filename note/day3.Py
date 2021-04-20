#day3  笔记

# for 循环  计数循环
# i是代表接收到的字符串遍历(循环)出来的每一个元素
# 'python'  是可迭代对象
# 循环的次数由可迭代对象的长度决定
##for i in  'python':
##     print(i)

# range()  左闭右开  只能传入整数
# range(结束值)  默认从0开始 左闭右开
# range(开始值,结束值)  一样的左闭右开 结束值不取
# range(开始值,结束值,步长)
##for i in range(5,10,6):
##     print(i)


# 查看是否是可迭代对象的方法  dir(对象)  有‘_iter_’就是可迭代对象

#for循环也能够和else混合使用
# continue  跳出本次循环，继续下次循环
##for i in range(20):
##     if i==10:
##          continue
##     print(i)
##else:
##     print('循环结束')
##

# 列表推导式
# 列表 list
##list = [] # 定义空列表
##for i in range(10):
##     list.append(i)  #append()  追加
##print(list)
##list = [i for i in range(10) if i%2==0]   # 列表推导式
##print(list)

# 列表推导式和三目运算混合使用
##list = [i*100  if i%2==0  else i*10 for i in range(10)]
##print(list)

# len()查看长度
# 列表
# 索引（下标）取值  list[索引值]
# 索引值从0开始
# 负索引从列表尾部开始往前数，负索引从-1开始
##list=[0,10,200,30,400,50,600,70,800,90]


# 切片 左闭右开 步长正负数是方向
#  list[索引开始值:索引结束值]
#  list[索引开始值:索引结束值:步长]
# 当从左往右切的时候，步长为正数   
# 当从右往左切的时候，步长为负数
# 切片超出范围的话，就取到最后一个值   list[2:20]
# 切片右边不写范围的时候，默认切到最后一个  list[2:]
# 切片左右都不写范围的时候，从头切到尾  list[:]


# 列表的增删改查
list =[i for i in 'abcdefg']


# 查
# list.index()  根据元素查找对应元素的索引值（下标）

# 增
# list.append()  追加，加载列表最后面
# list.insert(2,333) 在下标2的位置，添加333的数据  Insert 方法是将数据添加到指定位置
# list.extend(['q','w','e'])/list.extend('qwe')  批量添加，加在列表最后，里面的数据会自动遍历

# 删除
#  list.pop() 默认删除最后一个元素
#  list.pop(下标值)  根据下标删除元素
#  list.remove(元素名称) 根据元素名称删除元素
#  del list[1:3]  批量删除元素  切片 左闭右开
#  list.clear()  清空列表


# 改  赋值语句
#  list[0] ='aa'  替换单个元素
#  list[0:3]  ='bbb'  可迭代对象会自动遍历 替换的数量不需要一致
#  list[0:3]=['aaa','bbb','ccc']


#  列表的其他方法
#  copy()  复制列表
#  id()   查看id指向，能够通过id指向判断是否为同一个对象
#  list.sort()  列表排序  会改变原列表  同类型才能排序
#  list.reverse() 反向， 将列表顺序颠倒一下
#  list.sort(reverse=True)  反向排序
#  count() 统计元素出现的次数
#  sorted(list)  临时排序 不改变原列表
#  sorted(list,reverse=True)   临时反向排序


#  元组  tuple  不可以改变
#  元组可以索引取值 也能切片
#  元组不能替换元素
#  元组支持index()  根据元素查找对应元素索引
#  元组支持count()  统计元素出现的次数
#  元组支持sorted()方法 可以临时排序，返回的是列表不是元组
#  tu = (1,)  元组只有一个元素，也要加上逗号，否则就是本身的数据类型



#  元组拆包
#  a,b,*c =  tu   按顺序接受元组的元素值，
#  多余的给带*的变量接收，并放在列表里面，带*的是不定长参数
#  *号只能给一个变量，也就是只能存在一个不定长参数






















     











     
