
from constants import *
import pygame


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.scale = scale

    def draw(self, surface):
        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def draw_centered(self, surface):
        surface.blit(self.image, (self.rect.x - (self.image.get_width() * self.scale),
                                  self.rect.y - (self.image.get_height() * self.scale)))

    def hovered(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def is_clicked(self):
        if self.hovered() and pygame.mouse.get_pressed()[0]:
            return True

	''' Try to get hovered_centered'''
    def hovered_centered(self, centerX, centerY):
        pos = pygame.mouse.get_pos()
        rect = self.image.get_rect(center=(centerX, centerY))
        if rect.collidepoint(pos):
            return True
        else:
            return False

    def is_clicked_centered(self):
        if self.hovered_centered and pygame.mouse.get_pressed()[0]:
            return True
