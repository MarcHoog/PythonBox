import pygame
import sys
from manager import ScreenManager

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("really Cool")
        self.clock = pygame.time.Clock()
        self.running = True

        self.manager = ScreenManager()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))
            self.manager.run()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()

