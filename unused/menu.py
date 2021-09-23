
import pygame
from pygame import image
from constants import *
from game import game
from buttons import Button
from functions import fade
import time


''' Merged onto stage class, this file is no longer needed '''


pygame.init()
pygame.display.set_caption('Never Gonna Give You Up')


def main_menu():

    # x, y, IMAGE_PATH, scale
    game_image = Button(375, 30, image_const('intro'), 0.8)
    untouchable = Button(260, 320, image_const('untouchable'), 1)
    description = Button(150, 100, image_const('description'), 0.75)

    qmark = Button(1100, 30, image_const('qmark'), 0.5)
    qmark_hovered = Button(1100, 30, image_const('qmark_hovered'), 0.5)

    level_one = Button(100, 500, image_const('level_one'), 0.7)
    level_one_hovered = Button(100, 500, image_const('level_one_hovered'), 0.7)

    level_two = Button(470, 500, image_const('level_two'), 0.7)
    level_two_hovered = Button(470, 500, image_const('level_two_hovered'), 0.7)

    level_three = Button(840, 500, image_const('level_three'), 0.7)
    level_three_hovered = Button(840, 500, image_const('level_three_hovered'), 0.7)
    
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
                # fade(S_WIDTH,S_HEIGHT)
                time.sleep(.3)
                game(0)
        if level_two.hovered():
            level_two_hovered.draw(SCREEN)
            if level_two_hovered.is_clicked():
                # fade(S_WIDTH,S_HEIGHT)
                game(1)
        if level_three.hovered():
            level_three_hovered.draw(SCREEN)
            if level_three_hovered.is_clicked():
                # fade(S_WIDTH,S_HEIGHT)
                game(2)
        if qmark.hovered():
            qmark_hovered.draw(SCREEN)
            if qmark_hovered.is_clicked():
                description.draw(SCREEN)
                qmark_hovered.draw(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

