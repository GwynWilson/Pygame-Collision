# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 08:32:04 2017

@author: GWils
"""
import pygame

class Block():
    def __init__(self,pos,b_size):
        self.rect = pygame.Rect(pos[0],pos[1],b_size,b_size)
        self.aabb = (pos[0],pos[1],b_size,b_size)

class Level():
    
    def __init__(self,string):
        self.level = string
        self.blocklist  = []
    
    def gen_level(self,b_size):
        x = y =0
        for row in self.level:
            for col in row:
                if col == 'w':
                    self.blocklist.append(Block((x,y),b_size))
                x += b_size
            y += b_size
            x = 0
    
    def render(self,screen,color):      
        
        for b in self.blocklist:
            pygame.draw.rect(screen,color,b.rect)
        
        
        