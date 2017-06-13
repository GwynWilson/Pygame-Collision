# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 08:32:04 2017

@author: GWils
"""
import pygame
from objects import *
from constants import *

class Level():    
    def __init__(self,string):
        self.level = string
        self.blocklist  = []
        self.origin = None

    def gen_level(self,b_size):
        x = y =0
        for row in self.level:
            for col in row:
                if col == 'w':
                    self.blocklist.append(Block((x,y),b_size,white))
                if col == 'E':
                    self.blocklist.append(End((x,y),b_size,red))
                if col == 's':
                    self.blocklist.append(Spike((x,y),b_size,grey))
                if col == 'o':
                    self.origin = (x,y)
                x += b_size
            y += b_size
            x = 0
    
    def render(self,screen):      
        
        for b in self.blocklist:
            pygame.draw.rect(screen,b.colour,b.rect)

        
        
        