#!/usr/bin/python3

from abc import ABC, abstractmethod
from random import random, uniform


class Vehicle(ABC):
    next_id = 1
    def __init__(self, posx, posy, initial_speed, road_length, max_speed=3, vehicle_type='cooperator'):
        self.posx = posx
        self.posy = posy
        self.initial_speed = initial_speed
        self.road_length = road_length
        self.max_speed = max_speed
        self.vehicle_type = vehicle_type
        self.vehicle_speed = self.initial_speed

        self.previous_spd = self.vehicle_speed
        self.previous_posx = self.posx - 1
        if self.previous_posx < 0:
            self.previous_posx += self.road_length 

        self.f_speed = self.vehicle_speed
        self.new_speed = 0

        self.my_lane = []
        self.right_lane = []
        self.left_lane = []

        self.n_vehicle = None
        self.s_vehicle = None
        self.e_vehicle = None
        self.w_vehicle = None
        self.ne_vehicle = None
        self.se_vehicle = None
        self.sw_vehicle = None
        self.nw_vehicle = None

        self.si_vehicle = None

        self.road_length = road_length

        self.id = Vehicle.next_id
        Vehicle.next_id += 1

        # Model parameters
        self.barking_prob = .2
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
    def get_si_neighbor(self):
        pass

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
        info_dict = {'vehicle id': self.id,
                 'vehicle x position': self.posx,
                 'vehicle y position': self.posy,
                 'vehicle speed': self.vehicle_speed,
                 'vehicle max speed': self.max_speed,
                 'vehicle behavior type': self.vehicle_type,
                 'neighbors': {'n_neighbor': self.n_vehicle,
                               's_neighbor': self.s_vehicle,
                               'e_neighbor': self.e_vehicle,
                               'w_neighbor': self.w_vehicle,
                               'ne_neighbor': self.ne_vehicle,
                               'se_neighbor': self.se_vehicle,
                               'sw_neighbor': self.sw_vehicle,
                               'nw_neighbor': self.nw_vehicle
                     }
                 }

        return info_dict



