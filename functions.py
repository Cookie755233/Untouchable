
from constants import *


def shape_in_board(board, shape_abs_pos, figure) -> tuple[bool, list[list]]:
    '''check whether the shape falls into the board'''

    # shape_abs_pos = shape.left, shape.top (x, y)
    # figure = Shape.figure : [[0,1],[0,2],...]

    cell_size = CELL_SIZE
    is_in = False
    overlapped_cell = []
    for cell in figure:
        for r in range(board.height):
            for c in range(board.width):

                if (board.left + c * cell_size
                    < shape_abs_pos[0] + cell[1]*cell_size
                    < board.left + (c + 1) * cell_size

                    and board.top + r * cell_size
                    < shape_abs_pos[1] + cell[0]*cell_size
                        < board.top + (r + 1) * cell_size):

                    is_in = True
                    if is_in:
                        overlapped_cell.append([c, r])

    return is_in, overlapped_cell

def nearby(board):
    cashe = set([num for inner_list in [list(row) for row in board] for num in inner_list])
    paint_locs = []
    cashe.remove(0)
    for num in cashe:
        for r in range(len(board)):
            for c in range(len(board[r])):
                direction = [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1),
                                (r-1, c-1), (r-1, c+1), (r-1, c+1), (r+1, c+1)]
                if board[r][c] == num:
                    for row, col in direction:
                        if row >= 0 and col >= 0 and row < len(board) and col < len(board[row]):
                            if board[row][col] in cashe and board[row][col] != num:
                                paint_locs.append([r, c])

    return list(set(tuple(loc) for loc in paint_locs)) # location of nearby cells


def clean_up(board, num=None):
    def dfs(board, r, c):
        position = [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]
        for row, col in position:
            if row >= 0 and col >= 0 and row < len(board) and col < len(board[row]):
                if 2 < board[row][col] < 6:
                    board[row][col] = 0

    for r in range(len(board)):
        for c in range(len(board[r])):
            if num != None:
                if board[r][c] == num + 5:
                    dfs(board, r, c)
                    board[r][c] = 0
            if board[r][c] < 3:
                board[r][c] = 0


def draw_text_middle(surface, text, size, color, fontname):
    pygame.font.init()
    font = pygame.font.SysFont(fontname, size)
    label = font.render(text, 1, color)

    surface.blit(label, (S_WIDTH/2 - (label.get_width()/2), S_HEIGHT/2 - label.get_height()/2))


def fade(width, height):
    fade = pygame.Surface((width, height))
    fade.fill(WHITE)
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        SCREEN.blit(fade, (0,0))
        pygame.display.update(1)
        

def submit(board):
    win = False
    flat = [x for row in board for x in row]
    if all([flat.count(i) == 6 for i in range(1,12)]):
        win = True
  
    return win
