import pygame, os
from dialogbox import DialogBox
from text import Text
from dice import Dice
from button import Button

class Player(DialogBox):
    def __init__(self, image, coord_x, coord_y, name, rabbit_icon, sheep_icon, pig_icon, cow_icon,
                 horse_icon, small_dog_icon, large_dog_icon, wolf_icon, fox_icon, throw_dice_icon,
                 trade_icon, end_turn_icon, trade_icon_pressed, sound_path, sounds_on = True, second_player = False):
        super().__init__(image, coord_x, coord_y)
        self.name = str(name)
        self.livestock = {
            "rabbit": 0,
            "sheep": 0,
            "pig": 0,
            "cow": 0,
            "horse": 0,
            "small_dog": 0,
            "large_dog" : 0
        }
        self.rect.center = coord_x, coord_y

        self.rabbit_icon = rabbit_icon
        self.sheep_icon = sheep_icon
        self.pig_icon = pig_icon
        self.cow_icon = cow_icon
        self.horse_icon = horse_icon
        self.small_dog_icon = small_dog_icon
        self.large_dog_icon = large_dog_icon
        self.wolf_icon = wolf_icon
        self.fox_icon = fox_icon

        self.rabbit_sound = pygame.mixer.Sound(os.path.join(sound_path, 'rabbit_sound.mp3'))
        self.sheep_sound = pygame.mixer.Sound(os.path.join(sound_path, 'sheep_sound.mp3'))
        self.pig_sound = pygame.mixer.Sound(os.path.join(sound_path, 'pig_sound.mp3'))
        self.cow_sound = pygame.mixer.Sound(os.path.join(sound_path, 'cow_sound.mp3'))
        self.horse_sound = pygame.mixer.Sound(os.path.join(sound_path, 'horse_sound.mp3'))
        self.fox_sound = pygame.mixer.Sound(os.path.join(sound_path, 'fox_sound.mp3'))
        self.wolf_sound = pygame.mixer.Sound(os.path.join(sound_path, 'wolf_sound.mp3'))

        self.animal_sounds_on = sounds_on

        # Boolean allowing for change second player's interface coords
        self._second_player = second_player

        if not self._second_player:
            self._buttons_y = 55
        else:
            self._buttons_y = -50
        
        self._dice = Dice()
        self.threw_dice = False

        self.trade_pressed = False

        # Images of last throws, for each dice
        self._last_throw = self.rabbit_icon,
        self._last_throw2 = self.rabbit_icon
        
        self.throw_dice_button = Button(throw_dice_icon, self.rect.centerx - 200,
                                         self.rect.centery + self._buttons_y,)
        
        self.trade_button = Button(trade_icon, self.rect.centerx + 115,
                                    self.rect.centery + self._buttons_y,)
        
        self.trade_button_pressed = Button(trade_icon_pressed, self.rect.centerx + 115, 
                                           self.rect.centery + self._buttons_y,)
        
        self.end_turn_button = Button(end_turn_icon, self.rect.centerx + 430, 
                                      self.rect.centery + self._buttons_y,)


    def get_name(self):
        return self.name
    

    # Get the amount of given animal in livestock
    def _get_livestock_count(self, animal):
        return self.livestock.get(animal, None)
    

    def make_active(self):
        super().make_active()
        self.threw_dice = False
    

    def disable(self):
        super().disable()


    def press_trade(self):
        self.trade_pressed = True


    def unpress_trade(self):
        self.trade_pressed = False


    # Throwing dice and modifying the amount of animals
    def throw_and_update(self):
        throw_result = self._dice.throw_first()
        throw_result2 = self._dice.throw_second()

        throw_livestock = {
            "rabbit": 0,
            "sheep": 0,
            "pig": 0,
            "cow": 0,
            "horse": 0,
        }

        # Checking first dice and adding to temporary balance
        if throw_result == 12:
            self._last_throw = self.fox_icon
            if self.animal_sounds_on:
                self.fox_sound.play()
            if self.livestock.get("small_dog"):
                self.livestock['small_dog'] -= 1
            else:
                self.livestock["rabbit"] = 0
        elif throw_result >= 1 and throw_result <= 6:
            self._last_throw = self.rabbit_icon
            throw_livestock["rabbit"] += 1
            if self.animal_sounds_on:
                self.rabbit_sound.play()
        elif throw_result == 7 or throw_result == 8:
            self._last_throw = self.sheep_icon
            throw_livestock["sheep"] += 1
            if self.animal_sounds_on:
                self.sheep_sound.play()
        elif throw_result == 9 or throw_result == 10:
            self._last_throw = self.pig_icon
            throw_livestock["pig"] += 1
            if self.animal_sounds_on:
                self.pig_sound.play()
        elif throw_result == 11:
            self._last_throw = self.cow_icon
            throw_livestock["cow"] += 1
            if self.animal_sounds_on:
                self.cow_sound.play()
        
        # Checking second dice
        if throw_result2 == 12:
            self._last_throw2 = self.wolf_icon
            self.wolf_sound.play()
            if self.livestock.get("large_dog"):
                self.livestock['large_dog'] -= 1
            else:
                self.livestock["rabbit"] = 0
                self.livestock["sheep"] = 0
                self.livestock["pig"] = 0
                self.livestock["cow"] = 0
        elif throw_result2 >= 1 and throw_result2 <= 6:
            self._last_throw2 = self.rabbit_icon
            throw_livestock["rabbit"] += 1
            if self.animal_sounds_on:
                self.rabbit_sound.play()
        elif throw_result2 >= 7 and throw_result2 <= 9:
            self._last_throw2 = self.sheep_icon
            throw_livestock["sheep"] += 1
            if self.animal_sounds_on:
                self.sheep_sound.play()
        elif throw_result2 == 10:
            self._last_throw2 = self.pig_icon
            throw_livestock["pig"] += 1
            if self.animal_sounds_on:
                self.pig_sound.play()
        elif throw_result2 == 11:
            self._last_throw2 = self.horse_icon
            throw_livestock["horse"] += 1
            if self.animal_sounds_on:
                self.horse_sound.play()

        # Multiplying animals in livestock by temporary balance and their previous numbers
        if throw_livestock["rabbit"]:
            throw_livestock["rabbit"] += self.livestock["rabbit"]
            self.livestock["rabbit"] += int(throw_livestock["rabbit"] / 2)
        if throw_livestock["sheep"]:
            throw_livestock["sheep"] += self.livestock["sheep"]
            self.livestock["sheep"] += int(throw_livestock["sheep"] / 2)
        if throw_livestock["pig"]:
            throw_livestock["pig"] += self.livestock["pig"]
            self.livestock["pig"] += int(throw_livestock["pig"] / 2)
        if throw_livestock["cow"]:
            throw_livestock["cow"] += self.livestock["cow"]
            self.livestock["cow"] += int(throw_livestock["cow"] / 2)
        if throw_livestock["horse"]:
            throw_livestock["horse"] += self.livestock["horse"]
            self.livestock["horse"] += int(throw_livestock["horse"] / 2)

        self.threw_dice = True


                
    def draw(self, surface):
        # Changing interface coordinates for second player
        if not self._second_player:
            animals_y = -85
            counter_y = -20
        else:
            animals_y = 10
            counter_y = 75
        
        # Display box background
        surface.blit(self.image, self.rect)
                    
        # Display animal icons
        surface.blit(self.rabbit_icon, [self.rect.centerx - 590, self.rect.centery + animals_y])
        surface.blit(self.sheep_icon, [self.rect.centerx - 407, self.rect.centery + animals_y])
        surface.blit(self.pig_icon, [self.rect.centerx - 224, self.rect.centery + animals_y])
        surface.blit(self.cow_icon, [self.rect.centerx - 40, self.rect.centery + animals_y])
        surface.blit(self.horse_icon, [self.rect.centerx + 143, self.rect.centery + animals_y])
        surface.blit(self.small_dog_icon, [self.rect.centerx + 326, self.rect.centery + animals_y])
        surface.blit(self.large_dog_icon, [self.rect.centerx + 510, self.rect.centery + animals_y])

        # Text objects definition and drawing
        rabbit_counter = Text(self._get_livestock_count("rabbit"), pygame.color.THECOLORS['brown2'], 
                              self.rect.centerx - 520, self.rect.centery + counter_y, font_size = 60)
        
        sheep_counter = Text(self._get_livestock_count("sheep"), pygame.color.THECOLORS['brown2'], 
                             self.rect.centerx - 337, self.rect.centery + counter_y, font_size = 60)
        
        pig_counter = Text(self._get_livestock_count("pig"), pygame.color.THECOLORS['brown2'], 
                           self.rect.centerx - 154, self.rect.centery + counter_y, font_size = 60)
        
        cow_counter = Text(self._get_livestock_count("cow"), pygame.color.THECOLORS['brown2'], 
                           self.rect.centerx + 30, self.rect.centery + counter_y, font_size = 60)
        
        horse_counter = Text(self._get_livestock_count("horse"), pygame.color.THECOLORS['brown2'], 
                             self.rect.centerx + 213, self.rect.centery + counter_y, font_size = 60)
        
        small_dog_counter = Text(self._get_livestock_count("small_dog"), pygame.color.THECOLORS['brown2'], 
                                 self.rect.centerx + 396, self.rect.centery + counter_y, font_size = 60)
        
        large_dog_counter = Text(self._get_livestock_count("large_dog"), pygame.color.THECOLORS['brown2'], 
                                 self.rect.centerx + 580, self.rect.centery + counter_y, font_size = 60)
        
        name_display = Text(self.name, pygame.color.THECOLORS['gold'], self.rect.centerx - 540,
                            self.rect.centery + self._buttons_y, font_size = 68)

        text_objects = [rabbit_counter, sheep_counter, pig_counter, cow_counter, horse_counter, small_dog_counter,
                        large_dog_counter, name_display]
        
        for obj in text_objects:
            obj.draw(surface)

    
        # Drawing player interface
        if self.active:

            # Proper variation of the trade button
            if not self.trade_pressed:
                self.trade_button.draw(surface)
            else:
                self.trade_button_pressed.draw(surface)

            # End turn button
            self.end_turn_button.draw(surface)

            # Throw dice button
            if not self.threw_dice:
                self.throw_dice_button.draw(surface)

            else:
                # Displaying last throws
                surface.blit(pygame.transform.scale(self._last_throw, (50, 50)), 
                         [self.rect.centerx - 240, self.rect.centery + self._buttons_y - 20])

                surface.blit(pygame.transform.scale(self._last_throw2, (50, 50)), 
                         [self.rect.centerx - 160, self.rect.centery + self._buttons_y - 20])
           

            

        




    
