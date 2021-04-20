print('作业1')
date = 20181221
print (str((date // 10000))+'年'+str((date % 10000 // 100))+'月'+str((date % 100))+'日')

print('作业2')
str1  = 'こんにちは'
str2  = '私は 肉 です'
str3  = 'はじめまして'
print(','.join((str1,str2,str3)))
str4 = '昨夜の授業は'
str5 = '安言先生は'
str6 = 'お疲れ様です'
print ('{0},{1}{2}'.format(str4,str5,str6))
str7 = 'これから'
str8 = '私はPythonを勉強します、頑張ります'
str9 = 'よろしくお願いします'
print(f'{str7}、{str8}、{str9}~')

print('作业3')
import math
r = 4
π= math.pi
C = math.floor(2*π*r)
S = math.floor(π*r**2)
print('圆周长 = '+str(C))
print('圆面积 = '+str(S))









