
from constants import *

class Shape:
    def __init__(self, width, height, left, top, inner_color, outer_color, lines, rotation=0):
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.inner_color = inner_color
        self.outer_color = outer_color
        self.lines = lines
        self.rotation = rotation
        self.cell_size = CELL_SIZE


    def create_shape(self, num: int):  # num = 0-11
        self.figure = TUPLE_POSITION[num][self.rotation]
        self.board = [[0 for _ in range(self.width)]
                      for _ in range(self.height)]
        for pos in self.figure:
            self.board[pos[0]][pos[1]] = num+1


    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] > 0:
                    pygame.draw.rect(SCREEN, self.inner_color,
                                     (
                                         self.left + j * self.cell_size,
                                         self.top + i * self.cell_size,
                                         self.cell_size-1,
                                         self.cell_size-1,
                                     )
                                     )
                    pygame.draw.rect(
                        SCREEN,
                        self.outer_color,
                        (
                            self.left + j * self.cell_size,
                            self.top + i * self.cell_size,
                            self.cell_size,
                            self.cell_size,
                        ),
                        1,
                    )

    def rotate(self, num):
        self.rotation = (self.rotation + 1) % len(TUPLE_POSITION[num])
        self.figure = TUPLE_POSITION[num][self.rotation]
        
        for pos in self.figure:
            self.board[pos[0]][pos[1]] = num+1
            

    def update(self, left, top):
        self.left = left
        self.top = top

    # checking the mouse click on the figure
    def click_on_shape(self, mouse_x, mouse_y, num) -> tuple[bool, tuple]:
        self.figure = TUPLE_POSITION[num][self.rotation]
        
        clicked = False
        cell_size = CELL_SIZE
        for i in range(len(self.figure)):
            if (self.left + self.figure[i][1] * cell_size <= mouse_x <= self.left + self.figure[i][1] * cell_size + cell_size
                    and self.top + self.figure[i][0] * cell_size <= mouse_y <= self.top + self.figure[i][0] * cell_size + cell_size):
                clicked = True
                on_cell = self.figure[i] # tuple pos of [5x5]
                break
        if clicked:
            return clicked, on_cell
        else: 
            return clicked, None
