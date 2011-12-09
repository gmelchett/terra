
import random, os

from utils import Image
from defines import *


class Forest(Image):
    # Jungle - Large
    # Jungle - Large
    # Jungle - Small
    # Jungle - Small
    # Forest - Large
    # Forest - Large
    # Forest - Small
    # Forest - Small
    # Pines
    # Pines
    def __init__(self, image_name, forest_size):
        Image.__init__(self, image_name)
        self.forest_size = forest_size

    def get_image(self, type, feature):
        #yval = random.randint(0, 1)
        #xval = random.randint(0, self.forest_size[type])
        xval = 0
        yval = 0
        return self.surface.subsurface(xval * (FOREST_WIDTH) + (xval+1), yval * (FOREST_HEIGHT)+(yval+1), FOREST_WIDTH, FOREST_HEIGHT)


class ForestFeature:
    def __init__(self):
        self.Forests = NUM_TERRAINS*[None]
        self.Forests[GRASS] = Forest(os.path.join("Art", "Terrain", "grassland forests.pcx"), (4, 4, 6, 6, 4, 4, 5, 5, 6, 6))
        self.Forests[PLAINS] = Forest(os.path.join("Art", "Terrain", "plains forests.pcx"), (0, 0, 5, 5, 5, 5, 6, 6))
        self.Forests[TUNDRA] = Forest(os.path.join("Art", "Terrain", "tundra forests.pcx"), (0, 0, 4, 4, 5, 5, 6, 6))
        
    def get_image(self, terrain_type, feature):
        if feature == JUNGLE or feature == FOREST:
            if self.Forests[terrain_type] is not None:
                return self.Forests[terrain_type].get_image(terrain_type, feature)
        return None
    
        

class Feature:
    def __init__(self):
        self.f = ForestFeature()
    def get_image(self, type, feature):
        return self.f.get_image(type, feature)
    def get_ystride(self):
        return FOREST_HEIGHT
    def get_xstride(self):
        return FOREST_WIDTH

    