class Car(Vehicle):

    def get_si_neighbor(self):
        self.s = self.S if uniform(0, 1) <= self.r else 1
        if self.s == 1:
            self.si_vehicle = self.n_vehicle
        elif self.s == 2:
            if len(self.my_lane) == 2:
                self.s = 1
                self.si_vehicle = self.n_vehicle
            else:
                sv = self.n_vehicle
                self.si_vehicle = sv.n_vehicle
        
    def get_neighbors(self, list_of_lanes):
        #TODO

        # Initial conditions
        if self.posy == 0:
            self.my_lane = list_of_lanes[0]
            self.right_lane = list_of_lanes[1]
            self.left_lane = None
        else:
            self.my_lane = list_of_lanes[1]
            self.left_lane = list_of_lanes[0]
            self.right_lane = None

        for index, item in enumerate(self.my_lane):
            if item.id == self.id:
                my_index = index
                
        # North and South neighbors
        if my_index == len(self.my_lane) - 1:
            self.n_vehicle = self.my_lane[0]
        else:
            self.n_vehicle = self.my_lane[my_index + 1]
        
        if my_index == 0:
            self.s_vehicle = self.my_lane[len(self.my_lane) - 1]
        else:
            self.s_vehicle = self.my_lane[my_index - 1]

        # West and East neighbors
        if self.left_lane == None:
            for index, item in enumerate(self.right_lane):
                if item.posx == self.posx:
                    self.e_vehicle = item
                else:
                    self.e_vehicle = None
        elif self.right_lane == None:
            for index, item in enumerate(self.left_lane):
                if item.posx == self.posx:
                    self.w_vehicle = item
                else:
                    self.w_vehicle = None

    def _gap(self, neigb):
        gap = neigb.posx - self.posx
        if gap < 0:
            gap = neigb.posx + self.road_length - 1 - self.posx
        if gap < 0:
            print('Alert! Gap < 0 for id =', self.id,'!')

        return gap 

    def _acceleration(self, speed, gap, neighb):
        if gap >= self.G and speed <= neighb.vehicle_speed:
            speed = min(self.max_speed, speed + 1)
            if speed < 0:
                print('Alarm in Acceleration, speed is negative for id =', self.id,'!')
                return 1
            else:
                return min(self.max_speed, speed + 1)
        else:
            return speed

    def _slow_to_start(self, speed, road):
        if uniform(0, 1) <= self.q:
            si_prev_pos = self.si_vehicle.previous_posx
            if si_prev_pos < self.previous_posx:
                if (si_prev_pos + road - 1) - self.previous_posx == 0:
                    speed = 0
                    return speed
                else:
                    speed = min(speed, (si_prev_pos + road - 1) - self.previous_posx - self.s)
                    if speed < 0:
                        print('Alarm in Slow-to-start, speed is negative for id =', self.id,'!')
                        return 1
                    else:
                        return speed
            else:
                speed = min(speed, si_prev_pos - self.previous_posx - self.s)
                if speed < 0:
                    print('Alarm in Slow-to-start, speed is negative for id =', self.id,'!')
                    return 1
                else:
                    return speed
        else:
            return speed
    
    def _quick_start(self, speed, road):
        si_curr_pos = self.si_vehicle.posx
        si_gap = self._gap(self.si_vehicle)
        if si_curr_pos < self.posx:
            if si_gap == 0:
                speed = 0
                return speed
            else:
                speed = min(speed, si_gap - self.s)
                return speed
            if speed < 0: 
                print('Alarm in Quick Start, speed is negative for id =', self.id,'!')
                return 1
            else:
                return speed 
        else:
            speed = min(speed, si_curr_pos - self.posx - self.s)
            if speed < 0:
                print('Alarm in Quick Start, speed is negative for id =', self.id,'!')
                return 1
            else:
                return min(speed, self.si_vehicle.posx - self.posx - self.s)

    def _random_brake(self, speed, gap):
        if uniform(0, 1) < 1 - self.barking_prob:
            speed = max(1, speed - 1)
            if gap >= self.G:
                self.barking_prob = self.P1
            elif gap < self.G:
                if self.vehicle_speed < self.n_vehicle.vehicle_speed:
                    self.barking_prob = self.P2
                elif self.vehicle_speed == self.n_vehicle.vehicle_speed:
                    self.barking_prob = self.P3
                elif self.vehicle_speed > self.n_vehicle.vehicle_speed:
                    self.barking_prob = self.P4
            if speed < 0:
                print('Alarm in Random Brake, speed is negative for id =', self.id,'!')
                return 1
            else:
                return speed
        else:
            return speed 

    def _avoid_collision(self, speed, gap):
        speed = min(speed, gap - 1 + self.n_vehicle.f_speed)
        if speed < 0:
            print('Alarm in Avoid Collision, speed is negative for id =', self.id,'!')
            return 1
        else:
            return speed

    def get_new_speed(self, road, show_speed=True):

        # Initial
        self.previous_spd = self.vehicle_speed

        __car_speed = self.vehicle_speed

        __gap = self._gap(self.n_vehicle)

        # rule 1. Acceleration
        __car_speed = self._acceleration(__car_speed, __gap, self.n_vehicle)

        # rule 2. Slow-to-start
        __car_speed = self._slow_to_start(__car_speed, road)

        # rule 3. Perspective (Quick Start)
        __car_speed = self._quick_start(__car_speed, road)
        
        # rule 4. Random brake
        __car_speed = self._random_brake(__car_speed, __gap)

        # rule 5. Avoid collision
        __car_speed = self._avoid_collision(__car_speed, __gap)

        # Get new speed
        self.new_speed = __car_speed

        if show_speed == True:
            print('id =', self.id, 'speed =', self.new_speed, 's =', self.s)

    def move(self, road):
        self.previous_posx = self.posx
        self.posx += self.new_speed
        if self.posx >= road:
            self.posx -= road
        self.vehicle_speed = self.new_speed

