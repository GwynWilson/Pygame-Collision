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
#        self.clock = clock
        self.running = True
        self.fps = 30
        self.level = Level(level_1)
        self.player = Player(b_size,b_size,b_size)
        
        self.press_right = False
        self.press_left = False
        self.press_up = False
        self.press_down = False
        
        self.clock = pygame.time.Clock()
        self.frame_duration_ms = 1000/30
        
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
        self.level.render(screen,white)
        self.player.render(screen,red)
        pygame.display.flip()       
        self.clock.tick(self.fps)
        
    def move_player(self):
        if self.press_left == self.press_right:
            self.player.dx = 0
        elif self.press_left == True:
            self.player.dx = -player_vel
        elif self.press_right == True:
            self.player.dx = player_vel
           
        if self.press_up == self.press_down:
            self.player.dy = 0
        elif self.press_up == True:
            self.player.dy = -player_vel
        elif self.press_down == True:
            self.player.dy = player_vel
        
    def collision_detection(self):
        for wall in self.level.blocklist:
#            if self.player.rect.colliderect(wall.rect):
#                print 'collision'
#                if self.player.dx > 0: 
#                    print 'collision2'
#                    self.player.x = wall.rect[0] 
#                if self.player.dx < 0: 
#                    self.player.rect.x = wall.rect[0] + b_size
#                if self.player.dy > 0: 
#                    self.player.rect.y = wall.rect.top -b_size
#                if self.player.dy < 0: 
#                    self.player.rect.y = wall.rect.bottom

       
    def main_loop(self):
        self.screen.fill(black)
        self.level.gen_level(b_size)
        
        while self.running:
            self.events()
            self.move_player() 
            self.collision_detection()
            self.player.move()
            self.render()
        
g = Game(screen,clock)
g.main_loop()
pygame.quit()
quit()