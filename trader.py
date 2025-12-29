import pygame
from dialogbox import DialogBox
from button import Button
from text import Text

class Trader(DialogBox):
    def __init__(self, image, coord_x, coord_y, inventory, player_name, rabbit_icon, sheep_icon, pig_icon,
                 cow_icon, horse_icon, small_dog_icon, large_dog_icon, accept_icon, arrow_icon):
        super().__init__(image, coord_x, coord_y)

        self.active = False
        self.inventory = inventory
        self.player_name = str(player_name)
        self._exchange_rates = {
            ("rabbit", "sheep") : 6,
            ("sheep", "pig") : 2,
            ("pig", "cow") : 3,
            ("cow", "horse") : 2,
            ("sheep", "small_dog") : 1,
            ("cow", "large_dog") : 1
        }

        self.rect.center = coord_x, coord_y

        self.rabbit_icon = rabbit_icon
        self.sheep_icon = sheep_icon
        self.pig_icon = pig_icon
        self.cow_icon = cow_icon
        self.horse_icon = horse_icon
        self.small_dog_icon = small_dog_icon
        self.large_dog_icon = large_dog_icon
        self.accept_icon = accept_icon
        self.arrow_icon = arrow_icon

        self.confirm_trade_button = Button(self.accept_icon, self.rect.centerx - 75, self.rect.centery - 75,)
        self.confirm_trade_button2 = Button(self.accept_icon, self.rect.centerx - 75, self.rect.centery + 25,)
        self.confirm_trade_button3 = Button(self.accept_icon, self.rect.centerx - 75, self.rect.centery + 125,)
        self.confirm_trade_button4 = Button(self.accept_icon, self.rect.centerx + 325, self.rect.centery - 75,)
        self.confirm_trade_button5 = Button(self.accept_icon, self.rect.centerx + 325, self.rect.centery + 25,)
        self.confirm_trade_button6 = Button(self.accept_icon, self.rect.centerx + 325, self.rect.centery + 125,)


    def make_active(self):
        super().make_active()
    

    def disable(self):
        super().disable()


    # Check if trade can occur
    def check_if_available(self, given_animal, demanded_animal):
        for (source, target), rate in self._exchange_rates.items():
            if source == given_animal and target == demanded_animal:
                exchange_rate = rate
                break  
        if self.inventory.get(given_animal, 0) >= exchange_rate:
            return True
        else:
            return False


    def trade(self, given_animal, demanded_animal):
        for (source, target), exchange_rate in self._exchange_rates.items():
            if target == demanded_animal and source == given_animal:
                rate = exchange_rate

        self.inventory[given_animal] -= rate
        self.inventory[demanded_animal] += 1


    # Check the required amount in exchange rates by animals
    def get_required_amount(self, given_animal, demanded_animal):
        return self._exchange_rates.get((given_animal, demanded_animal), None)
    

    def disable_buttons(self):
        self.confirm_trade_button.disable()
        self.confirm_trade_button2.disable()
        self.confirm_trade_button3.disable()
        self.confirm_trade_button4.disable()
        self.confirm_trade_button5.disable()
        self.confirm_trade_button6.disable()


    # Part of the draw() implementation, making constant coordinate differences in rows
    def _draw_row(self, surface, icon, icon2, cx, cy, given_animal, demanded_animal):
        icon = pygame.transform.scale(icon, (50, 50),)
        icon2 = pygame.transform.scale(icon2, (50, 50),)

        required_amount = Text(self.get_required_amount(given_animal, demanded_animal),
                               pygame.color.THECOLORS['brown2'], cx - 33, cy + 40,
                                font_size = 40)
        
        amount2 = Text("1", pygame.color.THECOLORS['brown2'], cx + 118, cy + 40, font_size = 40)

        surface.blit(icon, [cx - 75, cy])
        surface.blit(icon2, [cx + 75, cy])
        surface.blit(self.arrow_icon, [cx + 8, cy + 8])
        required_amount.draw(surface)
        amount2.draw(surface)


    def draw(self, surface):
        # Drawing box background
        surface.blit(self.image, self.rect)

        # Info display
        player_info = Text(f"Trade - {self.player_name}", pygame.color.THECOLORS['gold'], 
                           self.rect.centerx, self.rect.centery - 130, font_size = 50)
        
        player_info.draw(surface)

        self._draw_row(surface, self.rabbit_icon, self.sheep_icon, self.rect.centerx - 250, 
                      self.rect.centery - 100, "rabbit", "sheep")
        self._draw_row(surface, self.sheep_icon, self.pig_icon, self.rect.centerx - 250, 
                      self.rect.centery, "sheep", "pig")
        self._draw_row(surface, self.pig_icon, self.cow_icon, self.rect.centerx - 250, 
                      self.rect.centery + 100, "pig", "cow")
        self._draw_row(surface, self.cow_icon, self.horse_icon, self.rect.centerx + 150, 
                      self.rect.centery - 100, "cow", "horse")
        self._draw_row(surface, self.sheep_icon, self.small_dog_icon, self.rect.centerx + 150, 
                      self.rect.centery, "sheep", "small_dog")
        self._draw_row(surface, self.cow_icon, self.large_dog_icon, self.rect.centerx + 150, 
                      self.rect.centery + 100, "cow", "large_dog")

        # Draw available functional buttons
        if self.check_if_available("rabbit", "sheep") and self.active:
            self.confirm_trade_button.draw(surface)
            self.confirm_trade_button.make_active()
        else:
            self.confirm_trade_button.disable()
        if self.check_if_available("sheep", "pig") and self.active:
            self.confirm_trade_button2.draw(surface)
            self.confirm_trade_button2.make_active()
        else:
            self.confirm_trade_button2.disable()
        if self.check_if_available("pig", "cow") and self.active:
            self.confirm_trade_button3.draw(surface)
            self.confirm_trade_button3.make_active()
        else:
            self.confirm_trade_button3.disable()
        if self.check_if_available("cow", "horse") and self.active:
            self.confirm_trade_button4.draw(surface)
            self.confirm_trade_button4.make_active()
        else:
            self.confirm_trade_button4.disable()
        if self.check_if_available("sheep", "small_dog") and self.active:
            self.confirm_trade_button5.draw(surface)
            self.confirm_trade_button5.make_active()
        else:
            self.confirm_trade_button5.disable()
        if self.check_if_available("cow", "large_dog") and self.active:
            self.confirm_trade_button6.draw(surface)
            self.confirm_trade_button6.make_active()
        else:
            self.confirm_trade_button6.disable()