#作业1:列表排序
li=[(1,5,7,3),(2,6,3,1),(7,2,1,3),(3,7,2,1)]
print('排序前数组                   ',li)
result=sorted(li, key=lambda x: (x[1]))
print('根据第二个元素排序后',result)
#作业2:isPrime() 函数判断是否是质数

def  isPrime(n):
     if str(n).isdigit()==False:
          return False
     elif n == 1 or n ==0:
          return False
     elif n == 2:
          return True
     else:
##从2开始一直遍历到传入的数值都不能整除，则为质数
          for i in range(2,n):
               if n%i==0:
                    return False
          return True
               
#作业3:递归函数，实现一个阶乘函数，支持正数和负数的阶乘
def func(n):
     if n==0:
          return 1
     elif n<0 :
          return func(n+1)*n
     else:
          return func(n-1)*n
#作业4:
def strSort():
     str1=list(input('请输入一个字符串：'))
     if sorted(str1)==str1:
          return 'up' 
     elif sorted(str1,reverse=True)==str1:
          return 'down'
     else:
          return 'false'






     
