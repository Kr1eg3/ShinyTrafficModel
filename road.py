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
            print(road_matrix)
            vehicles = []
            for index, value in np.ndenumerate(road_matrix):
                if value == 1:
                    c = Car(posx=index[1], posy=index[0], initial_speed=0)
                    vehicles.append(c)
                    del c
        self.created = True

        return vehicles

                             
    def get_road_info(self):
        road_info = {'road length': self.road_length,
                     'number of lanes': self.numb_of_lines,
                     'number of vehicles': self.numb_of_vehicles}

        return road_info


    def evaluate_road(self):
        # Create list with vehicles 
        vehicles = self.create_vehicles()

        # Main loop
        for i in range(self.n_iters):
            all_lanes = self._divide_road(vehicles)
            self._get_vehicles_pos(all_lanes[0])
            self._get_vehicles_pos(all_lanes[1])

            self._sort_roads(all_lanes)
            self._get_vehicles_pos(all_lanes[0])
            self._get_vehicles_pos(all_lanes[1])            

            for vehicle in vehicles:
                vehicle.get_neighbors(all_lanes)
                
            for vehicle in vehicles:
                vehicle.get_new_speed()
                vehicle.move()

        self._get_vehicles_id(vehicles)
        self._get_vehicles_pos(vehicles)



r = Road(road_length=10, numb_of_lanes=2, numb_of_vehicles=5, n_iters=1)   
r.evaluate_road()

