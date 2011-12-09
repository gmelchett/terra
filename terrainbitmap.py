
#
# This bitmap calculates which image that shall be used from the x-terrain
# files. 
#
# Example, if the tile is Grass and neighbors to plains and desert,
# xDGP, 1=D, 2=G, 3=P
# The look west, east, south, north for a single possible tile.


TerrainBitMap = [
    # Selection 0
    [
    # west
    [[True,  True,  True,  False, False, False, False, False, False],
     [True,  True,  True,  False, False, False, False, False, False],
     [True,  True,  True,  False, False, False, False, False, False],
     [True,  True,  True,  False, False, False, False, False, False],
     [True,  True,  True,  False, False, False, False, False, False],
     [True,  True,  True,  False, False, False, False, False, False],
     [True,  True,  True,  False, False, False, False, False, False],
     [True,  True,  True,  False, False, False, False, False, False],
     [True,  True,  True,  False, False, False, False, False, False]],
    # east
    [[True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False]],
    # south
    [[True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False]],
    # north
    [[True,  False, False, True,  False, False, True,  False, False],
     [True,  False, False, True,  False, False, True,  False, False],
     [True,  False, False, True,  False, False, True,  False, False],
     [True,  False, False, True,  False, False, True,  False, False],
     [True,  False, False, True,  False, False, True,  False, False],
     [True,  False, False, True,  False, False, True,  False, False],
     [True,  False, False, True,  False, False, True,  False, False],
     [True,  False, False, True,  False, False, True,  False, False],
     [True,  False, False, True,  False, False, True,  False, False]]],
    # Selection 1
    [
    # west
    [[False, False, False, True,  True,  True,  False, False, False],
     [False, False, False, True,  True,  True,  False, False, False],
     [False, False, False, True,  True,  True,  False, False, False],
     [False, False, False, True,  True,  True,  False, False, False],
     [False, False, False, True,  True,  True,  False, False, False],
     [False, False, False, True,  True,  True,  False, False, False],
     [False, False, False, True,  True,  True,  False, False, False],
     [False, False, False, True,  True,  True,  False, False, False],
     [False, False, False, True,  True,  True,  False, False, False]],
    # east
    [[False, False, False, False, False, False, False, False, False],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [False, False, False, False, False, False, False, False, False]],
    # south
    [[False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False]],
    # north
    [[False, True,  False, False, True,  False, False, True,  False],
     [False, True,  False, False, True,  False, False, True,  False],
     [False, True,  False, False, True,  False, False, True,  False],
     [False, True,  False, False, True,  False, False, True,  False],
     [False, True,  False, False, True,  False, False, True,  False],
     [False, True,  False, False, True,  False, False, True,  False],
     [False, True,  False, False, True,  False, False, True,  False],
     [False, True,  False, False, True,  False, False, True,  False],
     [False, True,  False, False, True,  False, False, True,  False]]],
    # Section 2
    [
    # west
    [[False, False, False, False, False, False, True,  True,  True ],
     [False, False, False, False, False, False, True,  True,  True ],
     [False, False, False, False, False, False, True,  True,  True ],
     [False, False, False, False, False, False, True,  True,  True ],
     [False, False, False, False, False, False, True,  True,  True ],
     [False, False, False, False, False, False, True,  True,  True ],
     [False, False, False, False, False, False, True,  True,  True ],
     [False, False, False, False, False, False, True,  True,  True ],
     [False, False, False, False, False, False, True,  True,  True ]],
    # east
    [[False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ]],
    # south
    [[False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [False, False, False, False, False, False, False, False, False],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ],
     [True,  True,  True,  True,  True,  True,  True,  True,  True ]],
    # north
    [[False, False, True,  False, False, True,  False, False, True ],
     [False, False, True,  False, False, True,  False, False, True ],
     [False, False, True,  False, False, True,  False, False, True ],
     [False, False, True,  False, False, True,  False, False, True ],
     [False, False, True,  False, False, True,  False, False, True ],
     [False, False, True,  False, False, True,  False, False, True ],
     [False, False, True,  False, False, True,  False, False, True ],
     [False, False, True,  False, False, True,  False, False, True ],
     [False, False, True,  False, False, True,  False, False, True ]]
    ]
]
