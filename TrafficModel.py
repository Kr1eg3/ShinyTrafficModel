#!/usr/bin/python3

#Program created by str1fe
#Traffic model - S-NFS

from car import Car
from road import Road
from random import randint, random
import numpy as np



#vars in settings.py
numb_of_cars = 4
numb_of_lines = 2
road_length = 10

if __name__ == "__main__":

    road_exmpl = Road(road_length, numb_of_lines, numb_of_cars)
    road = road_exmpl.generate_road
    print(road)
    cars = []
    for index, value in np.ndenumerate(road):
        if value == 1:
            a = Car(np.asarray(index), 2)
            road[index[0]][index[1]] = a.car_id
            cars.append(a)
            del a
    
    
    #cars[1].find_neighbors(cars)
    
    print(np.shape(road))
    print(road)
    print(cars)

    print('test cars created!')


