'''
1.访问字典的值
dict[key]

2.添加键-值对
dict[key1] = value1
dict[key2] = value2

3.空字典
dict = {}

4.修改字典的值
dict[key] = new_value

5.遍历字典
for key,value in dict.items():

6.遍历字典的所有键
for key in dict.keys():
dict.keys()     返回一个列表,里面有所有的key
遍历字典时,会默认遍历所有的键
for key in dict.keys(): == for key in dict:

7.遍历字典中的所有值
for value in dict.values():
这种做法提取字典中所有的值， 而没有考虑是否重复.
涉及的值很少时,这也许不是问题.
但如果被调查者很多,最终的列表可能包含大量的重复项.
为剔除重复项,可使用集合(set). 
集合 类似于列表， 但每个元素都必须是独一无二的:

8.嵌套访问
for key,list in dict 
    for content in list 
        print(key+":"+content)



'''



#demo1
'''
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
print(alien_0['color'])
alien_0['color'] = 'yellow'
print(alien_0['color'])
'''

#demo2
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favourite language is "
     +favorite_languages['sarah'].title()+' .')
'''

#demo3
'''
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key,value in user_0.items():
    print("\nKey:"+key,end=' ')
    print("\nValue:"+value,end=' ')
'''

#demo4
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for key in favorite_languages.keys():
    print(key.title())
'''
#demo5
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for value in favorite_languages.values():
    print(value.title())
'''

#嵌套
#demo6  生成三个外星人
'''
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'green','points':5}
alien_2 = {'color':'green','points':5}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
'''

#demo7  使用代码自动生成30个外星人
'''
aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')

print('Total number of liens:'+str(len(aliens)))
'''

#demo8      外星人能力升级
'''
aliens = []
for alien_number in range(0,30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'    
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[0:5]:
    print(alien)
print('...')
'''

#demo9      字典中存储了列表
'''
pizza = {
    'crust':'thick',
    'toppings':['mushrooms','extra cheese']
}

print("Your order a "+ pizza['crust'] + "-crust pizza"+
     " with the following toppings:"
     )

for topping in pizza['toppings']:
    print("\t"+topping)
'''

#demo10     将字典中的列表输出
'''
favorite_languages = {
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}
for name,languages in favorite_languages.items():
    print("\n"+name.title()+"'s favorite languages are:")
    for language in languages:
        print("\t "+language.title())
'''

#demo11     在字典中存储字典
'''
users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
    },

    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}

for username,user_info in users.items():
    print("\nUsername: "+username)
    full_name = user_info['first'] + user_info['last']
    location = user_info['location']
    print("\tFull_name: "+full_name.title())
    print("\tlocation: "+location.title())
'''
#practice8
'''
pets = []
tom = {'type':'dog','master':'tomM'}
harry = {'type':'cat','master':'harryM'}
bob = {'type':'mouse','master':'bobM'}
lily = {'type':'fish','master':'lilyM'}
pets.append(tom)
pets.append(harry)
pets.append(bob)
pets.append(lily)

for pet in pets:
    print("pet: "+pet['type']+" \tmaster: "+" "+pet['master'])
'''
#practice9
'''
favorite_palces = {'joe':['Dortmund','shanghai','guangzhou','wuhan'],
                   'reus':['beijing','dalian'],
                   'trump':['white house','washington']
}

for name,places in favorite_palces.items():
    for place in places:
        print(name+' want to go '+place)
'''
