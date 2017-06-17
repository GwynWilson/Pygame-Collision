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
                    self.blocklist.append(Wall((x,y),b_size,white))
                elif col == 'E':
                    self.blocklist.append(End((x,y),b_size,red))
                elif col == 's':
                    self.blocklist.append(Spike((x,y),b_size,grey))
                elif col == 'o':
                    self.origin = (x,y)
                elif col == 'l':
                    self.blocklist.append(Moving_Spike((x,y),b_size,
                                                       grey,direction='left'))
                elif col == 'r':
                    self.blocklist.append(Moving_Spike((x,y),b_size,
                                                       grey,direction='right'))
                elif col == 'u':
                    self.blocklist.append(Moving_Spike((x,y),b_size,
                                                       grey,direction='up'))
                elif col == 'd':
                    self.blocklist.append(Moving_Spike((x,y),b_size,
                                                       grey,direction='down'))
                elif col == 'L':
                    self.blocklist.append(Moving_Wall((x,y),b_size,
                                                      white,direction='left'))
                elif col == 'R':
                    self.blocklist.append(Moving_Wall((x,y),b_size,
                                                      white,direction='right'))
                elif col == 'U':
                    self.blocklist.append(Moving_Wall((x,y),b_size,
                                                      white,direction='up'))
                elif col == 'D':
                    self.blocklist.append(Moving_Wall((x,y),b_size,
                                                      white,direction='down'))
                x += b_size
                
            y += b_size
            x = 0
    
    def render(self,screen):      
        
        for b in self.blocklist:
            pygame.draw.rect(screen,b.colour,b.rect)

        
        
        