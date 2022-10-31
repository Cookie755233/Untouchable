
from webbrowser import get
from glob_func import get_image, get_shape_rotations


# <-- Display Settings --->
S_WIDTH = 1200
S_HEIGHT = 800
CELL_SIZE = 40

FPS = 60

# <--- Colour Config --->
RED    = (255,   0,   0)
TEAL   = (  0, 128, 128)
LIME   = (  0, 255,   0)
GREY   = (168, 168, 168)
BLUE   = (  0,   0, 255)
NAVY   = (  0,   0, 128)
AQUA   = (  0, 255, 255)
PINK   = (255, 192, 203)
WHITE  = (255, 255, 255)
GREEN  = (  0, 128,   0)
OLIVE  = (128, 128,   0)
BLACK  = (  0,   0,   0)
PURPLE = (128,   0, 128)
ORANGE = (255, 165,   0)
MAROON = (128,   0,   0)
SILVER = (230, 230, 230)
COLORS = [PURPLE, TEAL, LIME, GREEN, OLIVE,
          ORANGE, PINK, MAROON, BLUE, AQUA, GREY]


# <--- Shapes --->
SHAPES = [
    [1,  2,  5,   6,  11,  16],
    [1,  6, 10,  11,  12,  16],
    [1,  2,  3,   7,  12,  17],
    [3,  7,  8,  11,  12,  16],
    [1,  2,  6,  10,  11,  15],
    [2,  3,  7,  12,  16,  17],
    [2,  7,  8,  11,  12,  16],
    [2,  7,  8,  12,  16,  17],
    [1,  6,  7,   8,  12,  17],
    [7,  8,  9,  10,  11,  12],
    [2,  7,  8,  11,  12,  17]
]

SHAPE_POSITIONS = [get_shape_rotations(i) for i in SHAPES]

#! <--- Levels ---> This is weird.
# [width, height, left, top]
LEVELS = [
    [9, 17, 120, 60],
    [10, 15, 100, 100],
    [12, 12, 60, 160]
]

SHAPE_POS = [
    [610, 50],
    [820, 50],
    [980, 50],
    [610, 250],
    [820, 250],
    [980, 250],
    [610, 450],
    [820, 450],
    [980, 450],
    [690, 600],
    [900, 600]
]
