list =[i for i in range(1,10)]
list.extend(j for j in ([1,4,6,7,8]))
print(list)
result = []
for k in list:
     if result.count(k)==0:
          result.append(k)
print(result)
     
