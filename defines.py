

# Terrain types

NOTHING      = 0
OCEAN        = 1
SEA          = 2
COAST        = 3
DESERT       = 4
PLAINS       = 5
GRASS        = 6
TUNDRA       = 7
ICE          = 8
NUM_TERRAINS = 9

# Just extra
LAND         = 10

# Feature
JUNGLE = 1
FOREST = 2
FLOOD_PLAINS = 3

FOREST_JUNGLE_SMALL = 0
FOREST_JUNGLE_LARGE = 1
FOREST_LARGE = 2
FOREST_SMALL = 3
FOREST_PINES = 4

ICE_SIZE = 1
TUNDRA_SIZE = 15

WEST  = 0
EAST  = 1
SOUTH = 2
NORTH = 3

# Terrain Images:
TERRAIN_IMAGE_SEA                 = 0 # wSSS
TERRAIN_IMAGE_OCEAN               = 1 # wOOO
TERRAIN_IMAGE_ICE                 = 2 # wICE
TERRAIN_IMAGE_COAST_SEA_OCEAN     = 3 # wCSO
TERRAIN_IMAGE_DESERT_GRASS_COAST  = 4 # xDGC
TERRAIN_IMAGE_DESERT_GRASS_PLAINS = 5 # xDGP
TERRAIN_IMAGE_DESERT_PLAINS_COAST = 6 # xDPC
TERRAIN_IMAGE_PLAINS_GRASS_COAST  = 7 # xPGC
TERRAIN_IMAGE_GRASS_GRASS_COAST   = 8 # xPGC
TERRAIN_IMAGE_TUNDRA_GRASS_COAST  = 9 # xPGC
TERRAIN_IMAGE_NUM_OF              = 10


TERRAIN_IMAGES = {TERRAIN_IMAGE_SEA:                 {"data":(SEA,    SEA,    SEA),    "filename":"wSSS.pcx"},
                  TERRAIN_IMAGE_OCEAN:               {"data":(OCEAN,  OCEAN,  OCEAN),  "filename":"wOOO.pcx"},
                  TERRAIN_IMAGE_ICE:                 {"data":(ICE,    ICE,    OCEAN),  "filename":"polarICEcaps-final.pcx"},
                  TERRAIN_IMAGE_COAST_SEA_OCEAN:     {"data":(COAST,  SEA,    OCEAN),  "filename":"wCSO.pcx"},
                  TERRAIN_IMAGE_DESERT_GRASS_COAST:  {"data":(DESERT, GRASS,  COAST),  "filename":"xdgc.pcx"},
                  TERRAIN_IMAGE_DESERT_GRASS_PLAINS: {"data":(DESERT, GRASS,  PLAINS), "filename":"xdgp.pcx"},
                  TERRAIN_IMAGE_DESERT_PLAINS_COAST: {"data":(DESERT, PLAINS, COAST),  "filename":"xdpc.pcx"},
                  TERRAIN_IMAGE_PLAINS_GRASS_COAST:  {"data":(PLAINS, GRASS,  COAST),  "filename":"xpgc.pcx"},
                  TERRAIN_IMAGE_GRASS_GRASS_COAST:   {"data":(GRASS,  GRASS,  COAST),  "filename":"xggc.pcx"},
                  TERRAIN_IMAGE_TUNDRA_GRASS_COAST:  {"data":(TUNDRA, GRASS,  COAST),  "filename":"xtgc.pcx"}
                 }




ALPHA_NUM = 255
TERRAIN_HEIGHT = 64
TERRAIN_WIDTH = 128

FOREST_WIDTH = 127
FOREST_HEIGHT = 87
FOREST_COVER = 0.3 # 30 percent

IsLand = lambda x: x == DESERT or x == PLAINS or x == GRASS or x == TUNDRA
