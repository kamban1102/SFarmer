import pygame
from text import Text
from dialogbox import DialogBox

class Button(DialogBox):
    def __init__(self, image, coord_x, coord_y):
        super().__init__(image, coord_x, coord_y)
        self.active = False


    def disable(self):
        return super().disable()
    

    def make_active(self):
        return super().make_active()


    def draw(self, surface):
        surface.blit(self.image, self.rect)