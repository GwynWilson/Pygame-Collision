# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 08:49:45 2017

@author: GWils
"""

import pygame

class Player():
    def __init__(self,b_size,x,y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.size = b_size
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
    def render(self,screen,colour):
        pygame.draw.rect(screen,colour,(self.x,self.y,self.size,self.size))