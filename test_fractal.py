#!/usr/bin/env python
import pygame, time, sys 
from pprint import pprint

import fractal

def update_callback(c, l):
        sys.stdout.write("*")
        sys.stdout.flush()

s = 256+1

d = fractal.Fractal(size=s, debug=False, update_callback=update_callback)
terrain = d.getTerrain()

#pprint(terrain)

#sys.exit(0)

h = d.getHistogram()

a = 0
sea_level = None
land_level = None
tree_level = None
hill_level = None
mountain_level = None
for i in range(0, 256):
    a = a + h[i]
    if a >= 80*sum(h)/100 and sea_level is None:
        sea_level = i

    if a >= 80*sum(h)/100 and land_level is None:
        land_level = i
    if a >= 87*sum(h)/100 and tree_level is None:
        tree_level = i
    if a >= 96*sum(h)/100 and hill_level is None:
        hill_level = i
    if a >= 98*sum(h)/100 and mountain_level is None:
        mountain_level = i
print


pygame.init()

pygame.display.set_mode((s*2, s*2))
surface = pygame.display.get_surface()

surface.fill((255,0,0), ((0, 0), (s*2,s*2)))


for x in range(0, s):
    for y in range(0, s):
        if 1:
	    if terrain[x][y] < sea_level:
                c = (0, 0, 255)
            elif terrain[x][y] < land_level:
                c = (128, 0, 255)
            elif terrain[x][y] < tree_level:
                c = (0, 255, 128)
            elif terrain[x][y] < hill_level:
                c = (0, 170, 0)
            elif terrain[x][y] < mountain_level:
                c = (170, 170, 170)
            else:
                c = (255, 255, 255)

        else:
            c = (terrain[x][y], terrain[x][y], terrain[x][y])

        if x >= s/2:
            mx = x - s/2
        else:
            mx = x + s/2

        surface.set_at((mx,y), c)

pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    time.sleep(0.1)
