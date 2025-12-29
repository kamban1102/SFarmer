import pygame, os
import datetime
from player import Player
from session import Session
from trader import Trader
from pet import Pet
from text import Text
from button import Button


pygame.init()

# Resolution settings and clock initialization
SIZESCREEN = WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode(SIZESCREEN)
clock = pygame.time.Clock()

# Preparing files
image_path = os.path.join(os.getcwd(), 'assets/images')
sound_path = os.path.join(os.getcwd(), 'assets/sounds')
file_names = os.listdir(image_path)
BACKGROUND = pygame.image.load(os.path.join(image_path, 'background.jpg')).convert()
file_names.remove('background.jpg')
IMAGES = {}
for file_name in file_names:
    image_name = file_name[:-4].upper()
    IMAGES[image_name] = pygame.image.load(os.path.join(image_path, file_name)).convert_alpha(BACKGROUND)

rabbit_img = IMAGES['RABBIT']
sheep_img = IMAGES['SHEEP']
pig_img = IMAGES['PIG']
cow_img = IMAGES['COW']
horse_img = IMAGES['HORSE']
small_dog_img = IMAGES['SMALLDOG']
large_dog_img = IMAGES['LARGEDOG']
wolf_img = IMAGES['WOLF']
fox_img = IMAGES['FOX']

throw_dice_button_img = IMAGES['THROWDICE']
trade_button_img = IMAGES['TRADE']
end_turn_button_img = IMAGES['ENDTURN']
trade_button_pressed_img = IMAGES['TRADEPRESSED']

button_sound = pygame.mixer.Sound(os.path.join(sound_path, 'button_sound.mp3'))
menu_sound = pygame.mixer.Sound(os.path.join(sound_path, 'button_sound2.mp3'))
throw_sound = pygame.mixer.Sound(os.path.join(sound_path, 'dice_sound.mp3'))

sheep_sound = pygame.mixer.Sound(os.path.join(sound_path, 'sheep_sound.mp3'))
pig_sound = pygame.mixer.Sound(os.path.join(sound_path, 'pig_sound.mp3'))
cow_sound = pygame.mixer.Sound(os.path.join(sound_path, 'cow_sound.mp3'))
horse_sound = pygame.mixer.Sound(os.path.join(sound_path, 'horse_sound.mp3'))
small_dog_sound = pygame.mixer.Sound(os.path.join(sound_path, 'smalldog_sound.mp3'))
large_dog_sound = pygame.mixer.Sound(os.path.join(sound_path, 'largedog_sound.mp3'))

# Allows to disable animal sounds that play when throwing dice or trading
animal_sounds_on = True

# Variables storing names of the players
player_name = "Player1"
player2_name = "Player2"

# Class instances
player = Player(IMAGES['PLAYERBOX'], 640, 100, player_name, rabbit_img, sheep_img, pig_img, cow_img, horse_img,
                 small_dog_img, large_dog_img, wolf_img, fox_img, throw_dice_button_img, trade_button_img,
                   end_turn_button_img, trade_button_pressed_img, sound_path, animal_sounds_on)

player2 = Player(IMAGES['PLAYERBOX'], 640, 620, player2_name, rabbit_img, sheep_img, pig_img, cow_img, horse_img,
                 small_dog_img, large_dog_img, wolf_img, fox_img, throw_dice_button_img, trade_button_img,
                  end_turn_button_img, trade_button_pressed_img, sound_path, animal_sounds_on, True)

# Making player 2 inactive at start
player2.disable()

trader = Trader(IMAGES['TRADEBOX'], 640, 360, player.livestock, player_name, rabbit_img, sheep_img, pig_img,
                cow_img, horse_img, small_dog_img, large_dog_img, IMAGES['ACCEPT'], IMAGES['ARROW'])
trader2 = Trader(IMAGES['TRADEBOX'], 640, 360, player2.livestock, player2_name, rabbit_img, sheep_img, pig_img, 
                 cow_img, horse_img, small_dog_img, large_dog_img, IMAGES['ACCEPT'], IMAGES['ARROW'])

session = Session()

