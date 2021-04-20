##作业1.找出两个列表中相同元素，并打印出来
list1 =[1,2,3,4]
print('列表1为:',list1)
list2 =[2,4,6,8]
print('列表2为:',list2)
set1 = set(list1)
set2 = set(list2)
list3=list((set1 & set2))
print('两个列表中相同元素为:',list3)


##作业2.统计一串字符中，每个字母 a~z的出现次数，忽略大小写
str1 = 'QWEasdRTFSQseresldfsg'
print(str1)
str2 = str1.lower()
print(str2)
dic1 = {}
for j in str2:
     dic1[j]=str2.count(j)
print(dic1)

##作业3.利用26个字母和10个数字，随机生成10个8位密码
password='abcdefghijklmnopqrstuvwxyz0123456789'
import random
for j in range(10):
     random.choices(password,k=8)
     print('随机密码',j+1,':',''.join(random.choices(password,k=8)))

     
##作业4.判断用户输入的是不是一个手机号码
phonenumber = input('请输手机号码：')
list=[i for i in phonenumber]
j=1
while j>0:
     if phonenumber.isdigit() and list[0]=='1' and len(phonenumber)==11: 
          print('输入的手机号码正确')
          break
     else:
          phonenumber = input('号码有误，请输入正确的手机号：')
          j +=1
          
     



     
