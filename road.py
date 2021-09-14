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
from vehicle import Vehicle, Car
from pprint import pprint


class Road:
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
    def __init__(self, road_length, numb_of_lanes, numb_of_vehicles, n_iters):
        self.road_length = road_length
        self.numb_of_lanes = numb_of_lanes
        self.numb_of_vehicles = numb_of_vehicles
        self.n_iters = n_iters
        self.__rng = np.random.default_rng()

        self.created = False

    def _get_vehicles_id(self, list_of_vehicles):
        __ids = []
        for v in list_of_vehicles:
            __ids.append(v.id)
        print(__ids)

    def _get_vehicles_pos(self, list_of_vehicles):
        __poss = []
        for v in list_of_vehicles:
            __poss.append((v.posx, v.posy))
        print(__poss)

    def _generate_road(self):
        __road = np.zeros(self.road_length * self.numb_of_lanes)
        __road[:self.numb_of_vehicles] = 1
        np.random.shuffle(__road)
        __road = __road.reshape(self.numb_of_lanes, self.road_length)

        return __road

    def _show_id_matrix(self, list_of_vehicles, i=1):
        id_matrix = np.zeros((self.numb_of_lanes, self.road_length))
        for v in list_of_vehicles:
            if v.posx >= self.road_length:
                j = (v.posx - self.road_length) % 10
                id_matrix[v.posy][j] = v.id
            else:
                id_matrix[v.posy][v.posx] = v.id
                
        print(id_matrix)

    def _divide_road(self, list_of_vehicles):
        # Создать переменную с числом
        # TODO
        __lane1 = []
        __lane2 = []
        __all_lanes = []

        for v in list_of_vehicles:
            if v.posy == 0:
                __lane1.append(v)
            else:
                __lane2.append(v)
        __all_lanes.append(__lane1)
        __all_lanes.append(__lane2)

        return __all_lanes

    def _sort_roads(self, list_of_lanes):
        for lane in list_of_lanes:
            lane.sort(key=lambda x: x.posx, reverse=False)

    def create_vehicles(self):
        if not self.created:
            road_matrix = self._generate_road()
            vehicles = []
            for index, value in np.ndenumerate(road_matrix):
                if value == 1:
                    c = Car(posx=index[1], posy=index[0], initial_speed=3, road_length=self.road_length)
                    vehicles.append(c)
                    del c
        self.created = True

        return vehicles

    def get_road_info(self):
        road_info = {'road length': self.road_length,
                     'number of lanes': self.numb_of_lines,
                     'number of vehicles': self.numb_of_vehicles}

        return road_info

    def evaluate_road(self, show_speed=True, show_matrices=True):
        # Create list with vehicles 
        vehicles = self.create_vehicles()

        # Show id matrix
        if show_matrices == True:
            print('____________initial matrix________________')
            self._show_id_matrix(vehicles)
            print('____________iteration = 0_________________')

        # Main loop
        for i in range(self.n_iters):
            all_lanes = self._divide_road(vehicles)
            self._sort_roads(all_lanes)
         
            for vehicle in vehicles:
                vehicle.get_neighbors(all_lanes)
            
            for vehicle in vehicles:
                vehicle.get_si_neighbor()

            for vehicle in vehicles:
                vehicle.get_new_speed(self.road_length, show_speed)

            for vehicle in vehicles:
                vehicle.move(self.road_length)

            if show_matrices == True:
                self._show_id_matrix(vehicles, i)
                print('____________iteration =', i+1,'_________________')

        print('End of calculations!')

r = Road(road_length=10, numb_of_lanes=2, numb_of_vehicles=8, n_iters=100)   

# Start processing
r.evaluate_road(show_speed=True, show_matrices=True)

