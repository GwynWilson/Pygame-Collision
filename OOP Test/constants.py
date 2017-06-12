# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 08:09:40 2017

@author: GWils
"""
import pygame
pygame.init()


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,51)
grey = (160,160,255)

b_size = 16
s_width = b_size*30
s_height = b_size*20

player_vel = 4

small_font = pygame.font.SysFont(None,25)
med_font = pygame.font.SysFont(None,50)
large_font = pygame.font.SysFont(None,80)

level_1 = ['wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
           'wo                           w',
           'w            s               w',
           'w                       s    w',
           'w                            w',
           'w    s             s         w',
           'w                            w',
           'w           s                w',
           'w                            w',
           'w                            w',
           'w        s                   w',
           'w                    s       w',
           'w              s             w',
           'w                            w',
           'w    s                  s    w',
           'w                            w',
           'w            ssssss    ssssssw',
           'w            s               w',
           'w            s          E    w',
           'wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',]
          
level_2 = ['wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
           'w  E                         w',
           'w                            w',
           'w                            w',
           'wsssssssssssssssss   ssssssssw',
           'w                            w',
           'w                            w',
           'wsss   ssssssssssssssss  ssssw',
           'w                            w',
           'w                            w',
           'w                            w',
           'wsssssssssssss   ssssssssssssw',
           'w                            w',
           'w                            w',
           'w                            w',
           'wsssss   ssssssssssssssssssssw',
           'w                            w',
           'w                            w',
           'w                       o    w',
           'wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',]
         
level_list = [level_1,level_2]