#!/usr/bin/python3

from art import *
import numpy as np


number_of_cars = 10
length_of_the_road = 30
number_of_lines = 2



# input array
x = np.array([[ 1., 2., 3.], [ 4., 5., 6.], [ 7., 8., 9.]])

# random boolean mask for which values will be changed
mask = np.random.randint(2, size=x.shape).astype(np.bool)

# random matrix the same shape of your data
r = np.random.rand(*x.shape)*np.max(x)

# use your mask to replace values in your input array
x[mask] = r[mask]


RL = 5
L = 2
N = 3

A = np.zeros(RL*L)

A[:N] = 1



class Testcar(object):
    next_id = 1

    def __init__(self, pos):
        self.pos = pos
        self.id = Testcar.next_id
        Testcar.next_id += 1

testcars = []
for i in range(10):
    testcars.append(Testcar(np.array([i+10, 1])))
    print(testcars[i].pos)

print(testcars)
print('____________________')
cars15 = [car for car in testcars if getattr(car,
    'pos')[0] > 15 and getattr(car, 'pos')[1] != 2]
print('____________________')
for car in cars15:
    print(car.pos)


min_car = min(cars15, key=lambda x: x.pos[0])
print(min_car.pos, min_car.id)

#a = [car for car in testcars if getattr(car, 'id') == 4]
#print(*a)



#from operator import attrgetter
#a = min(cars15, key=attrgetter('pos'))
#print('object =', a.pos[0])





