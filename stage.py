
import pygame
import random
import time
from constants import *
from board import MainBoard, MemoryBoard, WarningBoard
from shapes import Shape
from animation import Coordinates, animation_path
from mouse import Mouse
from functions import *
from cutscene import win, continues

pygame.init()
clock = pygame.time.Clock()

class GameState():
    def __init__(self):
        self.state = 'main_menu'
        self.lvl = None

    def stage_manager(self):
        if self.state == 'main_menu':
            self.main_menu()

        if self.state == 'main_game':
            self.main_game()

    def main_menu(self):
        # x, y, IMAGE_PATH, scale
        game_image = Button(375, 30, image_const('intro'), 0.8)
        untouchable = Button(260, 320, image_const('untouchable'), 1)
        description = Button(150, 100, image_const('description'), 0.75)

        qmark = Button(1100, 30, image_const('qmark'), 0.5)
        qmark_hovered = Button(1100, 30, image_const('qmark_hovered'), 0.5)

        level_one = Button(100, 500, image_const('level_one'), 0.7)
        level_one_hovered = Button(
            100, 500, image_const('level_one_hovered'), 0.7)

        level_two = Button(470, 500, image_const('level_two'), 0.7)
        level_two_hovered = Button(
            470, 500, image_const('level_two_hovered'), 0.7)

        level_three = Button(840, 500, image_const('level_three'), 0.7)
        level_three_hovered = Button(
            840, 500, image_const('level_three_hovered'), 0.7)

        while True:
            SCREEN.fill(WHITE)
            game_image.draw(SCREEN)
            untouchable.draw(SCREEN)
            level_one.draw(SCREEN)
            level_two.draw(SCREEN)
            level_three.draw(SCREEN)
            qmark.draw(SCREEN)

            if level_one.hovered():
                level_one_hovered.draw(SCREEN)
                if level_one_hovered.is_clicked():
                    time.sleep(.3)
                    self.lvl = 0
                    self.state = 'main_game'
                    self.stage_manager()

            if level_two.hovered():
                level_two_hovered.draw(SCREEN)
                if level_two_hovered.is_clicked():
                    self.lvl = 1
                    self.state = 'main_game'
                    self.stage_manager()

            if level_three.hovered():
                level_three_hovered.draw(SCREEN)
                if level_three_hovered.is_clicked():
                    self.lvl = 2
                    self.state = 'main_game'
                    self.stage_manager()

            if qmark.hovered():
                qmark_hovered.draw(SCREEN)
                if qmark_hovered.is_clicked():
                    description.draw(SCREEN)
                    qmark_hovered.draw(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()

    def main_game(self):
        # Time
        milsec = 0
        second = 0
        minute = 0
        hour = 0
        numbers = ['zero', 'one', 'two', 'three', 'four',
                   'five', 'six', 'seven', 'eight', 'nine']

        tens = [pygame.transform.scale(image_const(num), (50, 60))
                for num in numbers[0:6]]
        singles = [pygame.transform.scale(
            image_const(num), (50, 60)) for num in numbers]
        colon = pygame.transform.scale(image_const('colon'), (50, 60))

        # Buttons
        submit = Button((levels[self.lvl][2]*2 + CELL_SIZE*levels[self.lvl][0])/2 - 95,
                        levels[self.lvl][3]+CELL_SIZE*levels[self.lvl][1],
                        image_const('submit'),
                        0.7)
        submit_hovered = Button((levels[self.lvl][2]*2 + CELL_SIZE*levels[self.lvl][0])/2 - 95,
                                levels[self.lvl][3]+CELL_SIZE *
                                levels[self.lvl][1],
                                image_const('submit_hovered'),
                                0.7)
        home = Button(30, 750, image_const('home'), 0.3)

        # Board //levels = [width, height, left, top]
        main_board = MainBoard(
            levels[self.lvl][0], levels[self.lvl][1], levels[self.lvl][2], levels[self.lvl][3], WHITE, BLACK, 1)
        memo_board = MemoryBoard(
            levels[self.lvl][0], levels[self.lvl][1], levels[self.lvl][2], levels[self.lvl][3], WHITE, BLACK, 1)
        warning_board = WarningBoard(
            levels[self.lvl][0], levels[self.lvl][1], levels[self.lvl][2], levels[self.lvl][3], WHITE, RED, 1)

        shapes = [Shape(5, 5, shape_pos[i][0], shape_pos[i][1],
                        COLORS[random.randint(0, len(COLORS)-1)], BLACK, 1) for i in range(11)]

        # Animation //Coordinates(CenterX, CenterY, width, height)
        board_coord = Coordinates(levels[self.lvl][2] + 1/2*levels[self.lvl][0]*CELL_SIZE,
                                  levels[self.lvl][3] + 1/2 *
                                  levels[self.lvl][1]*CELL_SIZE,
                                  levels[self.lvl][0] * CELL_SIZE,
                                  levels[self.lvl][1] * CELL_SIZE).rectangle()
        board_animation = animation_path(board_coord, 50)

        pressed = None

        mouse = pygame.sprite.Group()
        Mouse(mouse)

        while True:
            SCREEN.fill(WHITE)

            # Bottons
            submit.draw(SCREEN)
            home.draw(SCREEN)
            # Game elements
            main_board.render()
            warning_board.render()
            # Outline for main_board
            pygame.draw.rect(
                SCREEN, BLACK,
                (levels[self.lvl][2], levels[self.lvl][3], CELL_SIZE*levels[self.lvl][0], CELL_SIZE*levels[self.lvl][1]), 5)
            # Shapes
            for shape in shapes:
                shape.render()

            # Time
            time_left = (levels[self.lvl][2]*2 +
                         CELL_SIZE*levels[self.lvl][0])/2 - 100

            SCREEN.blit(tens[hour//10], (time_left, levels[self.lvl][3]-60))
            SCREEN.blit(singles[hour % 10],
                        (time_left+20, levels[self.lvl][3]-60))

            SCREEN.blit(colon, (time_left+40, levels[self.lvl][3]-60))
            SCREEN.blit(tens[minute//10],
                        (time_left+60, levels[self.lvl][3]-60))
            SCREEN.blit(singles[minute % 10],
                        (time_left+80, levels[self.lvl][3]-60))

            SCREEN.blit(colon, (time_left+100, levels[self.lvl][3]-60))
            SCREEN.blit(tens[second//10],
                        (time_left+120, levels[self.lvl][3]-60))
            SCREEN.blit(singles[second % 10],
                        (time_left+140, levels[self.lvl][3]-60))

            # Game
            if home.is_clicked():
                self.state = 'main_menu'
                self.stage_manager()


            if submit.hovered() and pressed==None:
                submit_hovered.draw(SCREEN)
                if submit_hovered.is_clicked():
                    for pos in board_animation:
                        for cell in pos:
                            pygame.draw.rect(SCREEN, (255, 255, 0), pygame.Rect(
                                cell[0]-3, cell[1]-3, 6, 6), 0)
                        pygame.display.update()
                        complete = check_win(memo_board.board)

                    if not complete:
                        continues()
                    else:
                        win()
                        if win() is True:
                            self.lvl += 1
                            if self.lvl > 2:
                                self.state = 'main_menu'
                                self.stage_manager()
                        else:
                            self.state = 'main_menu'
                            self.stage_manager()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                for i, shape in enumerate(shapes):
                    shape.create_shape(i)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pressed == None:
                            clicked = shape.click_on_shape(
                                event.pos[0], event.pos[1], i)
                            if clicked[0] == True:
                                warning_board.reset()
                                pressed = i
                                pos = clicked[1]

                                if pressed == i:  # clean the memo_board if shape_i get picked up
                                    for r in range(len(memo_board.board)):
                                        for c in range(len(memo_board.board[r])):
                                            if memo_board.board[r][c] == i+1:
                                                memo_board.board[r][c] = 0

                        if event.button == 3:
                            pressed = None
                            warning_board.reset()

                    if event.type == pygame.MOUSEMOTION and pressed == i:
                        x_new = event.pos[0] - pos[1]*CELL_SIZE
                        y_new = event.pos[1] - pos[0]*CELL_SIZE
                        shape.update(x_new, y_new)

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE and pressed == i:
                            shape.rotate(i)

                    if event.type == pygame.MOUSEBUTTONUP:
                        if pressed == i:
                            is_in, cells_on_board = shape_in_board(
                                memo_board, (shape.left, shape.top), shape.figure)

                            if is_in:
                                shape_overlapped = [
                                    memo_board.board[cell[1]][cell[0]] == 0 for cell in cells_on_board]

                                if all(shape_overlapped):
                                    for cell in cells_on_board:
                                        if memo_board.board[cell[1]][cell[0]] == 0:
                                            memo_board.board[cell[1]
                                                             ][cell[0]] = i+1
                                        new_pos = memo_board.get_shape(
                                            event.pos, pos)
                                        shape.update(memo_board.left + new_pos[0]*CELL_SIZE,
                                                     memo_board.top + new_pos[1]*CELL_SIZE)
                                    pressed = None

                                else:
                                    pressed = None
                                    shape.update(
                                        shape_pos[i][0], shape_pos[i][1])

                            paint_locs = nearby(memo_board.board)
                            for loc in paint_locs:
                                warning_board.board[loc[0]][loc[1]] = 1

            milsec += 1
            if milsec == 60:
                milsec = 0
                second = second+1
            if second == 60:
                second = 0
                minute = minute+1
            if minute == 60:
                minute = 0
                second = 0
                hour = hour+1
            if hour == 24:
                hour = 0
                second = 0
                minute = 0

            clock.tick(FPS)

            mouse.update()
            pygame.display.update()
