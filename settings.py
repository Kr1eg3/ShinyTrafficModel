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

