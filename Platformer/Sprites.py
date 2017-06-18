# -*- coding: utf-8 -*-

import Constants as c
import pygame as pg
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
        self.image = game.spritesheet.get_image(614,1063,120,191)
        self.image.set_colorkey(c.black)
        self.rect = self.image.get_rect()
        self.rect.center = (c.width/2., c.height/2)
        self.pos = vec(c.width/2., c.height/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    
    def jump(self):
        #Could be moved into the game to avoid referancing game upon init
        self.pos.y += 1
        hits = pg.sprite.spritecollide(self,self.game.platforms,False)
        self.pos.y -= 1
        if hits:
            self.vel.y = -c.player_jump
    
    def update(self):
        self.acc = vec(0,c.player_grav)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] == keys[pg.K_RIGHT]:
            pass
        elif keys[pg.K_LEFT]:
            self.acc.x = -c.player_acc
        elif keys[pg.K_RIGHT]:
            self.acc.x = +c.player_acc
            
        self.acc.x += -self.vel.x * c.player_fric
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc
        
        if self.pos.x > c.width:
            self.pos.x = 0
        elif self.pos.x < 0:
            self.pos.x = c.width
        
        self.rect.midbottom = self.pos
        

class Platform(pg.sprite.Sprite):
    def __init__(self,x,y,w,h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(c.green_light)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y