'''
1.创建类
    class class_name():
       def __init__(self,other)
  类中的函数称为方法
  
  __init__() 是一个特殊的方法， 每当你根
  据类创建新实例时， Python都会自动运行它
  
  形参self 必不可少， 还必须位于其他形参的前面

  以self 为前缀的变量都可供类中的所有方法使用
  我们还可以通过类的任何实例来访问这些变量。 
  self.name = name 获取存储在形参name 中的值

2.给属性指定默认值
  在方法__init__()内指定这种初始值是可行的
  __init__(a,b,c)

3.继承
    class father()

    class son(father):
        def __init__(self)
            super().__init__(从父类中继承的属性)
    super() 是一个特殊函数， 
    帮助Python将父类和子类关联起来
    父类也称为超类 (superclass)
    名称super因此而得名

4.重写父类的方法
  对于父类的方法,只要它不符合子类模拟的实物的行为,
  都可对其进行重写

  使用继承时,可让子类保留从父类那里继
  承而来的精华,并剔除不需要的糟粕














'''
# demo1
'''
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " is rooled over!")

my_dog = Dog("willie",6)
your_dog = Dog("lucy",3)

print("My dog name is "+ my_dog.name.title()+".")
print("My dog name is "+ str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

print("\nYour dog's name is "+your_dog.name+" .")
print("Your dog is "+str(your_dog.age)+" years old.")
'''
#practise1
'''
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print("restaurant_name:" + self.restaurant_name)
        print("cuisine_type:" + self.cuisine_type)

    def open_restaurant(self):
        print("The "+ self.restaurant_name +" restaurant is opening")

KFC = Restaurant("kfc","chicken")
Dicos = Restaurant("dicos","hamburger")

KFC.describe_restaurant()
Dicos.describe_restaurant()

KFC.open_restaurant()
Dicos.open_restaurant()
'''
#practise2
'''
class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("user name is " + self.first_name +" "+self.last_name )

    def greet_user(self):
        print(self.first_name +" "+self.last_name +" say hallo")

user = User("joe","liang")
user.describe_user()
user.greet_user()
'''


#demo2
'''
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' +self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileage):
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        self.odometer_reading += miles

my_new_car = Car("Audi","a4",2016)
print(my_new_car.get_descriptive_name())
#my_new_car.odometer_reading = 23 
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car("subaru","outback",2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

'''

#practice3
'''
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("restaurant_name:" + self.restaurant_name)
        print("cuisine_type:" + self.cuisine_type)
        print(self.number_served)

    def open_restaurant(self):
        print("The "+ self.restaurant_name +" restaurant is opening")

    def set_number_served(self,number_served):
        self.number_served = number_served
        print("number of served: " +str(self.number_served))

    def increment_number_served(self):
        self.number_served += 20

KFC = Restaurant("kfc","chicken")
Dicos = Restaurant("dicos","hamburger")

KFC.describe_restaurant()
Dicos.describe_restaurant()

KFC.open_restaurant()
Dicos.open_restaurant()

KFC.set_number_served(20)
KFC.describe_restaurant()
'''

#practice4
'''
class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("user name is " + self.first_name +" "+self.last_name )

    def greet_user(self):
        print(self.first_name +" "+self.last_name +" say hallo")

    def increment_login_atttempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("joe","liang")
user.describe_user()
user.greet_user()
print(user.login_attempts)
user.increment_login_atttempts()
print(user.login_attempts)
user.increment_login_atttempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
'''

#demo3
'''
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' +self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileage):
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("The car has filled")

class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a "+ str(self.battery_size) +" kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
    message = "This car can go approximately "+str(range)
    message += " miles on a full charge."
    print(message)

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla','model s',2016);
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
'''
#practice5
'''
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("restaurant_name:" + self.restaurant_name)
        print("cuisine_type:" + self.cuisine_type)
        print(self.number_served)

    def open_restaurant(self):
        print("The "+ self.restaurant_name +" restaurant is opening")

    def set_number_served(self,number_served):
        self.number_served = number_served
        print("number of served: " +str(self.number_served))

    def increment_number_served(self):
        self.number_served += 20

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cusine_type,favors):
        super().__init__(restaurant_name,cusine_type)
        self.favors = favors

    def decribe_favors(self):
        print("This IceCream favor is "+self.favors)

IceCream = IceCreamStand("miki","ice cream","grape")
IceCream.decribe_favors()
'''
#practice7
'''
class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("user name is " + self.first_name +" "+self.last_name )

    def greet_user(self):
        print(self.first_name +" "+self.last_name +" say hallo")

    def increment_login_atttempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges =["can add post","can delete post","can ban user"] 

    def show_privileges(self):
        for privilege in self.privileges:
            print("The priviveges is "+privilege+" .")

user = Admin("joe","liang")
user.show_privileges()
'''
#practice8
'''
class User:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print("user name is " + self.first_name +" "+self.last_name )

    def greet_user(self):
        print(self.first_name +" "+self.last_name +" say hallo")

    def increment_login_atttempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class privileges():
    def __init__(self):
        self.privileges = ["can add post","can delete post","can ban user"]
    def show_privileges(self):
        for privilege in self.privileges:
            print("The priviveges is "+privilege+" .")

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = privileges()

user = Admin("joe","liang")
user.privileges.show_privileges()
'''
#practice9
'''
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' +self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileage):
        self.odometer_reading = mileage

    def increment_odometer(self,miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("The car has filled")

class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a "+ str(self.battery_size) +" kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately "+str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla','model s',2016);
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
'''
#demo4
'''
#add demo4 can run my_car.py and my_cars.py and my_electric_car.py
class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an dodmeter!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles
class Battery():
    def __init__(self,battery_size=60):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")

    def get_range(self):
        range = 0
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
'''
#demo5
'''
from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = "python"
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title()+".")
'''

#practice10
from random import randint

class Die():
    def __init__(self,sides = 6):
        self.sides = sides

    def roll_die(self,roll_time):
        while roll_time > 0:
            x = randint(1,self.sides)
            print("The"+str(roll_time)+" time is "+str(x))
            roll_time -= 1

die = Die(20)
die.roll_die(100)






