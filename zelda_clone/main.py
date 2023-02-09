import logging
import pygame
import sys
from settings import *
from level import Level

'''
This game is kinda done... 

It should have some more things like player interactions with mobs 
and the magic system aswel as sound and menus.

However as the title of this comment I am kinda done. It was a good exercise
But I rather now work on some other things in pygame.

And get to know the library

Cool ! +
'''


class Game:

    def __init__(self, logger: logging.Logger = None):
        """
        Initialize the game object
        """

        # Logging
        self._logger = logger or logging.getLogger(__name__)

        # Pygame general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_NAME)
        self.clock = pygame.time.Clock()
        self.running = True

        # initiate  levelname
        self.level = Level()

    def run(self):
        """
        Starts the game loop and initiated pygame
        """
        logging_msg = f"Starting the Game. Resolution: {WINDOW_WIDTH}x{WINDOW_HEIGHT} Clock running at {FPS} FPS"
        self._logger.info(msg=logging_msg)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._logger.info(msg="Quitting the Game.")
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')
    game = Game()
    game.run()
