
import random, math, sys, time
import pygame

import map
from defines import *

# Kinda messy, but does the job.

class Area:
    def __init__(self, Map, MinDots, MaxDots, x=None, y=None):
        if x is None:
            self.x = random.randint(5, Map.getWidth() - 5)
        else:
            self.x = x
            
        if y is None:
            self.y = random.randint(ICE_SIZE+10, Map.getHeight() - (ICE_SIZE+10))
        else:
            self.y = y
            
        self.__average_dots = int(random.gauss(float(MaxDots - MinDots), float(MaxDots - MinDots)/2)+ MinDots)

    def generate(self, Map, size, delta=0):
        xys = []

        start = random.randint(0, 359)

        for i in range(start, 360 + start, 360/self.__average_dots):
            d = random.gauss(size, size/4) + delta
            x = int(self.x + d * math.sin(math.radians(i)))
            y = int(self.y + d * math.cos(math.radians(i)))
            
            xys.append((Map.validate(x=x), Map.validate(y=y)))

        return xys



class Continent(Area):

    def __init__(self, Map, MinDots, MaxDots, ContinentSize):
        Area.__init__(self, Map,MinDots, MaxDots)
        self.continentarea = self.generate(Map, ContinentSize)
        self.continentcoast = self.generate(Map, ContinentSize, delta=3)
        self.continentsockel = self.generate(Map, ContinentSize, delta=6)


class SeaTop(Area):
    def __init__(self, Map, MinDots, MaxDots, size):
        Area.__init__(self, Map, MinDots, MaxDots)
        self.area = self.generate(Map, size)



