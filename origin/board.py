
from constants import *

class MainBoard:
    def __init__(self, width, height, left, top, inner_color, outer_color, lines):
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.inner_color = inner_color
        self.outer_color = outer_color
        self.lines = lines
        self.rotation = 0
        self.cell_size = CELL_SIZE

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(SCREEN, self.inner_color,
                                     (
                                         self.left + j * self.cell_size,
                                         self.top + i * self.cell_size,
                                         self.cell_size,
                                         self.cell_size,
                                     )
                                     )
                    pygame.draw.rect(SCREEN, self.outer_color,
                                        (
                                            self.left + j * self.cell_size,
                                            self.top + i * self.cell_size,
                                            self.cell_size,
                                            self.cell_size,
                                        ),
                                        1
                                        )



    def get_shape(self, event_pos, pos: list):

        return (event_pos[0]-pos[1]*CELL_SIZE - self.left)//CELL_SIZE,\
               (event_pos[1]-pos[0]*CELL_SIZE - self.top)//CELL_SIZE


class MemoryBoard(MainBoard):
    def __init__(self, width, height, left, top, inner_color, outer_color, lines):
        super().__init__(width, height, left, top, inner_color, outer_color, lines)
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.cell_size = CELL_SIZE
        
    def reset(self):
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]


class WarningBoard(MainBoard):
    def __init__(self, width, height, left, top, inner_color, outer_color, lines):
        super().__init__(width, height, left, top, inner_color, outer_color, lines)
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.cell_size = CELL_SIZE
    def  render(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    pygame.draw.rect(SCREEN, self.outer_color,
                                        (
                                            self.left + j * self.cell_size,
                                            self.top + i * self.cell_size,
                                            self.cell_size,
                                            self.cell_size,
                                        ),
                                        10
                                        )

    def reset(self):
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]

