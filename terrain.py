
import pygame
import os
import pprint, random

from defines import *
from utils import Image


class TerrainImage(Image):
    def __init__(self, image_name):
        Image.__init__(self, image_name)
        self.size = (TERRAIN_WIDTH, TERRAIN_HEIGHT)
        self.items = (self.surface.get_width()/self.size[0], self.surface.get_height()/self.size[1])

class Terrain:
    def __init__(self):

        self.Images = []

        for k in TERRAIN_IMAGES.keys():
            self.Images.append(TerrainImage(os.path.join("Art", "Terrain", TERRAIN_IMAGES[k]["filename"])))

    def getYStride(self):
        # Ugly hack.
        return TERRAIN_HEIGHT
    def getXStride(self):
        return TERRAIN_WIDTH                                                

    def getTileImage(self, world, x, y):

        terrain = self.Images[world.getImageVal(x, y)]
        (x, y) = world.getImageIndex(x, y)

        if terrain is not None:
            return terrain.surface.subsurface((x*TERRAIN_WIDTH, y*TERRAIN_HEIGHT , TERRAIN_WIDTH, TERRAIN_HEIGHT))
        else:
            return None




        
                                    

