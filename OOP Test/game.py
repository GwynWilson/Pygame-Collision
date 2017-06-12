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
        
        self.level_list = level_list
        self.level = None
        
        self.text_list = []
        
        self.player = Player((b_size,b_size))
        
        self.press_right = False
        self.press_left = False
        self.press_up = False
        self.press_down = False
        
        self.clock = pygame.time.Clock()
        
    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
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
        for text in self.text_list:
            text.render(self.screen,red)
        pygame.display.flip()       
        self.clock.tick(self.fps)
        
    def move_player(self, blocklist):
        
        if self.press_left == self.press_right:
            end = self.player.move(0,0, blocklist)
        elif self.press_left == True:
            end = self.player.move(-player_vel,0, blocklist)
        elif self.press_right == True:
            end = self.player.move(player_vel,0, blocklist)
           
        if self.press_up == self.press_down:
            self.player.move(0,0, blocklist)
        elif self.press_up == True:
            self.player.move(0,-player_vel, blocklist)
        elif self.press_down == True:
            self.player.move(0,player_vel, blocklist)
        
        return end
        
    def level_loop(self):
        while self.running:
            self.events()
            self.running = self.move_player(self.level.blocklist)
            self.render()
       
    def main_loop(self):
        for level_ in self.level_list:
            self.screen.fill(black)
            self.level = Level(level_)
            self.level.gen_level(b_size)
            self.player.origin = self.level.origin
            self.level_loop()
            self.running = True
    
    def title_loop(self):
        title = True
        self.text_list.append(Text('Welcome',colour=red,pos=(s_width/2,s_height/4),size='large'))
        self.text_list.append(Text('Press P to play',colour=white,pos=(s_width/2,s_height/2)))
        self.text_list.append(Text('Press Q to play',colour=white,pos=(s_width/2,s_height/2 +20)))
        while title:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    self.running = False
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_p:
                        self.text_list = []
                        self.main_loop()
                        title = False
                    elif e.key == pygame.K_q:
                        pygame.quit()
                        quit()
            
            self.screen.fill(black)
            for text in self.text_list:
                text.render(self.screen)
            pygame.display.flip()
            self.clock.tick(5)
            
        print 'Thanks For Playing'
        
        
g = Game(screen,clock)
g.title_loop()
pygame.quit()
quit()