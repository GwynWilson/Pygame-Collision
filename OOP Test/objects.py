# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:37:25 2017

@author: GWils
"""
import pygame

class Block():
    def __init__(self,pos,b_size,colour):
        self.rect = pygame.Rect(pos[0],pos[1],b_size,b_size)
        self.colour = colour

class End(Block):
    def __init__(self,pos,b_size,colour):
        Block.__init__(self,pos,b_size,colour)
        
class Spike(Block):
    def __init__(self,pos,b_size,colour):
        Block.__init__(self,pos,b_size,colour)
    