# Animated pets
# frog = Pet([IMAGES[name] for name in IMAGES if 'FROG' in name], 1060, 360)
# cat = Pet([IMAGES[name] for name in IMAGES if 'CAT' in name], 1140, 290)

# Menu buttons/text
start_button = Button(IMAGES['START'], 420, 360)
exit_button = Button(IMAGES['EXIT'], 860, 360)

# Game loop with variables
window_open = True
active_game = False
while window_open:
    # Loading background image
    screen.blit(BACKGROUND, (0, 0))

    # Displaying menu
    if not active_game:
        start_button.draw(screen)
        exit_button.draw(screen)

    # Event scripts
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if active_game:
                    active_game = False
                    window_open = False
                else:
                    window_open = False

        if event.type == pygame.QUIT:
            window_open = False

        # Menu button scripts
        if event.type == pygame.MOUSEBUTTONDOWN and not active_game:
            if start_button.rect.collidepoint(pygame.mouse.get_pos()):
                menu_sound.play()
                active_game = True
                pygame.time.delay(150)
            if exit_button.rect.collidepoint(pygame.mouse.get_pos()):
                menu_sound.play()
                window_open = False

        # Scripts - player 1
        if event.type == pygame.MOUSEBUTTONDOWN and player.active:

            # Toggling trade window
            if player.trade_button.rect.collidepoint(pygame.mouse.get_pos()) and not trader.active:
                button_sound.play()
                trader.make_active()
                player.press_trade()
            elif player.trade_button.rect.collidepoint(pygame.mouse.get_pos()) and trader.active:
                button_sound.play()
                trader.disable()
                player.unpress_trade()

            # Confirming trade button scripts
            if trader.active:
                if trader.confirm_trade_button.rect.collidepoint(pygame.mouse.get_pos()) and trader.confirm_trade_button.active:
                    button_sound.play()
                    if animal_sounds_on:
                        sheep_sound.play()
                    trader.trade("rabbit", "sheep")
                elif trader.confirm_trade_button2.rect.collidepoint(pygame.mouse.get_pos()) and trader.confirm_trade_button2.active:
                    button_sound.play()
                    if animal_sounds_on:
                        pig_sound.play()
                    trader.trade("sheep", "pig")
                elif trader.confirm_trade_button3.rect.collidepoint(pygame.mouse.get_pos()) and trader.confirm_trade_button3.active:
                    button_sound.play()
                    if animal_sounds_on:
                        cow_sound.play()
                    trader.trade("pig", "cow")
                elif trader.confirm_trade_button4.rect.collidepoint(pygame.mouse.get_pos()) and trader.confirm_trade_button4.active:
                    button_sound.play()
                    if animal_sounds_on:
                        horse_sound.play()
                    trader.trade("cow", "horse")
                elif trader.confirm_trade_button5.rect.collidepoint(pygame.mouse.get_pos()) and trader.confirm_trade_button5.active:
                    button_sound.play()
                    if animal_sounds_on:
                        small_dog_sound.play()
                    trader.trade("sheep", "small_dog")
                elif trader.confirm_trade_button6.rect.collidepoint(pygame.mouse.get_pos()) and trader.confirm_trade_button6.active:
                    button_sound.play()
                    if animal_sounds_on:
                        large_dog_sound.play()
                    trader.trade("cow", "large_dog")

            # End turn button scripts
            if player.end_turn_button.rect.collidepoint(pygame.mouse.get_pos()):
                button_sound.play()
                player.disable()
                trader.disable()
                player.unpress_trade()
                # Check for the player reaching the game's goals at turn end, export the score to a text file, if won
                if session.check_victory(player.livestock):
                    finish_text = Text(f"{player_name} wins!", pygame.color.THECOLORS['red'], *screen.get_rect().center,
                                       font_size=120)
                    try:
                        now = datetime.datetime.now()
                        current_time = f"{now.year}-{now.month:02d}-{now.day:02d} {now.hour:02d}:{now.minute:02d}:{now.second:02d}"
                        with open('scores.txt', 'a') as scores_file:
                            scores_file.write(f"{player_name}   {current_time}\tRound: {session.round}\n")
                    except Exception as e:
                        print(f"Error while trying to write a game's score to a file: {e}")
                    active_game = False
                    window_open = False
                    finish_text.draw(screen)
                player2.make_active()
                session.update_round()

            # Throw dice button script and limit the player to one throw
            if not player.threw_dice and player.throw_dice_button.rect.collidepoint(pygame.mouse.get_pos()):
                player.throw_and_update()
                player.threw_dice = True
                throw_sound.play()


        # Scripts - player 2
        elif event.type == pygame.MOUSEBUTTONDOWN and player2.active:

            if player2.trade_button.rect.collidepoint(pygame.mouse.get_pos()) and not trader2.active:
                button_sound.play()
                trader2.make_active()
                player2.press_trade()
            elif player2.trade_button.rect.collidepoint(pygame.mouse.get_pos()) and trader2.active:
                button_sound.play()
                trader2.disable()
                # trader2.disable_buttons()
                player2.unpress_trade()

            if trader2.active:
                if trader2.confirm_trade_button.rect.collidepoint(pygame.mouse.get_pos()) and trader2.confirm_trade_button.active:
                    button_sound.play()
                    if animal_sounds_on:
                        sheep_sound.play()
                    trader2.trade("rabbit", "sheep")
                elif trader2.confirm_trade_button2.rect.collidepoint(pygame.mouse.get_pos()) and trader2.confirm_trade_button2.active:
                    button_sound.play()
                    if animal_sounds_on:
                        pig_sound.play()
                    trader2.trade("sheep", "pig")
                elif trader2.confirm_trade_button3.rect.collidepoint(pygame.mouse.get_pos()) and trader2.confirm_trade_button3.active:
                    button_sound.play()
                    if animal_sounds_on:
                        cow_sound.play()
                    trader2.trade("pig", "cow")
                elif trader2.confirm_trade_button4.rect.collidepoint(pygame.mouse.get_pos()) and trader2.confirm_trade_button4.active:
                    button_sound.play()
                    if animal_sounds_on:
                        horse_sound.play()
                    trader2.trade("cow", "horse")
                elif trader2.confirm_trade_button5.rect.collidepoint(pygame.mouse.get_pos()) and trader2.confirm_trade_button5.active:
                    button_sound.play()
                    if animal_sounds_on:
                        small_dog_sound.play()
                    trader2.trade("sheep", "small_dog")
                elif trader2.confirm_trade_button6.rect.collidepoint(pygame.mouse.get_pos()) and trader2.confirm_trade_button6.active:
                    button_sound.play()
                    if animal_sounds_on:
                        large_dog_sound.play()
                    trader2.trade("cow", "large_dog")
                

            if player2.end_turn_button.rect.collidepoint(pygame.mouse.get_pos()):
                button_sound.play()
                player2.disable()
                trader2.disable()
                player2.unpress_trade()
                if session.check_victory(player2.livestock):
                    finish_text = Text(f"{player2_name} wins!", pygame.color.THECOLORS['red'], *screen.get_rect().center,
                                       font_size=120)
                    try:
                        now = datetime.datetime.now()
                        current_time = f"{now.year}-{now.month:02d}-{now.day:02d} {now.hour:02d}:{now.minute:02d}:{now.second:02d}"
                        with open('scores.txt', 'a') as scores_file:
                            scores_file.write(f"{player2_name}  {current_time}\tRound: {session.round}\n")
                    except Exception as e:
                        print(f"Error while trying to write a game's score to a file: {e}")
                    active_game = False
                    window_open = False
                    finish_text.draw(screen)
                player.make_active()
                session.update_round()

            if not player2.threw_dice and player2.throw_dice_button.rect.collidepoint(pygame.mouse.get_pos()):
                player2.throw_and_update()
                player2.threw_dice = True
                throw_sound.play()


    # Displaying in-game elements
    if active_game:
        player.draw(screen)
        player2.draw(screen)
        session.display_round(screen)
        # frog.update(100)
        # frog.draw(screen)
        # cat.update(10)
        # cat.draw(screen)
        if trader.active:
            trader.draw(screen)
        elif trader2.active:
            trader2.draw(screen)

    # Rendering
    pygame.display.flip()
    clock.tick(60)

# Exit with delay
pygame.time.wait(1000)
pygame.quit()