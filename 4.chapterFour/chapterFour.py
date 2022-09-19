'''
列表的  遍历
for in        Traversal using for...in statements
'''



'''
创建数值列表
声明列表而并不赋值
list = []

1.range(x,y) == x,x+1...,y-1

2.使用range() 创建数字列表 
  list(range(1,6)) = [1,2,3,4,5]

3.对数据列表进行简单的统计计算
    min(list) max(list) sum(list)

'''



'''
列表解析
1.squares = [value**2 for value in range(1,11)] 此处for没有冒号
  squares = [1,4,9,16,25,36,49,64,81,100]
'''

'''
使用列表的一部分
切片
list[x:y] x,x+1,...,y-1    x从0开始
'''

'''
复制列表
list1 = list2[:] 
'''

'''
元组        
tuple = (x,y,...) 

调用 tuple[i] = x      无法修改

修改元组
tuple = (x,y,...)
tuple = (a,b,...)      可以修改

如果需要存储的一组值在程序的整个生命周期内都不变， 
可使用元组。
'''















#practice3
'''
for i in range(1,21):
    print(i,end = " ")
print()
'''
#practice4
'''
num = [value for value in range(1,1000001)]
for value in num:
    print(value,end=" ")
'''
#practice5
'''
num = [value for value in range(1,1000001)]
print(max(num))
print(min(num))
print(sum(num))
'''

#practice6
'''
odd = [value for value in range(1,20,2)]
print(odd)

for value in odd:
    print(value,end=" ")
'''

#practice7
'''
value = range(3,20,3)
for i in value:
    print(i,end = " ")
'''

#practice8
'''
cube = []
for value in range(1,11):
    cube.append(value**2) 
for value in cube:
    print(value,end=" ")
'''

#practice9
'''
cube = [value**2 for value in range(1,11)]
for i in cube:
    print(i,end=" ")
'''













