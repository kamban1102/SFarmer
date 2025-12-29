import pygame

class Pet():
    def __init__(self, images, coord_x, coord_y):
        self.images = images
        self.image = images[0]
        self.coord_x = coord_x
        self.coord_y = coord_y
        self._count = 0

    def _animate(self, animation_speed):
        self.image = self.images[self._count//animation_speed]
        self._count = (self._count + 1) % (len(self.images) * animation_speed)

    def update(self, speed):
        self._animate(speed)

    def draw(self, surface):
        surface.blit(self.image, [self.coord_x, self.coord_y])