class Generate:
    def __init__(self, width, height, numcontinents, continentsize, seed=None):
        if seed is not None:
            random.seed(seed)

        self.NumContinents = numcontinents

        self.Map = map.Map(width, height)

        self.MinDots = 5
        self.MaxDots = 20
        self.ContinentSize = continentsize

        self.NumSeaTops = random.randint(1, 5)
        self.NumCoastTops = random.randint(1, 5)
        self.SeaTopSize = 8
        self.CoastTopSize = 4
        self.SeaMinDots = 4
        self.SeaMaxDots = 9
        self.NumTinyIles = 4


    def __fillcore(self, x, y):
        if not self.Map.isValid(x, y):
            return

        #print x, y, "valid:", self.Map.isvalid(x, y)

        if self.Map.isMarked(x, y):
            return

        #print "type", self.Map.getTerrainType(x,y), "marked", self.Map.isMarked(x, y)

        self.Map.setMark(x, y, True)

        self.__fillcore(x-1, y)
        self.__fillcore(x+1, y)
        self.__fillcore(x, y-1)
        self.__fillcore(x, y+1)


    def fill(self, x, y, type, land):

        self.__fillcore(x,y)
        
        # Finalize fill
        self.Map.fillMark(type, land)

    def createarea(self, area, center_x, center_y, type, land=False):
        """ Draw the lines between the different dots generated for a continent/sea/coast area. Finalize with filling."""
        
        prevx = prevy = -1
        for xy in area:
            if prevx != -1:
                self.drawinterpolline((prevx, prevy), (xy[0], xy[1]))
            else:
                startx = xy[0]
                starty = xy[1]

            prevx = xy[0]
            prevy = xy[1]

        self.drawinterpolline((startx, starty), (xy[0], xy[1]))
            
        self.fill(center_x, center_y, type, land)


    def generate(self):

        self.Continents = []
        self.TinyIles = []
        self.SeaTops = []
        self.CoastTops = []

        for i in range(self.NumContinents):
            self.Continents.append(Continent(self.Map, self.MinDots, self.MaxDots, self.ContinentSize))

        for i in range(random.randint(0, self.NumTinyIles)):
            self.Continents.append(Continent(self.Map, self.MinDots/2, self.MaxDots/2, 2))

        # Draw the areas
        for c in self.Continents:
            self.createarea(c.continentsockel, c.x, c.y, SEA)

        for c in self.Continents:
            self.createarea(c.continentcoast, c.x, c.y, COAST)

        for c in self.Continents:
            self.createarea(c.continentarea, c.x, c.y, GRASS)

        for i in range(self.NumSeaTops):
            self.SeaTops.append(SeaTop(self.Map, self.SeaMinDots, self.SeaMaxDots, self.SeaTopSize))

        for i in range(self.NumCoastTops):
            self.CoastTops.append(SeaTop(self.Map, self.SeaMinDots, self.SeaMaxDots, self.CoastTopSize))

        for s in self.SeaTops:
            self.createarea(s.area, s.x, s.y, SEA)

        for s in self.CoastTops:
            self.createarea(s.area, s.x, s.y, COAST)


        
        self.Map.neighbourrules(ICE, (ICE, OCEAN), OCEAN)
        self.Map.neighbourrules(GRASS, (GRASS, COAST), COAST)
        self.Map.neighbourrules(COAST, (COAST, GRASS, SEA), SEA)
        self.Map.neighbourrules(SEA, (COAST, SEA, OCEAN), COAST)



        # Place desert and plains.

        for c in self.Continents:
            y = c.y+random.randint(0,10) - 5
            if y > int(self.Map.getHeight()*0.3) and y < int(self.Map.getHeight()*0.7):
                for athempts in range(random.randint(0,4)):
                    d = Area(self.Map, self.MinDots/2, self.MaxDots/2, c.x+random.randint(0,10) - 5, y)
                    area = d.generate(self.Map, random.randint(1, 6))
                    self.createarea(area, d.x, d.y, PLAINS, land=True)
        

        for c in self.Continents:
            y = c.y+random.randint(0,10) - 5
            if y > int(self.Map.getHeight()*0.35) and y < int(self.Map.getHeight()*0.65):
                for athempts in range(random.randint(0,4)):
                    d = Area(self.Map, self.MinDots/2, self.MaxDots/2, c.x+random.randint(0,10) - 5, y)
                    area = d.generate(self.Map, random.randint(1, 5))
                    self.createarea(area, d.x, d.y, DESERT, land=True)


        # Put Ice
        

        for x in range(self.Map.getWidth()):
            for i in range(ICE_SIZE):
                self.Map.setTerrainType(x, i, ICE)
                self.Map.setTerrainType(x, self.Map.getHeight() - i - 1, ICE)

            

        # Fullfill the graphics rules.
        # if current is land, then everything else must be coast or land


        #
        # -- Combinations --
        #
        # CoastSeaOcean
        # OceanOceanOcean
        # SeaSeaSea
        # DesertGrassCoast
        # DesertGrassPlains
        # DesertPlainsCoast
        # GrassGrassCoast
        # PlainsGrassCoast
        # TundraGrassCoast

        #
        # Water: Ocean, Sea, Coast
        # Land:  Desert, Plains, Grass, Tundra
        # Ice:

        # Ice    - Ocean,                             ** Land, Sea, Coast -> Ocean 
        # Ocean  - Coast, Sea,                        ** Land -> Sea
        # Sea    - Ocean, Coast,                      ** Land -> Coast
        # Coast  - Sea, Desert, Grass, Plains, Tundra ** Ocean -> Sea
        # Desert - Grass, Plains, Coast               ** Ocean, Sea -> Coast, Tundra->Grass
        # Plains - Grass, Desert, Coast               ** Ocean, Sea -> Coast, Tundra->Grass
        # Grass  - Plains, Desert, Tundra, Coast      ** Ocean, Sea -> Coast
        # Tundra - Grass, Coast                       ** Ocean, Sea -> Coast, Desert, Plains -> Grass


        # Put grass where needed.
        self.Map.neighbourrules(TUNDRA, (TUNDRA, COAST, GRASS), GRASS)
        self.Map.neighbourrules(PLAINS, (PLAINS, DESERT, COAST, GRASS), GRASS)
        self.Map.neighbourrules(DESERT, (DESERT, PLAINS, COAST, GRASS), GRASS)




        # Add tundra.
        tundrasize = self.Map.getHeight() * TUNDRA_SIZE/100
        for i in range(tundrasize):
            for x in range(self.Map.getWidth()):
                for y in (i, self.Map.getHeight() - i - 1):
                    if self.Map.getTerrainType(x, y) == GRASS:
                        d = tundrasize - y
                        if (d < 4 and random.randint(0,3) < d) or d > 3:
                            self.Map.setTerrainType(x, y, TUNDRA)


        self.Map.finalize()

        # 30% forests.
        grass_size = self.Map.getTerrainSize(GRASS)
        forest_size = int(grass_size * FOREST_COVER)
        print "Planting %d forests of %d" % (forest_size, grass_size)
        for i in range(forest_size):
            notfound = True
            attempts = 0
            while notfound and attempts < 100:
                j = random.randint(0, grass_size-1)
                if not self.Map.hasTerrainLocation(GRASS, j, FOREST) and \
                        self.Map.canHaveForest(GRASS, j):
                    print "Set forest at", j
                    self.Map.setTerrainList(GRASS, j, FOREST)
                    notfound = False
                attempts += 1

        return self.Map


    def cosinterpol(self, a, b, x):
        f = (1 - math.cos(math.pi*x)) * 0.5
        return  int(a*(1 - f) + b*f)

    def drawinterpolline(self, start_xy, end_xy):

        dx = end_xy[0] - start_xy[0]
        dy = end_xy[1] - start_xy[1]

        self.Map.setMark(end_xy[0], end_xy[1], True)

        if dx != 0 and dy != 0:
            lastyi = start_xy[1]
            for xi in range(start_xy[0], start_xy[0] + dx, dx/(abs(dx))):
                yi = int(self.cosinterpol(start_xy[1],
                                          end_xy[1], 
                                          float(xi - start_xy[0]) / float(dx)))
                if lastyi != yi:
                    for y in range(yi, lastyi, (lastyi - yi)/abs(lastyi - yi)):

                        self.Map.setMark(xi, y, True)
                else:
                    self.Map.setMark(xi, yi, True)
                lastyi = yi

            if lastyi != end_xy[1]:
                for y in range(lastyi, end_xy[1], (end_xy[1] - lastyi)/abs(end_xy[1] - lastyi)):
                    self.Map.setMark(xi, y, True)
                
        elif dx == 0 and dy != 0:
            for y in range(start_xy[1], start_xy[1]+dy, dy/abs(dy)):
                self.Map.setMark(start_xy[0], y, True)

        elif dx != 0 and dy == 0:
            for x in range(start_xy[0], start_xy[0]+dx, dx/abs(dx)):
                self.Map.setMark(x, start_xy[1], True)



    def draw(self):
        pygame.init()
        pygame.display.set_mode((120*2, 80*2))
        surface = pygame.display.get_surface()

        for y in range(self.Map.getHeight()):
            for x  in range(self.Map.getWidth()):
                if self.Map.getTerrainType(x, y) == SEA:
                    pygame.draw.line(surface, (50, 50, 150), (x, y), (x, y))
                elif self.Map.getTerrainType(x, y) == OCEAN:
                    pygame.draw.line(surface, (0,0,100), (x, y), (x, y))
                elif self.Map.getTerrainType(x, y) == COAST:
                    pygame.draw.line(surface, (0,100,200), (x, y), (x, y))
                elif self.Map.getTerrainType(x, y) == GRASS:
                    pygame.draw.line(surface, (0,200,100), (x, y), (x, y))
                elif self.Map.getTerrainType(x, y) == DESERT:
                    pygame.draw.line(surface, (255,255,0), (x, y), (x, y))
                elif self.Map.getTerrainType(x, y) == PLAINS:
                    pygame.draw.line(surface, (200,200,100), (x, y), (x, y))
                else:
                    pygame.draw.line(surface, (255,0,0), (x, y), (x, y))
        pygame.display.flip() 


if __name__ == "__main__":
    g = Generate(120, 80, 4, 12, seed = 0)
    g.generate()
    g.draw()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        time.sleep(0.1)



        
