# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 07:52:09 2017

@author: GWils
"""
import pygame
from constants import *
from player import *
from level import *

pygame.init()

screen = pygame.display.set_mode((s_width,s_height))
clock = pygame.time.Clock()

class Game():
    
    def __init__(self,screen,clock):
        self.screen = screen
        self.running = True
        self.fps = 60
        
        self.level = Level(level_1)
        self.level.gen_level(b_size)
        
        self.player = Player(b_size)
        
        self.press_right = False
        self.press_left = False
        self.press_up = False
        self.press_down = False
        
        self.clock = pygame.time.Clock()
        
    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False 
            
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.press_right = True
                elif e.key == pygame.K_LEFT:
                    self.press_left = True
                elif e.key == pygame.K_UP:
                    self.press_up = True
                elif e.key == pygame.K_DOWN:
                    self.press_down = True
                    
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.press_right = False
                elif e.key == pygame.K_LEFT:
                    self.press_left = False
                elif e.key == pygame.K_UP:
                    self.press_up = False
                elif e.key == pygame.K_DOWN:
                    self.press_down = False
                    
    def render(self):
        self.screen.fill(black)
        self.level.render(screen)
        self.player.render(screen,yellow)
        pygame.display.flip()       
        self.clock.tick(self.fps)
        
    def move_player(self, blocklist):
        if self.press_left == self.press_right:
            self.player.move(0,0, blocklist)
        elif self.press_left == True:
            self.player.move(-player_vel,0, blocklist)
        elif self.press_right == True:
            self.player.move(player_vel,0, blocklist)
           
        if self.press_up == self.press_down:
            self.player.move(0,0, blocklist)
        elif self.press_up == True:
            self.player.move(0,-player_vel, blocklist)
        elif self.press_down == True:
            self.player.move(0,player_vel, blocklist)
        
    def main_loop(self):
        self.screen.fill(black)
        self.level.gen_level(b_size)
        self.player.origin = self.level.origin
        
        while self.running:
            self.events()
            self.move_player(self.level.blocklist)
            self.render()
        
g = Game(screen,clock)
g.main_loop()
pygame.quit()
quit()