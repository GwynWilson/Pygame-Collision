# -*- coding: utf-8 -*-

import Constants as c
import pygame as pg
from random import choice,randrange
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
        self.groups = game.all_sprites
        self._layer = c.player_layer
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.load_images()
        self.image = self.standing_frames[0]
        self.image.set_colorkey(c.black)
        
        self.walking = False
        self.jumping = False
        self.hurt = False
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
        self.hurt_image = self.game.spritesheet.get_image(382,946,150,174)
        self.hurt_image.set_colorkey(c.black)
         
    def jump(self):
        #Could be moved into the game to avoid referancing game upon init
        self.pos.y += 2
        hits = pg.sprite.spritecollide(self,self.game.platforms,False)
        self.pos.y -= 2
        if hits and not self.jumping:
#            self.game.jump_sound.play()
            self.jumping = True
            self.vel.y = -c.player_jump
            
    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
                
        pass
    
    def animate_frame(self,list_,now,ref):
        if now - self.last_update > ref:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(list_)
            self.image = list_[self.current_frame]
    
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
        elif self.jumping:
            self.image = self.jump_frame
        if self.hurt:
            self.image = self.hurt_image
            
        bot = self.rect.bottom
        self.rect = self.image.get_rect()
        self.rect.bottom = bot
        
        self.mask = pg.mask.from_surface(self.image)    
            
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
        self.groups = game.all_sprites, game.platforms
        self._layer = c.plat_layer
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        images = [self.game.spritesheet.get_image(0,288,380,94),
                  self.game.spritesheet.get_image(213,1662,201,100)]
                  
        self.image = choice(images)
        self.image.set_colorkey(c.black)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if randrange(100) < c.power_spawn:
            Power(self.game,self)
        
class Power(pg.sprite.Sprite):
    def __init__(self,game,plat):
        self.groups = game.all_sprites, game.powerups
        self._layer = c.pow_layer
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.plat = plat
#        self.type = choice(('boost','not boost'))
        self.type = 'boost'
                  
        self.image = self.game.spritesheet.get_image(852,1089,65,77)
        self.image.set_colorkey(c.black)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.y - 5
        
    def update(self):
        self.rect.bottom = self.plat.rect.y - 5
        if not self.game.platforms.has(self.plat):
            self.kill()
            
class Mob(pg.sprite.Sprite):
    def __init__(self,game):
        self.groups = game.all_sprites, game.mobs
        self._layer = c.mob_layer
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image_up = self.game.spritesheet.get_image(566,510,122,139)
        self.image_up.set_colorkey(c.black)
        self.image_down = self.game.spritesheet.get_image(568,1534,122,135)
        self.image_down.set_colorkey(c.black)
        self.image = self.image_up
        self.rect = self.image.get_rect()
        self.rect.centerx = choice([-50,c.width+50])
        self.vx = randrange(2,6)
        if self.rect.x > c.width:
            self.vx *= -1
        self.rect.y = randrange(0,c.height/2)
        self.vy = 0
        self.dy = 0.5
        
    def update(self):
        self.rect.x += self.vx
        self.vy += self.dy
        if self.vy > 3 or self.vy < -3:
            self.dy *= -1
        center = self.rect.center
        if self.dy > 0:
            self.image = self.image_down
        else:
            self.image = self.image_up
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.rect.y += self.vy
        if self.rect.left > c.width + 50 or self.rect.right < -50:
            self.kill()
        self.mask = pg.mask.from_surface(self.image)   
        
class Cloud(pg.sprite.Sprite):
    def __init__(self,game):
        self.groups = game.all_sprites, game.clouds
        self._layer = c.cloud_layer
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image = choice(self.game.cloud_images)
        self.image.set_colorkey(c.black)
        self.rect = self.image.get_rect()
        scale = randrange(50,101)/100.
        self.image = pg.transform.scale(self.image,(int(self.rect.width*scale),
                                                   int(self.rect.height*scale)))
        self.rect.x = randrange(0,c.width-self.rect.width)
        self.rect.y = randrange(-500,-50)
        
    def update(self):
        if self.rect.top > c.height*2:
            self.kill()