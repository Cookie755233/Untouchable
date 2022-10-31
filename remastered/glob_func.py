
import pygame
import os
import numpy as np


def get_image(image_name: str) -> pygame.Surface:
    return pygame.image.load(
        os.path.join('../Assets', f'{image_name}.png')
    ).convert_alpha()


def get_shape_rotations(default_position: list) -> list[list[int]]:
    # Map shape into 5x5 grid
    zero_array = np.zeros(25)
    for p in default_position:
        zero_array[p] = 1
    matrix = zero_array.reshape(5, 5)

    # Create all rotations of a single piece 
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
    
    # Find all the rotations in by its index(x, y) from grid system
    output = []

    # Find all the rotations in grid system(5x5)
    for index in range(8):
        rotated = []
        for i, array in enumerate(matrixs[index]):
            for j, element in enumerate(array):
                if element: 
                    # Find all rotations' index by its position
                    pos = i*len(matrix) + j # position: -> 9
                    x, y = pos//5, pos%5    #   x, y  : -> (1,4)
                    rotated.append((x, y))

        output.append(rotated)
    
    return output

