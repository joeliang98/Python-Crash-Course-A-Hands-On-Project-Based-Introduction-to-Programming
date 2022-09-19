'''
1.打开文件
  with open("FileName.xxx") as file:
    
  关键字with 在不再需要访问文件后将其关闭

2.逐行读取
    with open(filename) as file_object:
        lines = file_object.readlines()

3.写入文件
    with open(filename, 'w') as file_object
    调用open()时提供了两个实参
        第一个实参也是要打开的文件的名称
        第二个实参('w') 告诉Python,
            我们要以写入模式 打开这个文件

    打开文件时,可指定-读取模式('r')、
                    -写入模式('w')、
                    -附加模式('a')
    或让你能够读取和写入文件的模式('r+')
    如果你省略了模式实参， 
    Python将以默认的只读模式打开文件

    写入('w')模式打开文件时千万要小心,
    因为如果指定的文件已经存在,
    Python将在返回文件对象前清空该文件

4.异常
    Python使用被称为异常的特殊对象
    来管理程序执行期间发生的错误.
    每当发生让Python不知所措的错误时,
    它都会创建一个异常对象。

    如果你编写了处理该异常的代码,
    程序将继续运行;如果你未对异常进行处理
    程序将停止,并显示一个traceback,
    其中包含有关异常的报告

    ZeroDivisionError 异常
    FileNotFoundError 异常

    try:
    
    except except_name:

    else:

    pass语句,什么都不做直接跳过

5.存储数据
    保存用户提供的信息
    简单的方式是使用模块json来存储数据
    块json让你能够将简单的Python数据结构转储到文件中
    并在程序再次运行时加载该文件中的数据
    你还可以使用json在Python程序之间分享数据

    json.dump()存储

    json.load()读取    

6.重构
    代码能够正确地运行，
    但可做进一步的改进——将代码划分为一系列
    完成具体工作的函数，这样的过程被称为重构 


'''

#demo1
'''
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())
'''

#demo2
'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
'''

#demo3
'''
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string+=line.rstrip()

print(pi_string)
print(len(pi_string))
pi = float(pi_string)
print(pi)
'''

#demo4
'''
filename = "pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string[:100]+'...')
print(len(pi_string))
'''

#demo5
'''
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birth = input("Please input your birthday:")
if birth in pi_string:
    print("Yep")
else:
    print("nope")
'''
#demo6
'''
filename = 'programing.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming")
'''

#demo7
'''
filename = 'programming.txt'

with open(filename,'w') as file_object:
    file_object.write("I love programing \n")
    file_object.write("I love creating new games \n")
'''

#demo8
'''
filename = 'programming.txt'

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets. \n")
    file_object.write("I love creating apps that can run in a browser.\n")
'''

#demo9
'''
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")
'''

#demo10
'''
print("Give me two numbers,and I'll divide them")
print("Enter q to quit")

while True:
    first_num = input("\n First number:")
    if first_num == 'q':
        break
    second_num = input("\n second number:")
    if second_num == 'q':
        break

    try:
        anwer = int(first_num)/int(second_num)
    except ZeroDivisionError:
        print("you can't divide by 0")
    else:
        print(anwer)
'''

#demo11
'''
filename = "alice.txt"
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry,the file "+filename+" does not exist."
    print(msg)
'''

#demo12
'''
def count_words(filename):    
    try:
        with open(filename,encoding='utf-8') as f_obj:
            contents = f_obj.read()

    except FileNotFoundError:
        msg = "Sorry,the file "+filename+" does not exist."
        print(msg)
    else:
        words = contents.split()
        num = len(words)
        print("The file " + filename + " has about " + str(num) + " words.")
filenames = ["alice.txt", \
            "siddhartha.txt", \
            "moby_dick.txt", \
            "The Woman and the Car.txt"
            ]


for filename in filenames:
    count_words(filename)
'''
#demo13
'''
import json

numbers = [2,3,5,7,11,13]

filename = "numbers.json"
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)
'''

#demo14
'''
import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)
'''

#demo15
'''
import json

username = input("what is your name?")

filename = "username.json"
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remeber you when you come back,"+username+"!")
'''

#demo16
'''
import json

filename = 'username.json'
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("welcome back, "+username+"!")
'''



#practice1
'''
filename = 'practice_1.txt'
with open(filename) as file_object:
    all_string = file_object.read()
with open(filename) as file_object:
    for one in file_object:
        print(one.rstrip())

with open(filename) as file_object:
    lines_string = file_object.readlines()
print(all_string)
for line in lines_string:
    print(line.rstrip())
'''

#practice2
'''
filename = 'practice_1.txt'
with open(filename) as file_object:
    all_string = file_object.read()
all_string = all_string.replace('Python','C')
print(all_string)
'''

#practice3
'''
filename = "practice3.txt"
name = input("please input your name:")
with open(filename,'a') as file_object:
    file_object.write(name+"\n") 
'''


#pracice4
'''
filename = 'practice4.txt'
rolling_actice = True
with open(filename,'a') as file_object:
    while rolling_actice:

        name = input("please input your name(input q to quit):")
        if name == 'q':
            rolling_actice = False
        print("welcome "+name+'!')
        file_object.write(name+'\n')
'''        

#practice5
'''
print("please input two numbers:")
first = input("first number:")
second = input("second number:")
try:
    first_int = int(first)
    second_int = int(second)
except ValueError:
    print("please input number")
else:
    print("Two number add equal "+str(first_int+second_int))
'''

#practice6
'''
add_active = True
while add_active:
    print("please input two numbers,input q to quit")
    first = input("first number:")
    if first == 'q':
        break
    second = input("second number:")
    if second == 'q':
        break
    try:
        first_int = int(first)
        second_int = int(second)
    except ValueError:
        print("please input number")
    else:
        print("Two number add equal "+str(first_int+second_int))
'''

#practice8
'''
filename_dogs = "dogs.txt"
filename_cats = "cats.txt"
dogs_name = ''
cats_name = ''
try:    
    with open(filename_dogs) as dogs_object:
        dogs_name = dogs_object.read()
except FileNotFoundError:
    print(filename_dogs+" file not exist!")
else:
    print("dogs name:"+dogs_name+"\n")

try:
    with open(filename_cats) as cats_object:
        cats_name = cats_object.read()
except FileNotFoundError:
    print(filename_cats+" file not exist!")
else:
    print("cats name:"+cats_name)
'''
#practice9
'''
filename_dogs = "dogs.txt"
filename_cats = "cats.txt"
dogs_name = ''
cats_name = ''
try:    
    with open(filename_dogs) as dogs_object:
        dogs_name = dogs_object.read()
except FileNotFoundError:
    pass
else:
    print("dogs name:"+dogs_name+"\n")

try:
    with open(filename_cats) as cats_object:
        cats_name = cats_object.read()
except FileNotFoundError:
    pass
else:
    print("cats name:"+cats_name)
'''

#practice10
'''
with open("alice.txt") as file_object:
    contents = file_object.read()
    print(contents.lower().count("row"))
'''
#practice11
'''
import json
filename = "practice11.json"
number = input("Please input a number:")
with open(filename,'w') as f_obj:
    json.dump(number,f_obj)


import json
filename = "practice11.json"
with open(filename) as f_obj:
    num = json.load(f_obj)
    print("I know your favourite number! It's is "+num)
'''











