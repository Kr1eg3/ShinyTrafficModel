#!/usr/bin/python3

#Code written by 
#       _          _   __
#  ___ | |_  _ __ / | / _|  ___
# / __|| __|| '__|| || |_  / _ \
# \__ \| |_ | |   | ||  _||  __/
# |___/ \__||_|   |_||_|   \___|
#


import numpy as np
from random import random, uniform


class Car(object):
    """
    A class to represent a car

    ...

    Attributes
    ----------
    position : np.ndarray
        car position at the moment
    initial_speed : int 
        the speed at which the car starts
    max_speed : int
        (oprional: default 2) 
        maximum possible speed of the car
    agent_type : str
        (optional: default 'cooperator')
        the type of character of the agent, two values are possible:
        'cooperator' - goood caaar
        'destructor' - baaaad carr

    Methods
    -------
    find_neighbors(cars_list):
        Description
    find_gap(args)
        Description
    get_car_speed(args)
        Description
    get_new_pos(args)
        Description
    get_car_info(args)
        Description
    take_a_step(args)
        Description

    """

    next_id = 1

    def __init__(self, position, initial_speed, max_speed=2,
            agent_type='cooperator'):
        self.position = position
        self.initial_speed = initial_speed
        self.car_id = Car.next_id
        self.braking_prob = .2
        self.max_speed = max_speed
        self.agent_type = agent_type
        self.speed = self.initial_speed
        self.turn_left = np.array([-1, 1])
        self.turn_right = np.array([1, 1])
        self.__previous_pos = 0
        self.__previous_spd = 0
        self.neighbors_dict = {}
        Car.next_id += 1

        ### model parameters ##
        self.G = 3
        self.q = .2
        self.r = .2
        self.P1 = .5
        self.P2 = .4
        self.P3 = .3
        self.P4 = .2
        #######################
        
    def __get_neighbors(self, cars_list, road_matrix):
        
        for index, value in np.ndenumerate(road_matrix):
            
            if value > 0 and != self.car_id:
                #find forward car id
                if index[0] == self.position[0] and index[1] > self.position[1]:

 
                #find behind car id
                if index[0] == self.position[0] and

                #find left/right side car id
                if index[0] != self.position[0] and index[1] == self.position[1]:
                    self.neighbors_dict['side neighbor id'] = value

                #find behind side car id
                if index[0] != self.position and  



         
        #forward_neighbor_id = 
        #side_f_neighbor_id = 
        #side_b_neighbor_id = 
        if len(cars_list) == 10:
            print('yee')

#all_frames = []
#
#for i in range(10):
#    img = np.random.randint(0, high=255, size=(720, 1280, 3), dtype=np.uint8) # generate a random, noisy image
#    all_frames.append(Frame(img, i))
#
#frames_to_plot = [frame for frame in all_frames if getattr(frame, index) == 5]


    def find_gap(self):
        gap = 1
        return gap


    def get_car_speed(self, cars_list, neib_list):

        self.__previous_spd = self.speed
        _next_car = car in cars_list if getattr(car, car_id) == neib_list['forward car id'] 
        

        #rule 1. Acceleration
        if gap >= self.G and self.speed <= _next_car.speed:
            car_speed = min(self.max_speed, self.speed + 1)

        #rule 2. Slow-to-start
        if uniform(0, 1) <= self.q:
            self.s = self.S if uniform(0, 1) <= self.r else 1
            car_speed = min(car_speed, 1)
        
        #rule 3. Perspective (Quick start)
        

        #rule 4. Random brake
        if uniform(0, 1) < 1 - self.braking_prob:
            car_speed = max(1, car_speed - 1)
    
        #rule 5. Avoid collision
        
        return car_speed

    def get_new_pos(self, gap):
        speed = self.get_car_speed(gap)
        new_pos = (self.position[0] + speed, self.position[1])
        return new_pos

    
    def get_car_info(self):
        info_dict = {'car id': self.car_id,
                 'car position': self.position,
                 'car speed': self.speed,
                 'car max speed': self.max_speed,
                 'car behavior type': self.agent_type,
                 'neighbors': self.neighbors_dict}
        return info_dict
     

    def take_a_step(self):
        gap = self.find_gap()
        self.position = self.get_new_pos(gap) 
        







    
