import numpy as np
import random
import keyboard
from typing import List, Tuple

class Snake():

    def __init__(self, position=None, orientation=None, points=0):

        if position is not None:
            self.position = position
        else:
            self.position = np.array([7,7], np.int16)
            
        if orientation is not None:
            self.orientation = orientation
        else:
            self.orientation = random.choice(['up', 'down', 'left', 'right'])

        self.trail = []
        self.state = 'alive'
        self.points = points

    def change_position(self):
        if self.orientation == 'up':
            self.position[0] += 1
        if self.orientation == 'down':
            self.position[0] -= 1
        if self.orientation == 'left':
            self.position[1] -= 1
        if self.orientation == 'right':
            self.position[1] += 1
        self.trail.append(tuple([self.position[0], self.position[1]]))
    

    def grow(self, points):
        self.points = points
        self.body_position = self.trail[-points::] 


    def change_orientation(self, key):
        if key.name == 'up' and self.orientation not in ['up', 'down']:
            self.orientation = 'up'
        elif key.name ==  'down' and self.orientation not in ['up', 'down']:
            self.orientation = 'down'
        elif key.name == 'left' and self.orientation not in ['left', 'right']:
            self.orientation = 'left'
        elif key.name == 'right' and self.orientation not in ['left', 'right']:
            self.orientation = 'right'


    def check_if_dies(self, walls: List[Tuple[int, int]]):
        
        hits_wall = set([(self.position[0], self.position[1])]).issubset(walls)

        try:
            eats_itself = bool(set([(self.position[0], self.position[1])]).intersection(self.body_position))
        except AttributeError:
            eats_itself = False
        
        if hits_wall or eats_itself:        
            self.state = 'dead'

class Fruits():
    def __init__(self, free_coordinates):
        """
        FRUIT MUST BE INSTANTIATED BEFORE THE LOOP.  
        """
        self.state = 'not eaten'
        self.position = tuple([10,7])#random.choice(tuple(free_coordinates))

    def spawns(self, free_coordinates):
        self.position = random.choice(tuple(free_coordinates))

    def gets_eaten(self, snake_position):
        
        if tuple(snake_position) == self.position:
            self.state = 'eaten'
        


        

    

    



