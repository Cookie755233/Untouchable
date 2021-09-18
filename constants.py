
import pygame
import numpy as np
import os
from buttons import Button

S_WIDTH = 1200
S_HEIGHT = 800
CELL_SIZE = 40

SCREEN = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
FPS = 60

PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
LIME = (0, 255, 0)
GREEN = (0, 128, 0)
OLIVE = (128, 128, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
MAROON = (128, 0, 0)
SILVER = (230, 230, 230)
GREY = (168, 168, 168)
BLUE = (0, 0, 255)
NAVY = (0, 0, 128)
AQUA = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 192, 203)
COLORS = [PURPLE, TEAL, LIME, GREEN, OLIVE, ORANGE,
          PINK, MAROON, BLUE, AQUA, GREY]

''' 
intro, untouchable, qmark, rules
level_one, level_one_hovered ...

'''
def image_const(name):
    return pygame.image.load(os.path.join('./Assets', f'{name}.png')).convert_alpha()

default_shapes = [[1, 2, 5, 6, 11, 16],
                  [1, 6, 10, 11, 12, 16],
                  [1, 2, 3, 7, 12, 17],
                  [3, 7, 8, 11, 12, 16],
                  [1, 2, 6, 10, 11, 15],
                  [2, 3, 7, 12, 16, 17],
                  [2, 7, 8, 11, 12, 16],
                  [2, 7, 8, 12, 16, 17],
                  [1, 6, 7, 8, 12, 17],
                  [7, 8, 9, 10, 11, 12],
                  [2, 7, 8, 11, 12, 17]]


def get_rotation(default_position):
    zero_arr = np.array([0 for _ in range(25)])
    for p in default_position:
        zero_arr[p] = 1
    matrix = zero_arr.reshape(5, 5)

    output = []
    matrixs = [
        matrix,
        np.rot90(matrix, 1),
        np.rot90(matrix, 2),
        np.rot90(matrix, 3),
        np.fliplr(matrix),
        np.rot90(np.fliplr(matrix), 1),
        np.rot90(np.fliplr(matrix), 2),
        np.rot90(np.fliplr(matrix), 3),
    ]
    num = 0
    while num < 8:
        rotated = []
        for i, array in enumerate(matrixs[num]):
            for j, element in enumerate(array):
                if element == 1:
                    rotated.append(i * len(matrix) + j)
        output.append(rotated)
        num += 1
    return output


shapes_rotation = [get_rotation(i) for i in default_shapes]
TUPLE_POSITION = [[[[x // 5, x % 5] for x in c]
                   for c in i] for i in shapes_rotation]

# levels = width, height, left, top
levels = [
    [9, 17, 120, 60],
    [10, 15, 100, 100],
    [12, 12, 60, 160]
]


shape_pos = [
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
    [900, 600]]
