#深浅复制  只在嵌套列表当中存在
#  copy() 浅复制
##li = [1,2,3,[4,5,6]]
##li1= li.copy()


#深复制
import copy
li = [1,2,3,[4,5,6]]
print(li)
li1 = copy.deepcopy(li)
print(li1)
