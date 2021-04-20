#  字符串 字符串本身不能修改

##str1 = 'hello world'

##str1.replace('h','3')   替换，将h替换成3 但是不修改原字符串，只是新生成一个字符串
##str1.replace('l','3',1)  默认符合条件会全部替换，第三个参数表示替换几个
##str1.upper()  大写
##str1.lower()   小写
##str1.capitalize()  首字母大写
##str1.title()  标题形式，每一个单词的首字母大写

##str1.strip()   去掉两边的空格
##str1.lstrip()   去掉左边的空格
##str1.rstrip()   去掉右边的空格
##str2 = 'hello world this is python'
##str2.split() 字符串切割，默认以空格作为切割符，切完之后的数据存在列表中
##str2.split('o') 指定以o当做切割符
##str2.split('o',2) 指定以o当做切割符  第二个参数限定切割次数
##'*'.join(str2.split('o')) 指定以o当做切割符，并用*将字符串再拼接回来
##'he'.join(str2.split('this'))  join拼接，返回字符串
##str2.index('h')  查找，根据元素名称查找对应元素位置
##str2.index('o',5) 第二个参数表示下标5的位置开始查找元素
##index() 如果没有找到元素，则会报错

##str2.find('o',5) 第二个参数表示下标5的位置开始查找元素
##如果没找到元素，则返回-1

##判断字符串是不是全是字母活中文
##'hello world'.isalpha()  False 空格是字符，但不是字母

##判断全是数字
##'1234a'.isdigit()  False

##判断全是小写
##'idsdfkdfPPHHEE'.islower()

##判断全是大写
##'idsdfkdfPPHHEE'.isupper()


##字符串转义 只在print() 函数里面起作用
## \n 代表换行
##print('hello\nworld')
## \t水平制表符，表示八个字符八个字符实现对齐
##print('hello\tworld')
## \b 相当于退格键，也就是往前退一个 
##print('hello\bworld')  cmd中效果-->hellworld

## \a 系统提示音

## \0产生一个空格
##print('hello\0world')

## \  取消字符串的转义
##print('hello\\nworld')

## r  统一取消转义,表示路径时非常方便
##print(r'\nab\')acd\0e\t')


##  字符串的编码 以什么形式编码，就要以什么形式解码
## encode() 编码 默认以utf-8形式编码
## decode() 解码 默认以utf-8形式解码
##str1 = '毛丽莎肉酱'
##str2 = str1.encode(encoding='utf-8')
##str2 = str1.encode('utf-8')
##str2 = str1.encode() #b'\xe6\xaf\x9b\xe4\xb8\xbd\xe8\x8e\x8e\xe8\x82\x89\xe9\x85\xb1'
##str3 = str2.decode() # '毛丽莎肉酱'

## 列表，元组，字符串 序列类型，可以通过下标取值
## 字典 dict 散列类型 无序 只能通过键取值
##  定义一个字典 {}
##  键和值之间用'：'连接，不同的数据之间用'，'隔开
##dic = {'name':'毛丽莎肉酱','age':18,'city':'shanghai'}
##dic['key'] 通过键去值

## 字段的定义
##dic1 = {}   # 空字典
##dic2 = {'a':1,'b':2}  # 常规定义
##dic3 =dict(a=1,b=2,c=2) # 使用dict函数定义字典   

## 字典的增删改查


## 增
##dic = {'name':'毛丽莎肉酱','age':18,'city':'上海'}
##dic.setdefault(key,value)   添加一个键值对 ，无则增，有则查

## 查
## dic[key] 根据键取值，但是如果不存在的键，会报错
## dic.get(key) 根据键取值，如果不存在，则返回空 None

## 改
##  dic['name'] = '毛肉肉'
## dic[key] = value  无则增，有则改
## dic.update(key:value,key:value)  批量增加，无则增，有则改


## 删
## dic.pop(key)   删除对应键的键值对数据
## dic.popitem()  根据添加顺序进行删除，后添加，先删除
## dic.clear()  清空字典所有数据


## 其他方法
## dic.keys()  获取字典里面所有的键名
## dic.values()  获取字典里面所有的值
## dic.items()  获取字典里面所有的键值对，键值对放在元组当中


## 集合 集合会自动去重里面的值具有唯一性
##set1 = {23,4,3,2,1,3}


##集合是无序  散列类型  每次查询结果都不一样
##set1 = {2,'a',3,'b',4,3,2,1,3}

## 集合的运算
##set1 = {1,2,3,4,5,7}
##set2 = {1,3,5,7}
##set3 = {'a','b'}

##交集 两个集合中相同的元素
##print(set1 & set2)   --> {1,3,5,7}

## 并集  |  两个集合的元素合并在一起
##print(set1 | set2 | set3)   


## 差集 前面的集合减去后面的集合
##print(set1 - set2 | set3)   

##增
## set1.add('a') 往集合中增加一个数据
##set1.update({11,22,33})  #批量增加 


##删
##set1.pop()  随机删除
##set1.remove(key)  指定元素名称删除对应元素

##集合是不能进行修改操作的 ，因为集合是无序的

##set1 = {1,2,3}
##set2 = {4,5,6}
##set3 = {3,4,5}

##set1.isdisjoint(set2)  判断两个集合之间是否没有交集，没有交集返回True
##set1.issubset(set2) 判断1是否包含在2集合之间，没有包含返回False 括号中可以运算
##set1.issuperset(set2)  判断前面的集合是否包含后面的集合


##  运算符总结

##身份运算符   is  is not
## a==b  True
##因为在python里存在内存池 范围在 [-5,256]
##范围内的内存地址一致，范围外的内存地址不一致
## a is b False  is 是身份运算符，判断两者是否是同一个对象
##  is not    取反

##  成员运算符 in  not in
##  不管是序列类型还是散列类型都能使用成员运算符，数值类型不行
##  in  判断元素是否属于对象里面的内容
##  not in 取反
##  li = [1,2,3,4]
##  1 in  li  6 not in li

##  通过内存地址判断可变不可变
##  如果修改过后内存地址不变，就是可变对象，反之是不可变对象。
##  可变对象： list,dict,set
##  不可变对象：数值，str，元组

##import random
##random.choices(str1,k=8)
##''.join(random.choices(str1,k=8))
##纯数字，11位，以1开头









