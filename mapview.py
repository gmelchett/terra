#!/usr/bin/env python

import pygame
import os, time, sys

import world
import terrain
import view
import feature

from defines import *

pygame.init()

# Set running directory.
if os.path.dirname( __file__ ):
    os.chdir( os.path.dirname( __file__ ) )
 

w = world.World()
w.new()

pygame.display.set_caption("Map")
window = pygame.display.set_mode((TERRAIN_WIDTH*12, TERRAIN_HEIGHT*14))
screen = pygame.display.get_surface()

t = terrain.Terrain()

f = feature.Feature()

v = view.View(w, t, f, screen, 12, 14)

v.locate(10,10)
v.update()

pygame.display.flip() 

while 1:

    event = pygame.event.wait()
    if event.type == pygame.QUIT: 
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            v.left()
        if event.key == pygame.K_RIGHT:
            v.right()
        if event.key == pygame.K_UP:
            v.up()
        if event.key == pygame.K_DOWN:
            v.down()
            
        v.update()




