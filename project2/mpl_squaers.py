'''
1.plt.plot()函数尝试根据这些数字绘制出有意义的图形
    plot(list)

2.plt.show()打开matplotlib查看器,并显示绘制的图形

3.参数linewidth决定了plot()绘制的线条的粗细
  plt.title() 指定标题

4.xlabel()和ylabel()能够为每条轴设置标题

5.函数tick_params()设置刻度的样式
    plt.tick_params(axis='both', labelsize=14)
    axis='both'代表x、y轴都要设置


6.散点图
  

'''
#demo1
'''
import matplotlib.pyplot as plt


squares = [0,1,4,9,16,25]
plt.plot(squares,linewidth=5)

plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=24)
plt.ylabel("Squares of Value",fontsize=14)

plt.tick_params(axis='both',labelsize=14)

plt.show()
'''


#demo2
'''
import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth = 5)
plt.show()
'''
#demo3
'''
import matplotlib.pyplot as plt
plt.scatter(2,4,s=200)
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

plt.tick_params(axis="both",which="major",labelsize=14)

plt.show()

'''
#demo4
'''
import matplotlib.pyplot as plt
x_values = [1,2,3,4,5]
y_values = [1,4,9,16,25]
plt.scatter(x_values,y_values,s=100)
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)

plt.tick_params(axis="both",which="major",labelsize=14)

plt.show()
'''
#demo5
'''
import matplotlib.pyplot as plt
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,s=40)
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
plt.scatter(x_values,y_values,c=(0,0,0.1),edgecolor='none',s=40)
plt.tick_params(axis="both",which="major",labelsize=14)
plt.axis([0,1100,0,1100000])
plt.show()
'''

#demo6
'''
import matplotlib.pyplot as plt
x_values = list(range(1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues, \
            edgecolor='none',s=40)
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
plt.tick_params(axis="both",which="major",labelsize=14)
plt.axis([0,1100,0,1100000])
#plt.show()
plt.savefig("squares_plot.png",bbox_inches='tight')

'''

#demo7
'''
import matplotlib.pyplot as plt
from random import choice


class Randomwalk():
    def __init__(self,num_points=50000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values)<self.num_points:
            x_direction = choice([1,-1]) 
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1]) 
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            if x_step == 0 and y_step ==0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

while True:  
    rw = Randomwalk()
    rw.fill_walk()
    plt.figure(dpi=128,figsize=(10,6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=15)


#  plt.axes().get_xaxis().set_visible(False)
#  plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break
'''

#demo8
'''
import pygal
from random import randint

class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1,self.num_sides)

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#print(results)
frequencies = []
for value in range(1,die.num_sides+1):
    freqency = results.count(value)
    frequencies.append(freqency)

#print(frequencies)
hist = pygal.Bar()
hist.title = "Result of rolling one D6 1000 times"
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
'''

#demo9

import pygal
from random import randint

class Die():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1,self.num_sides)

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(2,max_results+1):
    freqency = results.count(value)
    frequencies.append(freqency)

hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')





#practice1
'''
import matplotlib.pyplot as plt
numbers = [0,1,2,3,4]
cubes = [number**3 for number in numbers]
plt.scatter(numbers,cubes)
plt.show()


import matplotlib.pyplot as plt
x_values = range(0,5001)
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,cmap=plt.cm.Blues, \
            edgecolor='none',s=40)
plt.axis([0,5000,0,25000000])
plt.show()
'''

