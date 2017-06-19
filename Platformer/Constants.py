# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:51:35 2017

@author: GWils
"""

white = (255,255,255)
black = (0,0,0)
red = (155,0,0)
red_light = (255,0,0)
green = (0,155,0,0)
green_light = (0,255,0)
yellow = (200,200,0)
yellow_light = (255,255,0)
blue = (0,0,255)
blue_light = (0,155,255)
sienna = (160,82,45)

title = 'Generic Platformer'
width = 480
height = 600
FPS = 60
hs_file = 'High Score.txt'
spritesheet_file = 'spritesheet_jumper.png'
refresh_idle = 350
refresh_walk = 200

font_name = 'arial'

boost_power = 40
power_spawn = 7
mob_freq = 5000

player_layer = 2
plat_layer = 1
pow_layer = 1
mob_layer = 2

player_acc = 0.8
player_fric = 0.15
player_grav = 0.8
player_jump = 20


platform_list = [(0,height-60),
                 (width/2 - 50, height/2 + 100),\
                 (25,height/2 - 200),\
                 (100,height/2 - 100),\
                 (375,height/2 + 50)]