print('作业1: 九九乘法表')
a = 1
while a<10:
     b=1
     while  b<=a :
          print(a,'*',b,'=',a*b,end=' ')
          b +=1
     a +=1
     print('''
''')
     continue

print('作业2:猜数字小游戏')
count=1
import random
num = random.randint(1,100)
while count<=10:
     guess_num = input('10次机会猜个1~100随机数，输入你猜的数字：')
     if int(guess_num)==num:
          print('猜对咯,你赢啦')
          break
     elif int(guess_num) < num:
          print('比正确的值小')
          count +=1
          continue
     else :
          print('比正确的值大')
          count +=1
          continue
print('游戏结束')
     
     
     


     
     
     
