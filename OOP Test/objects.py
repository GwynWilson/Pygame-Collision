# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:37:25 2017

@author: GWils
"""
import pygame
from constants import *

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
        
class Text():
    def __init__(self,msg,size='small',pos=None,colour=white):
        self.message = msg
        self.size = size
        self.pos = pos
        self.colour = colour
    
    def text_objects(self):
        if self.size == 'small':
            text_surface = small_font.render(self.message,True,self.colour)
        elif self.size == 'med':
            text_surface = med_font.render(self.message,True,self.colour)
        elif self.size == 'large':
            text_surface = large_font.render(self.message,True,self.colour)
        return text_surface,text_surface.get_rect()
    
    def render(self,screen):
        text_surface, text_rect = self.text_objects()
        if self.pos != None:
            text_rect.center = self.pos[0],self.pos[1]
        else:
            text_rect.center = s_width/2 , s_height/2
        screen.blit(text_surface,text_rect)
        
    