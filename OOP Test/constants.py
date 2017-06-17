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

level_0 = ['wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',]

level_1 = ['wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w o                        E w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'w                            w',
           'wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',]
           
level_2 = ['wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
           'w  E     w        w          w',
           'wwwww         w              w',
           'w   wwwwwwwwwwwwwwwww        w',
           'w    w              w        w',
           'w    w   wwwwwwwwwwwwwwww    w',
           'w    w   w                   w',
           'w        w                   w',
           'w  wwwwwww        wwwwwwwwwwww',
           'w        w        w        o w',
           'w        w       ww          w',
           'wwwwww   w       w     wwwwwww',
           'w                w           w',
           'wwwwwwwwwwwwww   wwwwwwwww   w',
           'w                w   w       w',
           'w                w   w       w',
           'w    wwwwwwwwwwwww   w       w',
           'w                    w       w',
           'w                            w',
           'wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',]

level_3 = ['wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
           'w  o                         w',
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
           'w            wwwwww    wwwwwww',
           'w            w               w',
           'w            w          E    w',
           'wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',]
          
level_4 = ['wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
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
           
#level_n = ['wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
#           'w           R                w',
#           'w                            w',
#           'w         L                  w',
#           'w             U              w',
#           'w              o             w',
#           'w       D                    w',
#           'w                            w',
#           'w                            w',
#           'w                            w',
#           'w                            w',
#           'w             d              w',
#           'w                            w',
#           'w          l                 w',
#           'w                u           w',
#           'w                            w',
#           'w                  r         w',
#           'w                            w',
#           'w                            w',
#           'wwwwwwwwwwwwwwwwwwwwwwwwwwwwww',]
         
level_list = [level_1,level_2,level_3,level_4]
#level_list = [level_n]