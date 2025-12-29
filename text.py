import pygame

class Text:
    def __init__(self, text, text_color, coord_x, coord_y, font_size = 36, font_type = None):
        self.text = str(text)
        self.text_color = text_color
        self.font_size = font_size
        self.font_type = font_type
        self.font = pygame.font.SysFont(self.font_type, self.font_size)
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.update()


    def draw(self, surface):
        surface.blit(self.image, self.rect)


    def update(self):
        self.image = self.font.render(self.text, 1, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.center = self.coord_x, self.coord_y