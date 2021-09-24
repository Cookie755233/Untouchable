
import pygame
from buttons import Button
from constants import *

def continues():
    running = True

    undone = Button(S_WIDTH/2, S_HEIGHT*1/3, image_const('undone'), 0.5)
    continue_ = Button(S_WIDTH/2, S_HEIGHT*1/2, image_const('continue'), 0.5)
        
    while running:
        SCREEN.fill(WHITE)
        undone.draw_centered(SCREEN)
        continue_.draw_centered(SCREEN)

        if continue_.is_clicked_centered(S_WIDTH/2, S_HEIGHT*1/2):
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.update()

def win():
    running = True

    complete = Button(S_WIDTH/2, S_HEIGHT*1/3, image_const('complete'), 0.5)
    nextlevel = Button(S_WIDTH*3/8, S_HEIGHT/2, image_const('nextlevel'), 0.5)
    menu = Button(S_WIDTH*5/8, S_HEIGHT/2, image_const('menu'), 0.5)

    while running:
        SCREEN.fill(WHITE)

        complete.draw_centered(SCREEN)
        nextlevel.draw_centered(SCREEN)
        menu.draw_centered(SCREEN)
        
        if nextlevel.is_clicked_centered(S_WIDTH*3/8, S_HEIGHT/2):
            return True

        if menu.is_clicked_centered(S_WIDTH*5/8, S_HEIGHT/2):
            running = False # for ending win loop
            return False # for ending game loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.update()

