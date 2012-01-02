

#import generate
import fractal
import random
from defines import *
from terrainbitmap import *




class World:

    def getWidth(self):
        return self.world.getWidth()

    def getHeight(self):
        return self.world.getHeight()

    def new(self):
        #self.generator = generate.Generate(120, 80, 4, 12, seed = 0)
        self.generator = fractal.Generate(65, 65, 4, 12, seed = 1)
        self.world = self.generator.generate()

        # Create the bit maps needs to figure out which image that is witch.

        for y in range(self.world.getHeight()):
            for x in range(self.world.getWidth()):

                l = NUM_TERRAINS * [0]

                l[self.world.getTerrainType(x, y, EAST)]  = 1
                l[self.world.getTerrainType(x, y, WEST)]  = 1
                l[self.world.getTerrainType(x, y, NORTH)] = 1
                l[self.world.getTerrainType(x, y, SOUTH)] = 1
                l[self.world.getTerrainType(x, y)]  = 1

                if sum(l[1:]) > 3:
                    print l[1:]
                    self.world.display(x, y)
                    print "ERROR: Impossible to find suitable image!"
                    raise

                possiblepicks = {}

                keys = TERRAIN_IMAGES.keys()

                for i in range(1, NUM_TERRAINS):

                    if l[i] > 0:
                        tmpk = []
                        for k in keys:
                            if i in TERRAIN_IMAGES[k]["data"]:
                                tmpk.append(k)
                        keys = tmpk

                # Keys can now be of several length long, but that is only for that like OCEAN next to only OCEANs exists in many images.

                # Hack until ICE is garrantied to be beside OCEAN only
                if len(keys) == 0:
                    print "== Adjusting =="
                    print l
                    print x, y, keys

                    image = TERRAIN_IMAGE_OCEAN
                else:
                    image = keys[0]

                self.world.setImageVal(x, y, image)
                subimage = self.__SelectSubImage(x, y, image)
                self.world.setImageIndex(x, y, subimage)

                

                    

    def load(self, filename):
        pass


    def __eliminate(self, p, p2):
        pout = []
        for y in range(0, 9):
            line = []
            for x in range(0, 9):
                line.append(p[y][x] and p2[y][x])
            pout.append(line)
        return pout

    def __lastone(self, p):
        fx = -1
        fy = -1

        for y in range(0, 9):
            for x in range(0, 9):
                if p[y][x]:
                    if fx != -1 or fy != -1:
                        print "Error More than one imagine left!"
                        pprint.pprint(p)
                    fx = x
                    fy = y

        if fx == -1 or fy == -1:
            return (0, 0)
        else:
            return (fx, fy)

    def __SelectSubImage(self, x, y, image):
        
        p = 9*[9*[True]]

        
        if self.world.getImageVal(x, y) == TERRAIN_IMAGE_ICE:

            x = random.randint(0,7)

            if self.world.getTerrainType(x, y, NORTH) == OCEAN:
                if self.world.getTerrainType(x, y, EAST) == OCEAN:
                    y = 3
                else:
                    y = 2
            else:
                if self.world.getTerrainType(x, y, EAST) == OCEAN:
                    y = 1
                else:
                    y = 0
            return (x, y)


        if self.world.getImageVal(x, y) == TERRAIN_IMAGE_SEA or self.world.getImageVal(x, y) == TERRAIN_IMAGE_OCEAN:
            return (random.randint(0, 8), random.randint(0, 8))


        # Figure out if we are going to use magic 1, 2 or 3

        for k in (EAST, WEST, SOUTH, NORTH):
            for val in range(0,3):
                if self.world.getTerrainType(x, y, k) == TERRAIN_IMAGES[image]["data"][val]:
                    p = self.__eliminate(p, TerrainBitMap[val][k])
                    break
            else:
                return (0, 0)

        # p should now only contain one.
        if len(p) == 0:
            print terrain.imagename
            self.world.display(x, y)
            print "P is broken, it shouldnt"
            return None

        (x, y) = self.__lastone(p)

        return (x, y)


    def getTerrainType(self, x, y):
        return self.world.getTerrainType(x, y)

    def getFeature(self, x, y):
        return self.world.getFeature(x, y)

    def getImageVal(self, x, y):
        return self.world.getImageVal(x, y)
    def getImageIndex(self, x, y):
        return self.world.getImageIndex(x, y)


    def display(self):

        for h in range(0, self.height):
            line = ""
            for w in range(0, self.width):
                if self.map[h][w].type == OCEAN:
                    line += " "
                elif self.map[h][w].type == DESERT:
                    line += "D"
                elif self.map[h][w].type == GRASS:
                    line += "G"
                elif self.map[h][w].type == PLAINS:
                    line +="P"
                elif self.map[h][w].type == COAST:
                    line +="c"
                else:
                    line +="?"
            print line


                                       
                













