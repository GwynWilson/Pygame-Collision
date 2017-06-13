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
        
class Button():
    def __init__(self,a_colour,i_colour,rect,action=None):
        self.active_colour = a_colour
        self.inactive_colour = i_colour
        self.rect = pygame.Rect(rect)
        self.rect.center = rect[0],rect[1]
        self.active = False
        self.action = action
        self.text = None
        
    def give_text(self,msg,size='small',colour=white):
        centre = self.rect.center
        self.text = Text(msg,size=size,pos=centre,colour=colour)
    
    def events(self,cursor,click):
        if self.rect.collidepoint(cursor):
            self.active = True
            if click[0] == 1 and self.action != None:
                return self.action
        else:
            self.active = False
        
        
    def render(self,screen):
        if self.active == True:
            pygame.draw.rect(screen,self.active_colour,self.rect)
        else:
            pygame.draw.rect(screen,self.inactive_colour,self.rect)
        if self.text != None:
            self.text.render(screen)
        
        
    