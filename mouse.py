
import pygame

class Mouse(pygame.sprite.Sprite):
    """mouse class for implementing click actions on an object"""

    def __init__(self, group):
        super().__init__(group)
        self.rect = pygame.Rect(pygame.mouse.get_pos(), (1, 1))

    def update(self):
        self.rect = pygame.Rect(pygame.mouse.get_pos(), (1, 1))