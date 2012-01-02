
import random

import map
from defines import *


class Fractal:
    def __dump(self):
        if self.debug:
            for x in range(0, self.size):
                print self.terrain[x]

    def __xwrap(self, d):
        if d >= self.size:
            return d - self.size + 1
        if d < 0:
            return d - 1
        return d

    def __add_rand(self, avg, rand):
        return max(0, min(255, avg + random.randint(-rand, rand)))

    def __get(self, x, y, s, p):

        if y < 0 or y >= self.size:
            return s, p + 1

        if self.debug:
            print x, "wrapped:", self.__xwrap(x), y, "is", self.terrain[self.__xwrap(x)][y]

        if self.terrain[self.__xwrap(x)][y] is not None:
            return s + self.terrain[self.__xwrap(x)][y], p + 1
        else:
            return s, p

    def __set(self, x, y, val):
        self.histogram[val] += 1
        self.terrain[self.__xwrap(x)][y] = val

    def __square_avg(self, x, y, d, rand):
        s = 0
        p = 0

        s, p = self.__get(x - d, y, s, p)
        s, p = self.__get(x + d, y, s, p)
        s, p = self.__get(x, y + d, s, p)
        s, p = self.__get(x, y - d, s, p)

        if x == 0 or x == self.size or y == 0 or y == self.size:
            return 0
        else:
            return self.__add_rand(s / p, rand)

    def __generate(self, x, y, d, rand):

        # diamond
        s = 0
        p = 0
        s, p = self.__get(x, y, s, p)
        s, p = self.__get(x + d, y, s, p)
        s, p = self.__get(x, y + d, s, p)
        s, p = self.__get(x + d, y + d, s, p)

        self.__set(x + d / 2, y + d / 2, self.__add_rand(s / p, rand))

        # square
        self.__set(self.__xwrap(x), y + d / 2, self.__square_avg(x, y + d/2, d / 2, rand))
        self.__set(self.__xwrap(x + d), y + d / 2,  self.__square_avg(x + d, y + d/2, d / 2, rand))
        self.__set(self.__xwrap(x + d / 2), y, self.__square_avg(x + d / 2, y, d / 2, rand))
        self.__set(self.__xwrap(x + d / 2), y + d, self.__square_avg(x + d / 2, y + d, d /2, rand))

        self.__dump()

    def __init__(self, size = 9, debug=False, update_callback=None):
        self.size = size
        self.terrain = []
        self.histogram = 256 * [0]
        self.debug = debug

        for y in range(0, size):
            l = []
            for x in range(0, size):
                l.append(None)
            self.terrain.append(l)

        self.__set(0, 0, 0)
        self.__set(0, size - 1, 0)
        self.__set(size - 1, 0, 0)
        self.__set(size - 1, size - 1, 0)

        #self.__set(0, 0, random.randint(0, 255))
        #self.__set(0, size - 1, random.randint(0, 255))
        # TODO: Wrap east-west. This is not good enough
        #self.terrain[size - 1][0] = self.terrain[0][0]
        #self.terrain[size - 1][size - 1] = self.terrain[0][size - 1]

        d = size - 1
        l = 1
        rand = 128

        if update_callback:
            update_callback(0, 5)

        while True:
            for m in range(0, l):
                for n in range(0, l):
                    self.__generate(m*d, n*d, d, rand)
            if update_callback:
                update_callback(d, 5)

            if d == 2:
                break
            l = l * 2
            d = d / 2
            # TODO: Parameter
            rand = 65*rand/100
    def getTerrain(self):
        return self.terrain
    def getSize(self):
        return self.size
    def getHistogram(self):
        return self.histogram

class Generate:
    # FIXME: Arguments does not match
    def __init__(self, width, height, numcontinents, continentsize, seed=None):
        if seed is not None:
            random.seed(seed)
        # FIXME: must be power of 2+1
        self.Map = map.Map(width, width)

    def generate(self):
        Frac = Fractal(size=self.Map.width)


        heights = Frac.getHistogram()
        terrain = Frac.getTerrain()

        current_height = 0
        sea_level = None
        land_level = None
        tree_level = None
        hill_level = None
        mountain_level = None

        for i in range(0, 256):
            current_height = current_height + heights[i]
            if current_height >= 80*sum(heights)/100 and sea_level is None:
                sea_level = i
        
            if current_height >= 80*sum(heights)/100 and land_level is None:
                land_level = i
            if current_height >= 87*sum(heights)/100 and tree_level is None:
                tree_level = i
            if current_height >= 96*sum(heights)/100 and hill_level is None:
                hill_level = i
            if current_height >= 98*sum(heights)/100 and mountain_level is None:
                mountain_level = i

        for x in range(0, self.Map.width):
            for y in range(0, self.Map.width):
                if terrain[x][y] < sea_level:
                    self.Map.setTerrainType(x, y, OCEAN)
                elif terrain[x][y] < land_level:
                    self.Map.setTerrainType(x, y, SEA)
                elif terrain[x][y] < tree_level:
                    self.Map.setTerrainType(x, y, GRASS)
                elif terrain[x][y] < hill_level:
                    self.Map.setTerrainType(x, y, GRASS)
                    self.Map.setFeature(x, y, FOREST)
                elif terrain[x][y] < mountain_level:
                    self.Map.setTerrainType(x, y, GRASS)
                else:
                    self.Map.setTerrainType(x, y, GRASS)

        self.Map.neighbourrules(ICE, (ICE, OCEAN), OCEAN)
        self.Map.neighbourrules(GRASS, (GRASS, COAST), COAST)
        self.Map.neighbourrules(COAST, (COAST, GRASS, SEA), SEA)
        self.Map.neighbourrules(SEA, (COAST, SEA, OCEAN), COAST)

        self.Map.neighbourrules(TUNDRA, (TUNDRA, COAST, GRASS), GRASS)
        self.Map.neighbourrules(PLAINS, (PLAINS, DESERT, COAST, GRASS), GRASS)
        self.Map.neighbourrules(DESERT, (DESERT, PLAINS, COAST, GRASS), GRASS)
        self.Map.finalize()

        return self.Map




