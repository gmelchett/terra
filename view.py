
import pygame
from defines import *

class Minimap:
    # FIXME: Just a hack
    def __init__(self, world, surface, x, y, size):
        self.world = world
        self.x = x
        self.y = y
        self.size = size
        self.surface = surface

    def update(self, x, y, w, h):

        for iy in range(0, self.world.world.height):
            for ix in range(0, self.world.world.width):
                t = self.world.world.getTerrainType(ix, iy)
                if t == OCEAN or t == SEA or t == COAST:
                    self.surface.set_at((500+ix, 500+iy), (0,0,255))
                else:
                    self.surface.set_at((500+ix, 500+iy), (128,128,128))

        pygame.draw.rect(self.surface, (255,255,255), pygame.Rect(x+500, y+500, w, h), 1)



class View:
    def __init__(self, world, terrain, feature, surface, tile_width, tile_height, minimap_x=-1, minimap_y=-1, minimap_size=-1):
        self.world = world
        self.terrain = terrain
        self.feature = feature
        self.x = 0
        self.y = 0
        self.changed = False

        self.surface = surface
        self.tile_width = tile_width
        self.tile_height = tile_height

        # Minmap, no border.
        self.minimap = Minimap(world, surface, minimap_x, minimap_y, minimap_size)

    def __verify(self, x, y):
        return x >=0 and x < (self.world.getWidth() - self.tile_width) and y >= 0 and y < (self.world.getHeight() - 2*self.tile_height)

    def locate(self, x, y):
        if self.__verify(x, y):
            self.x = x
            self.y = y
            self.changed = True
    def left(self):
        if self.__verify(self.x-1, self.y):
            self.x -= 1
            self.changed = True
    def right(self):
        if self.__verify(self.x+1, self.y):
            self.x += 1
            self.changed = True
    def up(self):
        if self.__verify(self.x, self.y-1):
            self.y -= 1
            self.changed = True
    def down(self):
        if self.__verify(self.x, self.y+1):
            self.y += 1
            self.changed = True
    def update(self):

        if not self.changed:
            return

        self.changed = False

        ystride = self.terrain.getYStride()
        xstride = self.terrain.getXStride()

        xstep = (TERRAIN_WIDTH*self.tile_width)/xstride+1
        ystep = 2 * (TERRAIN_HEIGHT*self.tile_height) / ystride + 1

	# Draw world
        for y in range(self.y, self.y + ystep):
            l = ""
            for x in range(self.x, self.x + xstep):

                tileimage = self.terrain.getTileImage(self.world, x, y)
                
                if tileimage is not None:
                    screen_x = (x - self.x)*xstride - (xstride / 2) * (y % 2)
                    screen_y = (y - self.y)*ystride - (ystride / 2) - (ystride / 2)* (y - self.y)
                    
                    self.surface.blit(tileimage, (screen_x, screen_y))

	# Draw features

        feature_h = self.feature.get_ystride()
        feature_w = self.feature.get_xstride()

        for y in range(self.y, self.y + ystep):

            for x in range(self.x, self.x + xstep):
                feature = self.world.getFeature(x, y)
                terrain_type = self.world.getTerrainType(x, y)
                
                image = self.feature.get_image(terrain_type, feature)
                if image is not None:
                    screen_x = (x - self.x)*xstride - (xstride/2) * (y % 2) #- abs(feature_w - xstride)/2
                    screen_y = (y - self.y)*ystride - (ystride/2) - (ystride/2)* (y-self.y) #- abs(feature_h - ystride)/2 + ystride/2
                    
                    self.surface.blit(image, (screen_x, screen_y))
                    

        self.minimap.update(self.x, self.y, xstep, ystep)

        pygame.display.flip() 





