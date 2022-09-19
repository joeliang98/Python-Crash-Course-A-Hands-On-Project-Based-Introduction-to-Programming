'''
1.函数的定义
    def 函数定义    冒号:结尾
    xxxx    文档字符串 (docstring) 的注释， 
            描述了函数是做什么的
            文档字符串用三引号括起
            Python使用它们来生成有关程序中函数的文档
2.函数参数
    位置实参    关键字实参

3.函数的默认值
    编写函数时， 可给每个形参指定默认值

4.让实参变成可选的
    可选参数默认值为空字符串,再用if来判断来完成相应操作

5.传递列表
    def function(list)
        for value in list:

6.禁止函数修改参数
    可向函数传递列表的副本而不是原件
    这样函数所做的任何修改都只影响副本
    而丝毫不影响原件
   
    切片表示法[:] 创建列表的副本

7.结合使用位置实参和任意数量实参

  如果要让函数接受不同类型的实参,
  必须在函数定义中将接纳任意数量
             实参的形参放在最后


  Python先匹配位置实参和关键字实参,
  再将余下的实参都收集到最后一个形参中

8.使用任意数量的关键字实参  demo7
  需要接受任意数量的实参
  可将函数编写成能够接受任意数量的键值对
  类似于关键字实参,而又不同于关键字实参

9.跨文件引用函数
    import file_name
    file_name.function()
    只需编写一条import 语句并在其中指定
    模块名,就可在程序中使用该模块中的所有函数
    书中的表示方法:
            module_name.function_name()

  其他方法
    一、你还可以导入模块中的特定函数，
        这种导入方法的语法如下：
    from module_name import function_name

    通过用逗号分隔函数名,
    可根据需要从模块中导入任意数量的函数：
    from module_name import function_0, function_1, function_2

    二、使用as 给函数指定别名
    如果要导入的函数的名称可能与程序中现有的名称冲突
    或者函数的名称太长
    可指定简短而独一无二的别名
    函数的另一个名称， 类似于外号。 
    要给函数指定这种特殊外号,
    需要在导入它时这样做
    from file_name import name as other_name

    三、导入模块中的所有函数
    使用星号(*)运算符可让Python导入模块中的所有函数:
    from module_name import *
    
'''

#demo1
'''
def greet_user():
    print("Hello")

greet_user()
'''

#demo2
'''
def greet_user(username):
    print("Hello "+username.title()+".")

greet_user("joe")
'''
#demo3
'''
def describe_pet(animal_type,pet_name):
    print("\n I have a "+animal_type+".")
    print("My "+animal_type+"\s name is "+pet_name.title() \
           +'.')

describe_pet('hamster',"harry")
describe_pet(animal_type='dog',pet_name='tom')
'''

#demo4
'''
def build_person(first_name,last_name,age=""):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

musician = build_person("jimi",'hendrix',23)
print(musician)
'''

#demo5
'''
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: "+current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
'''
#demo6
'''
def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+ \
    " inch pizza with the following topping:")
    for topping in toppings:
        print("- "+topping)

make_pizza(16,"pepperoni")
make_pizza(12,"mushrooms","green pepers", \
    "extra cheese")
'''
#demo7
'''
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', \
    'einstein',location='princeton',
    field = 'physics')
print(user_profile)
'''

#demo8
'''
import making_pizza
making_pizza.make_pizza(16,"peperoni")
making_pizza.make_pizza(14,"mushroom","peperoni")
'''






#practice6
'''
from typing import ChainMap

cityCountry = {}
def city_country(city_name,country_name):
    cityCountry[city_name] = country_name
    return cityCountry

cityCountry = city_country("dalian","China")
cityCountry = city_country("harbin","China")
cityCountry = city_country("shenyang","China")
print(cityCountry)
'''
#practice7
'''
def make_album(name,album,num=""):
    album_dict = {}
    album_dict[name] = album
    if num:
        album_dict['num'] = num
    return album_dict

album1 = make_album('zhoujielun','aizaixiyuanqian',5)
print(album1)
album2 = make_album('wanglihong','huatiancuo')
print(album2)
album3 = make_album('wuyifan','dawankuanmian',2)
print(album3)
'''

#practice8
'''
album_dict = {}
def make_album(name,album,num=""):
    album_dict = {}
    album_dict[name] = album
    if num:
        album_dict['num'] = num
    return album_dict

album_final = {}
roll_active = True
while roll_active:
    name = input("please input name:")
    album = input("please input album:")
    num = input("please input num::(input q to quit)")
    if num == 'q':
        roll_active = False
    album_dict = make_album(name,album,num)
      
print(album_final)
'''    

#practice9
'''
def show_magicians(magic_name):
    for name in magic_name:
        print(name,end = ' ')


def make_great(magic_name):
    magicname=[]
    for name in magic_name:
        name = 'The Great '+name
        magicname.append(name)     
    return magicname   

magic_name = ['a','b','c','d']
show_magicians(magic_name)
print("\n")
magicname = make_great(magic_name)
show_magicians(magicname)
'''

#practice12
'''
def add_food(*Toppings):
    for topping in Toppings:
        print("Your topping is "+topping)

add_food("vagetable","mushroom","melon")
'''


#practice13
'''
def build_profile(first,last,**user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('joe', \
    'liang',location='harbin',
    field = 'computer science',
    school = 'NEFU')
print(user_profile)
'''

#practice14
'''
def make_car(name,model,**others):
    car = {}
    car['name'] = name
    car['model'] = model
    for key,value in others.items():
        car[key] = value
    return car
car = make_car('tesla','model y',location='America',boss = 'musk')
print(car)
'''


