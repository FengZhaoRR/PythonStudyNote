print('作业1-for循环写九九乘法表')
for i in range(1,10):
     print('''
''')
     for j in range(1,i+1):
          print(j,'*',i,'=',i*j,end=' ')

print(''''
''')

print('作业2- 移除重复元素')
list = [i for i in range(10)]
list.extend(j for j in range(10) if j%2==0)
print('原    数    组：',list)
result = []
for k in list:
     if result.count(k) ==0:
          result.append(k)
list.clear()
list=result.copy()
print('去重后数组：',list)

