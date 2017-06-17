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
        self.button_list = []
        
        self.player = None
        
        self.press_right = False
        self.press_left = False
        self.press_up = False
        self.press_down = False
        
        self.clock = pygame.time.Clock()
    
    def button_events(self):
        cursor = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for button in self.button_list:
            action = button.events(cursor,click)
            if action == 'play':
                self.text_list = []
                self.button_list = []
                self.level = None
                self.player = Player((b_size,b_size))
                self.main_loop()
                title = False
            elif action == 'quit':
                pygame.quit()
                quit()

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
        self.button_events()
        
    def update(self):
        for b in self.level.blocklist:
            if isinstance(b,Moving):                
                b.update(self.level.blocklist)
                    
    def render(self):
        self.screen.fill(black)
        if self.level != None:
            self.level.render(screen)
        if self.player != None:
            self.player.render(screen,yellow)
        if len(self.text_list)>0:
            for text in self.text_list:
                text.render(self.screen)
        if len(self.button_list)>0:       
            for button in self.button_list:
                button.render(screen)
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
            self.update()
            self.render()
       
    def main_loop(self):
        for level_ in self.level_list:
            self.screen.fill(black)
            self.level = Level(level_)
            self.level.gen_level(b_size)
            self.player.__init__(self.level.origin)
            self.level_loop()
            self.running = True
        self.end_loop()
    
    def title_loop(self):
        title = True
        self.level = Level(level_0)
        self.level.gen_level(b_size)
        self.text_list.append(Text('Welcome',colour=red,
                                   pos=(s_width/2,s_height/4),size='large'))
        
        play_button = Button(grey,white,((1/4.)*s_width,(3/4.)*s_height,100,50),
                             action='play')
                             
        play_button.give_text('Play','small',black)
        self.button_list.append(play_button)
        
        quit_button = Button(grey,white,((3/4.)*s_width,(3/4.)*s_height,100,50),
                             action='quit')
                             
        quit_button.give_text('Quit','small',black)
        self.button_list.append(quit_button)
        
        while title:
            self.events()                    
            self.render()
            
    def end_loop(self):
        end = True
        self.player = None
        self.level = Level(level_0)
        self.level.gen_level(b_size)
        self.text_list.append(Text('Thanks For Playing',colour=red,
                                   pos=(s_width/2,s_height/4),size='med'))
        
        quit_button = Button(grey,white,(s_width/2,s_height/2,100,50),
                             action='quit')
                             
        quit_button.give_text('Quit','small',black)
        self.button_list.append(quit_button)
        
        while end:
            self.events()                
            self.render()
       
        
g = Game(screen,clock)
g.title_loop()
pygame.quit()
quit()