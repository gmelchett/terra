#!/usr/bin/env python
import pygame, time, sys 

import fractal

s = 257

d = fractal.Fractal(size=s)
terrain = d.get_terrain();
pygame.init()

pygame.display.set_mode((s, s))
surface = pygame.display.get_surface()


for x in range(0, s):
    for y in range(0, s):
        surface.fill((terrain[x][y],
                      terrain[x][y],
                      terrain[x][y]),
                     ((x,y), (x,y)))

pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    time.sleep(0.1)
