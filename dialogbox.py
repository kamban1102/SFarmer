from abc import ABC, abstractmethod
import pygame

class DialogBox(ABC, pygame.sprite.Sprite):
    def __init__(self, image, coord_x, coord_y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = coord_x, coord_y
        self.active = True


    def make_active(self):
        self.active = True


    def disable(self):
        self.active = False


    @abstractmethod
    def draw(self):
        pass
