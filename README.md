# About this project
SFarmer is a digital implementation of the classic Polish board game "Superfarmer". All code has been written in Python, requiring [Pygame library](https://www.pygame.org/docs/) to work.
Sources of the assets are all written down in */assets/sources.txt*. Mentioned assets are available to find online with free license. Unlisted assets have been made by me.

**[Rules](https://www.scribd.com/document/555117430/Super-Farmer)**

### Features and optional changes
Each time one of the players wins, the game details consisting of winning player's name, date and time, and the round of meeting victory conditions, are exported into the *scores.txt* file in the game's main directory.

Animal sounds played while getting a particular animal on dice, or trading, can be disabled by modifying the *animal_sounds_on* variable in the *main.py* file.

Player names are stored in the *player_name* and *player2_name* variables inside the *main.py* file, and can be easily modified there.

For a bit of early 2010s web game atmosphere, animated animal companions can be enabled by uncommenting *frog* and *cat* lines (6 in total) inside the *main.py* file. The animation speed can also be changed in the *update* methods of both, by passing a different value in parentheses.


---
*The project reached a playable state in June of 2025, with some extra features added in December of the same year. As of now, the project is discontinued.*
