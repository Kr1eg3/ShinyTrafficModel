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
from operator import attrgetter


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
    __get_neighbors(cars_list):
        Description
    __get_gap(args)
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
        self.__previous_pos = 0
        self.__previous_spd = 0
        self.__rnd_brake_spd = 0
        self.neighbors_dict = {}
        Car.next_id += 1

        ### model parameters ##
        self.G = 3
        self.S = 1
        self.s = 1
        self.q = .2
        self.r = .2
        self.P1 = .5
        self.P2 = .4
        self.P3 = .3
        self.P4 = .2
        #######################
        
    def __get_neighbors(self, cars_list):
        
        #forward car
        __cars = [car for car in cars_list if getattr(car,
            'position')[1] > self.position[1] and getattr(car,
                'position')[0] == self.position[0]]
        __fcar = min(__cars, key=lambda x: x.position[1])
        self.neighbors_dict['forward neighbor_id'] = __fcar.car_id

        #car behind
        __cars = [car for car in cars_list if getattr(car,
            'position')[1] < self.position[1] and getattr(car,
                'position')[0] == self.position[0]]
        __fcar = max(__cars, key=lambda x: x.position[1])
        self.neighbors_dict['behind neighbor_id'] = __fcar.car_id

        #left/right car
        __fcar = [car for car in cars_list if getattr(car,
            'position')[1] == self.position[1] and getattr(car,
                'position')[0] < self.position[0]]
        self.neighbors_dict['left neighbor_id'] = __fcar.car_id

        __fcar = [car for car in cars_list if getattr(car,
            'position')[1] == self.position[1] and getattr(car,
                'position')[0] >  self.position[0]]
        self.neighbors_dict['right neighbor_id'] = __fcar.car_id

        #left/right side car
        __cars = [car for car in cars_list if getattr(car,
            'position')[1] > self.position[1] and getattr(car,
                'position')[0] < self.position[0]]
        __fcar = min(__cars, key=lambda x: x.position[1])
        self.neighbors_dict['left side forward car id'] = __fcar.car_id

        __cars = [car for car in cars_list if getattr(car,
             'position')[1] < self.position[1] and getattr(car,
                 'position')[0] < self.position[0]]
        __fcar = max(__cars, key=lambda x: x.position[1])
        self.neighbors_dict['left side behind car id'] = __fcar.car_id
        
        __cars = [car for car in cars_list if getattr(car, 
            'position')[1] > self.position[1] and getattr(car, 
                'position')[0] > self.position[0]]
        __fcar = min(__cars, key=lambda x: x.position[1])
        self.neighbors_dict['rigth side forward car id'] = __fcar.car_id

        __cars = [car for car in cars_list if getattr(car,
            'position')[1] < self.position[1] and getattr(car,
                'position')[0] > self.position[0]]
        __fcar = max(__cars, key=lambda x: x.position[1])
        self.neighbors_dict['right side behind car id'] = __fcar.car_id


#all_frames = []
#
#for i in range(10):
#    img = np.random.randint(0, high=255, size=(720, 1280, 3), dtype=np.uint8) # generate a random, noisy image
#    all_frames.append(Frame(img, i))
#
#frames_to_plot = [frame for frame in all_frames if getattr(frame, index) == 5]


#import operator
#min([MyClass(3), MyClass(1), MyClass(2)], key=operator.attrgetter('foo'))
#MyClass(1)



    def __get_gap(self, cars_list):
        __forward_car = [car for car in cars_list if getattr(car,
            'car_id') == self.neighbors_dict['forward neighbor car id']]
        __gap = __forward_car.position[1] - self.position[1] 
        return __gap


    def get_car_speed(self, cars_list):
        
        self.__previous_spd = self.speed
        #__next_car = 
        

        #rule 1. Acceleration
        if gap >= self.G and self.speed <= __next_car.speed:
            __car_speed = min(self.max_speed, self.speed + 1)

        #rule 2. Slow-to-start
        if uniform(0, 1) <= self.q:
            self.s = self.S if uniform(0, 1) <= self.r else 1
            __car_speed = min(car_speed, 1)
        
        #rule 3. Perspective (Quick start)
        

        #rule 4. Random brake
        if uniform(0, 1) < 1 - self.braking_prob:
            __car_speed = max(1, __car_speed - 1)
            self.__rnd_brake_spd = __car_speed
            if self.__get_gap >= self.G:
                self.braking_prob = self.P1
            else:
                if self.__previous_spd < __next_car.__previous_spd:
                    self.braking_prob = self.P2
                elif self.__previous_spd == __next_car.__previous_spd:
                    self.braking_prob = self.P3
                elif self.__previous_spd > __next_car.__previous_spd:
                    self.braking_prob = self.P4
    
        #rule 5. Avoid collision
        __car_speed = min(__car_speed, self.__get_gap() - 1 + __next_car.__rnd_brake_spd)

        
        return __car_speed

    def get_new_pos(self, gap):
        #speed = self.get_car_speed(gap)
        new_pos = (self.position[1] + speed, self.position[0])
        return new_pos

    
    def get_car_info(self):
        info_dict = {'car id': self.car_id,
                 'car previous position': self.__previous_pos,
                 'car position': self.position,
                 'car speed': self.speed,
                 'car max speed': self.max_speed,
                 'car behavior type': self.agent_type,
                 'neighbors': self.neighbors_dict}
        return info_dict
     

    def take_a_step(self, cars_list):
        self.__get_neighbors(cars_list)
        #gap = self.find_gap()
        #self.position = self.get_new_pos(gap) 
        







    
