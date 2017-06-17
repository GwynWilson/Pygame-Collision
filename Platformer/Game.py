# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:49:52 2017

@author: GWils
"""

import pygame as pg
import random
import Constants as c
from Sprites import *

class Game():
    def __init__(self):
        self.running = True
        self.screen = pg.display.set_mode((c.width,c.height))
        self.clock = pg.time.Clock()
        
        pg.init()
        pg.mixer.init()
        
    def new_game(self):
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for p in c.platform_list:
            self.platforms.add(Platform(*p))
        self.game_loop()
    
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running =False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
              
    def draw(self):
        self.screen.fill(c.black)
        self.platforms.draw(self.screen)
        self.all_sprites.draw(self.screen)
        pg.display.update()
    
    def game_loop(self):
        self.playing = True
        while self.playing:
            self.clock.tick(c.FPS)
            self.events()
            self.update()
            self.draw()

    def show_start_screen(self):
        pass
    
    def show_go_screen(self):
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new_game()
    g.show_go_screen()
    
pg.quit()