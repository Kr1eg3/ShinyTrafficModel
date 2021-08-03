#!/usr/bin/python3

#Program created by str1fe
#Traffic model - S-NFS

from car import Car
from road import Road
from random import randint
import settings



#vars in settings.py
numb_of_cars = 10
numb_of_lines = 2
road_length = 10

if __name__ == "__main__":
    #print(baner)

    road_exmpl = Road(road_length, numb_of_lines, numb_of_cars)
    road = road_exmpl.generate_road()
    print(road)
    cars = []
    for i in range(numb_of_cars):
        cars.append(Car((i+10, randint(0,1)), 2))
        print(cars[i].car_id, cars[i].on_lane)
    

    cars[1].find_neighbors(cars)
    
    print('test cars created!')



