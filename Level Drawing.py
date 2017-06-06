# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 13:51:20 2017

@author: GWils
"""

import pygame

black = (0,0,0)
white = (255,255,255)

pygame.init()
pygame.display.set_caption('Im Trying to draw a level')
clock = pygame.time.Clock()
scr = pygame.display.set_mode((320,240))
block_size = 16
blocks = []

class Block():
    def __init__(self,pos):
        blocks.append(self)
        self.rect = pygame.Rect(pos[0],pos[1],block_size,block_size)

#blocks.append(Block((0,0)))

level =['wwwwwwwwwwwwwwwwwwww',
        'w w                w',
        'wwwwwwwwwwwwwwwwwwww',
        'w     w            w',
        'wwwwwwwwwwwwwwwwwwww',
        'w        w         w',
        'wwwwwwwwwwwwwwwwwwww',
        'w      w           w',
        'wwwwwwwwwwwwwwwwwwww',
        'w               w  w',
        'wwwwwwwwwwwwwwwwwwww',
        'w            w     w',
        'wwwwwwwwwwwwwwwwwwww',
        'w         w        w',
        'wwwwwwwwwwwwwwwwwwww']
x = y =0
for row in level:
    for col in row:
        if col == 'w':
            Block((x,y))
        x += 16
    y += 16
    x = 0
        
running = True
while running:
    
    clock.tick(60)
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    scr.fill(black)
    for b in blocks:
        pygame.draw.rect(scr,white,b.rect)
    pygame.display.update()
    
            
pygame.quit()
quit()