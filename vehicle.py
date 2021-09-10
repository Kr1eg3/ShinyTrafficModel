#!/usr/bin/python3

from abc import ABC, abstractmethod



class Vehicle(ABC):
    next_id = 1
    def __init__(self, posx, posy, initial_speed, max_speed=5, vehicle_type='cooperator'):
        self.posx = posx
        self.posy = posy
        self.max_speed = max_speed
        self.vehicle_type = vehicle_type
        self.vehicle_speed = initial_speed

        self.neighbors = {}
        
        self.__previous_spd = self.vehicle_speed

        self.__n_vehicle = None
        self.__s_vehicle = None
        self.__e_vehicle = None
        self.__w_vehicle = None
        self.__ne_vehicle = None
        self.__se_vehicle = None
        self.__sw_vehicle = None
        self.__nw_vehicle = None

        self.id = Vehicle.next_id
        Vehicle.next_id += 1

        # Model parameters
        self.G = 2
        self.S = 2
        self.s = 1
        self.q = .99
        self.r = .2
        self.P1 = .999
        self.P2 = .99
        self.P3 = .98
        self.P4 = .01

    @abstractmethod
    def get_neighbors(self):
        pass

    @abstractmethod    
    def get_new_speed(self):
        pass

    @abstractmethod    
    def move(self):
        pass

    @property
    def get_vehicle_info(self):
        info_dict = {'car id': self.id,
                 'vehicle x position': self.posx,
                 'vehicle y position': self.posy,
                 'vehicle speed': self.vehicle_speed,
                 'vehicle max speed': self.max_speed,
                 'vehicle behavior type': self.vehicle_type,
                 'neighbors': self.neighbors}
        return info_dict



class Car(Vehicle):

    def get_neighbors(self, list_of_lanes):
        #TODO
        if self.posy == 0:
            my_lane = list_of_lanes[0]
            right_lane = list_of_lanes[1]
        else:
            my_lane = list_of_lanes[1]
            left_lane = list_of_lanes[0]


        print('i get neighbors!')

    def get_new_speed(self):
        print('i get new speed!')

    def move(self):
        print('i moving!')