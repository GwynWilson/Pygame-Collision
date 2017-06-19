# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 15:49:52 2017

@author: GWils
"""

import pygame as pg
import random
import Constants as c
from Collision import *
from Sprites import *
from os import path

class Game():
    def __init__(self):
        self.running = True
        self.screen = pg.display.set_mode((c.width,c.height))
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(c.font_name)
        self.load_data()
        self.collide = Collide(self)
        
        pg.init()
        pg.mixer.init()
        
    def load_data(self):
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir,'img')
        with open(path.join(self.dir,c.hs_file),'r+') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        
        self.spritesheet = Spritesheet(path.join(img_dir,c.spritesheet_file))
        
        self.cloud_images = []
        for i in range(1,4):
            img = pg.image.load(path.join(img_dir,'cloud{}.png'.format(i))).convert()
            self.cloud_images.append(img)
#        snd_dir = path.join(self.dir,'snd')
#        self.jump_sound = pg.mixer.Sound(path.join(path.join(self.dir,'snd'),'Jump.mp3'))
         
    def new_game(self):
        self.score = 0
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.platforms = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.clouds = pg.sprite.Group()
        self.mob_timer = 0
        self.player = Player(self)
        for plat in c.platform_list:
            p = Platform(self,*plat)
        
        for i in range(5):
            cl = Cloud(self)
            cl.rect.y += 500
            
        self.collide.plat_collide = True
        self.game_loop()
        
    def draw_text(self,text,size,colour,x,y,topleft=False):
        font_ = pg.font.Font(self.font_name,size)
        text_surface = font_.render(text,True,colour)
        text_rect = text_surface.get_rect()
        if topleft == False:
            text_rect.center = (x,y)
        else:
            text_rect.topleft = (x,y)
        self.screen.blit(text_surface,text_rect)
        
    def update(self):
        self.all_sprites.update()
        
        self.collide.mob_collision()        
        self.collide.platform_collision()   
        self.collide.pow_collision()
        
        if self.player.rect.top <= c.height/4:
            if random.randrange(100) < 10:
                Cloud(self)
            scroll_vel = max(3,abs(self.player.vel.y))
            self.player.pos.y += scroll_vel
            
            for cloud in self.clouds:
                cloud.rect.y += (scroll_vel // 2)
                if cloud.rect.top > c.height:
                    cloud.kill()
            for plat in self.platforms:
                plat.rect.y += scroll_vel
                if plat.rect.top > c.height:
                    self.score += 10
                    plat.kill()       
            for mob in self.mobs:
                mob.rect.y += scroll_vel
                if mob.rect.top > c.height:
                    mob.kill()
                    
        while len(self.platforms) < 6:
            plat_width = random.randrange(30,100)
            y = -random.randrange(30,75)
            x = random.randrange(0,c.width - plat_width)
            p = Platform(self,x,y)

        if self.player.rect.bottom > c.height:
            for sprite in self.all_sprites:
                sprite.rect.y -= self.player.vel.y
                if sprite.rect.top < 0:
                    sprite.kill()  
                    
        now = pg.time.get_ticks()
        if now - self.mob_timer > c.mob_freq + random.choice([-1000,-500,0,500,1000]):
            self.mob_timer = now
            Mob(self)
                    
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
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()
    def draw(self):
        self.screen.fill(c.blue_light)
        self.all_sprites.draw(self.screen)
        self.draw_text('Score :{}'.format(str(self.score)),22,c.white,0,0,topleft=True)
        pg.display.update()
        
    def wait_input(self):
        start = False
        while not start:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    start = True
                if event.type == pg.KEYDOWN:
                    start = True
    
    def game_loop(self):
        self.playing = True
        while self.playing:
            self.clock.tick(c.FPS)
            self.events()
            self.update()
            self.draw()

    def show_start_screen(self):
        self.screen.fill(c.blue_light)
        self.draw_text('Title',50,c.white,c.width/2,c.height/4)
        self.draw_text('Arrows to move, spae to jump',20,c.white,c.width/2,c.height/2)
        self.draw_text('Press any key to continue',20,c.white,c.width/2,c.height* 3/4)
        self.draw_text('High Score :{}'.format(self.highscore),
                       20,c.white,c.width/2,15)
        pg.display.update()
        self.wait_input()
        

    
    def show_go_screen(self):
        if not self.running:
            return
        self.screen.fill(c.blue_light)
        self.draw_text('Game Over',50,c.white,c.width/2,c.height/4)
        self.draw_text('Score :{}'.format(str(self.score)),
                       20,c.white,c.width/2,c.height/2)
        self.draw_text('Press any key to continue',20,c.white,c.width/2,c.height* 3/4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text('NEW HIGH SCORE',20,c.white,c.width/2,c.height/2+40)
            with open(path.join(self.dir,c.hs_file),'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text('High Score :{}'.format(self.highscore),
                           20,c.white,c.width/2,c.height/2 + 40)
        
        pg.display.update()
        self.wait_input()

g = Game()
g.show_start_screen()
while g.running:
    g.new_game()
    g.show_go_screen()
    
pg.quit()