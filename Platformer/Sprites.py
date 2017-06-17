# -*- coding: utf-8 -*-

import Constants as c
import pygame as pg
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30,40))
        self.image.fill(c.yellow)
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
            self.vel.y = -20
    
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
        self.image.fill(c.green)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y