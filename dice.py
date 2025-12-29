import random

class Dice:
    def __init__(self, max = 12):
        self.max_amount = max


    def throw_first(self):
        return random.randint(1, self.max_amount)
    
    
    def throw_second(self):
        return random.randint(1, self.max_amount)