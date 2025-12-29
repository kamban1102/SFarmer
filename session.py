import pygame
from text import Text

class Session:
    def __init__(self):
        self.round = 1
        self._turn = 0


    def update_round(self):
        self._turn += 1
        if self._turn == 2:
            self.round += 1
            self._turn = 0


    def display_round(self, surface):
        round_text = Text("ROUND:", pygame.color.THECOLORS['goldenrod1'], 100, 720 / 2 - 25, font_size = 60)
        round_no = Text(self.round, pygame.color.THECOLORS['goldenrod1'], 100, 720 / 2 + 25, font_size = 60)

        round_text.draw(surface)
        round_no.draw(surface)


    @staticmethod
    def check_victory(inventory):
        required_animals = ["cow", "horse", "pig", "sheep", "rabbit"]
        for animal in required_animals:
            if inventory.get(animal, 0) < 1:
                return False
        return True  

