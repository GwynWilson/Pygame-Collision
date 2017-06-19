# -*- coding: utf-8 -*-
import pygame as pg
import Constants as c

class Collide():
    def __init__(self,game):
        self.game = game
        self.plat_collide = True
        
    def platform_collision(self):
        if self.plat_collide:
            if self.game.player.vel.y > 0:
                hits = pg.sprite.spritecollide(self.game.player,
                                               self.game.platforms,False)
                if hits:
                    lowest = max(hits,key=lambda x: x.rect.y)
                    if self.game.player.pos.x < lowest.rect.right + 5 and \
                        self.game.player.pos.x > lowest.rect.left - 5:
                        if self.game.player.pos.y <= lowest.rect.centery:
                            self.game.player.pos.y = lowest.rect.top + 1
                            self.game.player.vel.y = 0
                            self.game.player.jumping = False
                        
    def mob_collision(self):
        mob_hit = pg.sprite.spritecollide(self.game.player,self.game.mobs,False,
                                          pg.sprite.collide_mask)
        if mob_hit:
            self.plat_collide = False
            self.game.player.hurt = True
            
            for sprite in self.game.all_sprites:
                sprite.rect.y -= self.game.player.vel.y
                if sprite.rect.top < 0:
                    sprite.kill()
            
    def pow_collision(self):
        pow_hits = pg.sprite.spritecollide(self.game.player,self.game.powerups,True)
        for power in pow_hits:
            if power.type == 'boost':
                self.game.player.vel.y = -c.boost_power
                self.game.player.jumping = False