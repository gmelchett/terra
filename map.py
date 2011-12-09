
from defines import *


class MapItem:
    def __init__(self, terrain_type, feature):
        self.feature            = feature
        self.marked             = False
        self.terrain_type       = terrain_type
        self.terrain_type_east  = terrain_type
        self.terrain_type_west  = terrain_type
        self.terrain_type_north = terrain_type
        self.terrain_type_south = terrain_type

        self.image_index        = None
        self.image_val          = None


    def isLand(self):
        return self.terrain_type == DESERT or self.terrain_type == PLAINS or self.terrain_type == GRASS or self.terrain_type == TUNDRA
    

    def setTerrainType(self, val, name=None):

        if name is None:
            self.terrain_type       = val
        elif name == WEST:
            self.terrain_type_west  = val
        elif name == EAST:
            self.terrain_type_east  = val
        elif name == SOUTH:
            self.terrain_type_south = val
        elif name == NORTH:
            self.terrain_type_north = val
        else:
            raise
            
    def getTerrainType(self, name=None):

        if name is None:
            return self.terrain_type
        elif name == WEST:
            return self.terrain_type_west
        elif name == EAST:
            return self.terrain_type_east
        elif name == NORTH:
            return self.terrain_type_north
        elif name == SOUTH:
            return self.terrain_type_south
        else:
            return None


    def setFeature(self, what):
        if what != NOTHING:
            print "feature", what
        self.feature = what
    def getFeature(self):
        return self.feature

    def setImageIndex(self, val):
        self.image_index = val
    def getImageIndex(self):
        return self.image_index

    def setImageVal(self, val):
        self.image_val = val
    def getImageVal(self):
        return self.image_val


    def setMark(self, val):
        self.marked = val
    def isMarked(self):
        return self.marked


    ### DEBUG ###

    def display(self):
        print " " + self.__ptype(self.terrain_type_north) + " "
        print self.__ptype(self.terrain_type_west) + self.__ptype(self.terrain_type) + self.__ptype(self.terrain_type_east)
        print " " + self.__ptype(self.terrain_type_south) +  " "

    def __ptype(self, t):
        if t == OCEAN:
            return "_"
        if t == GRASS:
            return "g"
        if t == PLAINS:
            return "p"
        if t == DESERT:
            return "d"
        if t == COAST:
            return "c"
        if t == SEA:
            return "-"
        if t == ICE:
            return "."
        if t == TUNDRA:
            return "*"
        if t == NOTHING:
            return "?"

        print "Error:", t
        return "?"
    
    def TerrainType(self):
        return self.__ptype(self.terrain_type)



