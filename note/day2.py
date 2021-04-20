# if 语句

##weather= 'sunny'
### if 判断语句 判断语句最后一定要加冒号
##if  weather =='rainy':
###缩进  一个Tab键或者四个空格  
##     print('在家学习')
### 否则
##else:
##    print('出去玩')
#  快捷注释  选中后 alt + 3 /快速取消注释  选中后 alt + 4


##weather = input('请输入今天的天气：')
##if weather =='sunny':
##     print('出去玩')
##elif weather=='cloudy':
##     print('出去吃东西')
##else:
##     print('在家学习')

###  三目运算
##a  = 6
####if  a>5:
####     print('比5大')
####else:
####     print('不比5大')
####     
##print('比5大' if a>5 else '不比5大')



#逻辑运算
# 1. and 并且，和  当and左右两边都为真(true) 时 ,才会返回真 
##num = 10
##if num>5 and num<15:
##     print('值在5~15之间')
##else:
##     print('值不在范围内')
##     



# 2. or 或者  只要两边其一为真 ，则返回真
##num = 10
##if num>5 or num<1:
##     print('值是正确的')
##else:
##     print('值不在范围内')




#3. not  取反 真变成假，假变成真

#三者之间的优先级 ： not>and>or
#一句语句中如果三个条件都有，三个都会计算一遍，不是只计算第一个
#代码执行顺序：从左到右，从上到下
#逻辑短路   or ,and 都存在逻辑短路  ，not 没有逻辑短路
#  1==1 or  a==2
#==>True  因为左边为真，那么右边的结果对于整体的结果没有影响，就不走右边代码

#连续判断
# ’1‘  > '2' > 3   -->   '1' > '2'   and  '2' >3   --> False  




# while 循环  三要素：初始值 、判断条件  、更新循环变量
# while 循环又叫做条件循环
# 当循环 “正常”结束时，就会执行else 里面的代码
##i = 1  #循环的初始值
##while i<=5:  #  循环的判断条件
##     if i == 3:
##          break #提前终止程序，跳出当前循环
##     print(i)     #执行的代码块
##     i +=1       # i= i+1  更新循环变量，不更新就会出现死循环
##else:
##     print('循环语句执行完毕了')


##i = 1  
##while i<=5:  
##     if i == 3:
##          continue  #跳出本次循环，继续下次循环
##     print(i)   
##     i +=1       
##else:
##     print('循环语句执行完毕了')

#快捷键  ctrl+] 统一往右缩进 ctrl+[ 统一往左缩进
#嵌套循环
#print()默认情况会换行，end='' 能够让print()不换行
##a = 1
##while a<5:
##     print('a:',a)
##     a +=1
##else:
##     print('循环结束')
##
##
## b=1
##     while b<10:
##     if b%5==0:
##     break
##     print('b:',b,end='')
##     b +=1
##a = 1
##while a<5:
##     b=1
##     while b<10:
##          if b%5==0:
##               break
##          print('b:',b,end=' ')
##          b +=1
##     print('a:',a)   
##     a +=1
##     
     

import random
a = random.randint(1,10)  # 在1~10之间取一个随机数，都是闭区间







