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
        self.font_name = pg.font.match_font(c.font_name)
        
        pg.init()
        pg.mixer.init()
        
    def new_game(self):
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for plat in c.platform_list:
            p = Platform(*plat)
            self.platforms.add(p)
            self.all_sprites.add(p)
            
        self.game_loop()
        
    def draw_text(self,text,size,colour,x,y):
        font_ = pg.font.Font(self.font_name,size)
        text_surface = font_.render(text,True,colour)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x,y)
        self.screen.blit(text_surface,text_rect)
        
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
                
        if self.player.rect.top <= c.height/4:
            scroll_vel = abs(self.player.vel.y)
            self.player.pos.y += scroll_vel
            for plat in self.platforms:
                plat.rect.y += scroll_vel
                if plat.rect.top > c.height:
                    self.score += 10
                    plat.kill()
                    
        while len(self.platforms) < 6:
            plat_width = random.randrange(30,100)
            y = -random.randrange(30,75)
            x = random.randrange(0,c.width - plat_width)
            p = Platform(x,y,plat_width,20)
            self.platforms.add(p)
            self.all_sprites.add(p)
            
            
        if self.player.rect.bottom > c.height:
            for sprite in self.all_sprites:
                sprite.rect.y -= self.player.vel.y
                if sprite.rect.top < 0:
                    sprite.kill()
                    
        if len(self.platforms) < 1:
            self.playing = False
                
    
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
        self.all_sprites.draw(self.screen)
        self.draw_text('Score :{}'.format(str(self.score)),22,c.white,0,0)
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