class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.World = []
        self.TerrainLocations = []
        
        # This list keeps track of all the terrain types in the map. Useful for randomizing features at the right spot.
        for i in range(NUM_TERRAINS):
            self.TerrainLocations.append({})

        for y in range(self.height):
            mapline = []
            for x  in range(self.width):
                mapline.append(MapItem(OCEAN, NOTHING))
                self.__SetToTerrainList(x, y, OCEAN)
            self.World.append(mapline)
            

    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    
    def isValid(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height
    

    def validate(self, x=None, y=None):
        """ This is called when generating a map. Since we have ice an only ocean is allowed to neighbour ice, top and bottom on is -4"""
        if x is not None:
            if x >= self.width - 4:
                x = self.width - 4
            if x < 4:
                x = 4
            return x
        if y is not None:
            if y > self.height - (ICE_SIZE+6):
                y = self.height - (ICE_SIZE+6)
            if y < (ICE_SIZE+6):
                y = ICE_SIZE+6
            return y
        return None
        

    def setImageIndex(self, x, y, val):
        if self.isValid(x, y):
            self.World[y][x].setImageIndex(val)

    def getImageIndex(self, x, y):
        if self.isValid(x, y):
            return self.World[y][x].getImageIndex()
        else:
            return None


    def setImageVal(self, x, y, val):
        if self.isValid(x,y):
            self.World[y][x].setImageVal(val)

    def getImageVal(self,x,y):
        if self.isValid(x,y):
            return self.World[y][x].getImageVal()
        else:
            return None

    def __CalcKey(self, x, y):
        return y*10000+x

    def __RemoveFromTerrainList(self, x, y):
        prevterrain = self.World[y][x].getTerrainType()
        if prevterrain != NOTHING:
            del self.TerrainLocations[prevterrain][self.__CalcKey(x, y)]

    
    def __SetToTerrainList(self, x, y, terraintype):
        self.TerrainLocations[terraintype][self.__CalcKey(x, y)] = (x, y)


    def setTerrainType(self, x, y, val):

        self.__SetChanged()

        if not self.isValid(x, y):
            return

        self.__RemoveFromTerrainList(x, y)
        self.__SetToTerrainList(x, y, val)

        self.World[y][x].setTerrainType(val)

        if self.isValid(x-1, y):
            self.World[y][x-1].setTerrainType(val, EAST)
        else:
            self.World[y][x].setTerrainType(NOTHING, WEST)

        if self.isValid(x+1, y):
            self.World[y][x+1].setTerrainType(val, WEST)
        else:
            self.World[y][x].setTerrainType(NOTHING, EAST)

        if self.isValid(x, y-1):
            self.World[y-1][x].setTerrainType(val, SOUTH)
        else:
            self.World[y][x].setTerrainType(NOTHING, NORTH)

        if self.isValid(x, y+1):
            self.World[y+1][x].setTerrainType(val, NORTH)
        else:
            self.World[y][x].setTerrainType(NOTHING, SOUTH)


    def getTerrainType(self, x, y, name=None):
        if self.isValid(x, y):
            return self.World[y][x].getTerrainType(name)
        else:
            return NOTHING
            

    def isLand(self, x, y):
        return self.World[y][x].isLand()


    def setMark(self, x, y, val):
        self.World[y][x].setMark(val)

    def isMarked(self, x, y):
        return self.World[y][x].isMarked()

    def fillMark(self, val, land):
        for y in range(self.height):
            for x in range(self.width):
                if self.isMarked(x, y):
                    self.setMark(x, y, False)
                    if land == False or self.isLand(x,y):
                        self.setTerrainType(x, y, val)

    def getTerrainSize(self, type):
        return len(self.TerrainLocations[type])
    
    def hasTerrainLocation(self, type, location, what):
        k = self.TerrainLocations[type].keys()[location]
        (x, y) = self.TerrainLocations[type][k]
        return self.getFeature(x, y) == what

    def canHaveForest(self, type, location):
        k = self.TerrainLocations[type].keys()[location]
        (x, y) = self.TerrainLocations[type][k]
        # Only possible to have forest if three of four corners
        # are land
        s = 0
        if IsLand(self.getTerrainType(x, y, NORTH)):
            s += 1
        if IsLand(self.getTerrainType(x, y, SOUTH)):
            s += 1
        if IsLand(self.getTerrainType(x, y, WEST)):
            s += 1
        if IsLand(self.getTerrainType(x, y, EAST)):
            s += 1
        return s >= 3

    def setTerrainList(self, type, location, what):
        k = self.TerrainLocations[type].keys()[location]
        (x, y) = self.TerrainLocations[type][k]
        self.setFeature(x, y, what)

    def getFeature(self, x, y):
        return self.World[y][x].getFeature()

    def setFeature(self, x, y, what):
        self.World[y][x].setFeature(what)
                    
    def __exchange(self, x, y, oks, val):


        if self.isValid(x, y-1) and self.getTerrainType(x, y, NORTH) not in oks:
            self.setTerrainType(x, y-1, val)

        if self.isValid(x-1, y) and self.getTerrainType(x, y, WEST) not in oks:
            self.setTerrainType(x-1, y, val)

        if self.isValid(x+1, y) and self.getTerrainType(x, y, EAST) not in oks:
            self.setTerrainType(x+1, y, val)

        if self.isValid(x, y+1) and self.getTerrainType(x, y, SOUTH) not in oks:
            self.setTerrainType(x, y+1, val)



        if self.isValid(x-1, y-1) and self.getTerrainType(x-1,y-1) not in oks:
            self.setTerrainType(x-1, y-1, val)
        if self.isValid(x-1, y+1) and self.getTerrainType(x-1,y+1) not in oks:
            self.setTerrainType(x-1, y+1, val)
        if self.isValid(x+1, y+1) and self.getTerrainType(x+1,y+1) not in oks:
            self.setTerrainType(x+1, y+1, val)
        if self.isValid(x+1, y-1) and self.getTerrainType(x+1,y-1) not in oks:
            self.setTerrainType(x+1, y-1, val)

        if self.isValid(x, y-2) and self.getTerrainType(x,y-2) not in oks:
            self.setTerrainType(x, y-2, val)
        if self.isValid(x, y+2) and self.getTerrainType(x,y+2) not in oks:
            self.setTerrainType(x, y+2, val)


    def neighbourrules(self, type, oks, newval):
        # Fix name
        """ Make sure that the neighbour likes each other """
        self.__SetChanged()
        while self.__IsChanged():
            self.__ClearChanged()
            for y in range(self.height):
                for x in range(self.width):
                    if self.getTerrainType(x, y) == type:
                        self.__exchange(x, y, oks, newval)
    def __SetChanged(self):
        self.__changed = True
    def __ClearChanged(self):
        self.__changed = False
    def __IsChanged(self):
        return self.__changed


    def finalize(self):

        # FIXME: Edges.
        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):

                dw = (y - 1) % 2

                l = NUM_TERRAINS  * [0]
                l[self.getTerrainType(x,      y    )] += 1
                l[self.getTerrainType(x + dw, y - 1)] += 1
                l[self.getTerrainType(x + 1,  y    )] += 1
                l[self.getTerrainType(x + dw, y + 1)] += 1

                key = 0
                val = 0
                
                for i in range(NUM_TERRAINS):
                    if l[i] > val:
                        key = i
                        val = l[i]
                        
                self.World[y  ][x   ].setTerrainType(key, EAST)
                self.World[y  ][x+1 ].setTerrainType(key, WEST)
                self.World[y+1][x+dw].setTerrainType(key, NORTH)
                self.World[y-1][x+dw].setTerrainType(key, SOUTH)


    def display(self, x, y):
        if self.isValid(x, y):
            self.World[y][x].display()




        

        
