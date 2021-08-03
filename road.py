#!/usr/bin/python3

import numpy as np



class Road(object):

    def __init__(self, road_length, numb_of_lines, numb_of_cars):
        self.road_length = road_length
        self.numb_of_lines = numb_of_lines
        self.numb_of_cars = numb_of_cars


    def generate_road(self):
        road = np.random.randint(2, size=(self.numb_of_lines, 
            self.road_length))
        
        return road

                             
        
