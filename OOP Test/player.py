# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 08:49:45 2017

@author: GWils
"""

import pygame
from constants import *
from objects import *

class Player():
    def __init__(self,origin):
        self.origin = origin
        self.x = self.origin[0]
        self.y = self.origin[1]
        self.size = b_size
        self.rect = pygame.Rect(self.x,self.y,self.size,self.size)
        
    def collision(self,dx,dy,blocklist):
        for wall in blocklist:
            if isinstance(wall,End) and self.rect.colliderect(wall.rect):
                return False
            elif isinstance(wall,Spike) and self.rect.colliderect(wall.rect):
                self.rect.topleft = (self.origin)
            elif self.rect.colliderect(wall.rect):
                if dx > 0: 
                    self.rect.right = wall.rect.left
                if dx < 0: 
                    self.rect.left = wall.rect.right
                if dy > 0: 
                    self.rect.bottom = wall.rect.top
                if dy < 0: 
                    self.rect.top = wall.rect.bottom 
        return True 
             
    def move(self,dx,dy,blocklist):
        
        self.rect.x += dx
        self.rect.y += dy

        end = self.collision(dx,dy,blocklist)
        return end

    def render(self,screen,colour):
        pygame.draw.rect(screen,colour,self.rect)