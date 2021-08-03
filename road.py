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

                             
    def get_road_info(self):
        road_info = {'road length': self.road_length,
                     'number of lines': self.numb_of_lines,
                     'number of cars': self.numb_of_cars}
        return road_info



        
