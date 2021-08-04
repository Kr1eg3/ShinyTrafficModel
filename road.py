#!/usr/bin/python3

#Code written by 
#       _          _   __
#  ___ | |_  _ __ / | / _|  ___
# / __|| __|| '__|| || |_  / _ \
# \__ \| |_ | |   | ||  _||  __/
# |___/ \__||_|   |_||_|   \___|
#


import numpy as np
from random import random


class Road(object):
    """
    A class that creates a matrix-road for the cellular automaton

    ...

    Attributes
    ----------
    road_length : int
        the length of the road, and the number of columns in the matrix
    numb_of_lines : int 
        the number of lines at the road, as well as the number of matrix lines
    numb_of_cars : int
        the number of cars on the road, and the number of one's in the matrix

    Methods
    -------
    generate_road(args):
        Description
    get_road_info(args)
        Descriptionn

    """
    def __init__(self, road_length, numb_of_lines, numb_of_cars):
        self.road_length = road_length
        self.numb_of_lines = numb_of_lines
        self.numb_of_cars = numb_of_cars
        self.__rng = np.random.default_rng()

    @property
    def generate_road(self):
        road = np.zeros(self.road_length*self.numb_of_lines)
        road[:self.numb_of_cars] = 1
        np.random.shuffle(road)
        road = road.reshape(self.numb_of_lines, self.road_length)

        return road

                             
    def get_road_info(self):
        road_info = {'road length': self.road_length,
                     'number of lines': self.numb_of_lines,
                     'number of cars': self.numb_of_cars}

        return road_info



        
