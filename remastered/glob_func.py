
from pygame import image
import os
import numpy as np


def get_image(image_name):
    return image.load(
        os.path.join('../Assets', f'{image_name}.png')
    ).convert_alpha()


def get_shape_rotations(default_position):
    
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
    
    #
    output = []
    
    for i, array in enumerate(matrixs[num]):
        for j, element in enumerate(array):
            if element == 1:
                rotated.append( i*len(matrix) + j )
                
    
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
