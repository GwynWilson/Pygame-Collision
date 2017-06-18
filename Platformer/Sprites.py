# -*- coding: utf-8 -*-

import Constants as c
import pygame as pg
from random import choice
vec = pg.math.Vector2

class Spritesheet():
    def __init__(self,filename):
        self.spritesheet = pg.image.load(filename).convert()
        
    def get_image(self,x,y,width,height):
        image = pg.Surface((width,height))
        image.blit(self.spritesheet,(0,0),(x,y,width,height))
        image = pg.transform.scale(image,(width//2,height//2))
        return image

class Player(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.load_images()
        self.image = self.standing_frames[0]
        self.image.set_colorkey(c.black)
        
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        
        self.rect = self.image.get_rect()
        self.rect.center = (40, c.height - 100)
        self.pos = vec(40, c.height - 100)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        
    def set_colour_key(self,list_):
        for img in list_:
            img.set_colorkey(c.black)
    
    def load_images(self):
        self.standing_frames = [self.game.spritesheet.get_image(614,1063,120,191),
                                self.game.spritesheet.get_image(690,406,120,201)]

        self.set_colour_key(self.standing_frames)
        self.walk_frames_r = [self.game.spritesheet.get_image(678,860,120,201),
                              self.game.spritesheet.get_image(692,1458,120,207)]
        for i in self.walk_frames_r:
            i.set_colorkey(c.black)
        self.set_colour_key(self.walk_frames_r)
        self.walk_frames_l = [pg.transform.flip(x,True,False) for x in self.walk_frames_r]
        self.jump_frame = self.game.spritesheet.get_image(382,763,150,181)
        self.jump_frame.set_colorkey(c.black)
         
    def jump(self):
        #Could be moved into the game to avoid referancing game upon init
        self.pos.y += 1
        hits = pg.sprite.spritecollide(self,self.game.platforms,False)
        self.pos.y -= 1
        if hits:
#            self.jumping = True
            self.vel.y = -c.player_jump
    
    def animate_frame(self,list_,now,ref):
        if now - self.last_update > ref:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(list_)
            self.image = list_[self.current_frame]
            bot = self.rect.bottom
            self.rect = self.image.get_rect()
            self.rect.bottom = bot
    
    def animate(self):
        now = pg.time.get_ticks() 
        if not self.jumping and not self.walking:
            if now - self.last_update > c.refresh_idle:
                self.animate_frame(self.standing_frames,now,c.refresh_idle)
        elif not self.jumping and self.walking:
            if now - self.last_update > c.refresh_walk:
                if self.vel.x > 0:
                    self.animate_frame(self.walk_frames_r,now,c.refresh_walk)
                elif self.vel.x < 0:
                    self.animate_frame(self.walk_frames_l,now,c.refresh_walk)
#        elif self.jumping:
#            self.image = self.jump_frame
#            bot = self.rect.bottom
#            self.rect = self.image.get_rect()
#            self.rect.bottom = bot
            
    def update(self):
        self.animate()
        self.acc = vec(0,c.player_grav)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] == keys[pg.K_RIGHT]:
            self.walking = False
            pass
        elif keys[pg.K_LEFT]:
            self.acc.x = -c.player_acc
            self.walking = True
        elif keys[pg.K_RIGHT]:
            self.acc.x = +c.player_acc
            self.walking = True
            
        self.acc.x += -self.vel.x * c.player_fric
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc
        
        
        if self.pos.x > c.width + self.rect.width/2:
            self.pos.x = 0 - self.rect.width/2
        elif self.pos.x < 0 - self.rect.width/2:
            self.pos.x = c.width + self.rect.width/2
        
        self.rect.midbottom = self.pos
        

class Platform(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        images = [self.game.spritesheet.get_image(0,288,380,94),
                  self.game.spritesheet.get_image(213,1662,201,100)]
                  
        self.image = choice(images)
#        self.image.fill(c.green_light)
        self.image.set_colorkey(c.black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y