'''
1.input原理
    函数input() 让程序暂停运行， 等待用户输入一些文本
    获取用户输入后， Python将其存储在一个变量中

2.input 接收到的值为字符串类型,如果接收到数字的话,需要
  强转转换为数字类型

3.while condition:

4.可使用break跳出整个循环,可使用continue跳出本次循环

5.使用while 循环来处理列表和字典


'''

#demo1  在列表之间移动元素
'''
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user)

print('\nThe following users h=have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
'''

#demo2  删除包含特定值的所有列表元素
'''
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)
'''


#demo3  
'''
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat's your name?")
    response = input("Which montain would you \
                       like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another \
                    person respond?(yes/no)")

    if repeat == 'no':
        polling_active = False

print("\n---Poll Result---")
for name,response in responses.items():
    print(name+" Would like to climb "+response+".")
'''
#practice8
'''
sandwich_oreders = ['pork','sausage','beef','chicken']
finsished_sandwichs = []
for sandwich in sandwich_oreders:
    print("I make you tuna sandwich")
    finsished_sandwichs.append(sandwich)

for sandwich in finsished_sandwichs:
    print(sandwich,end=" ")
'''

#practice9
'''
sandwich_oreders = ['pastrami','pork','pastrami','sausage','pastrami','beef','chicken']
print("pastrami are sold out")
while 'pastrami' in sandwich_oreders: 
    sandwich_oreders.remove("pastrami")

for sandwich in sandwich_oreders:
    print(sandwich,end=" ")
'''

#practice10
'''
investigation = {}

poll_active = True

while poll_active:
    name = input("What is your name?")
    place = input("Hello "+name+",If you could \
                                  visit one \
                                  place in the world, \
                                  where would you go \
                                  ")    
    investigation[name] = place

    respon = input("Do you want other friend join this \
                    investigation?(yes/no)")
    if respon == 'no':
        poll_active = False

print(investigation)

'''










