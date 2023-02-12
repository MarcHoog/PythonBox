import pygame
import sys
from manager import GameStateManager

class Game: 

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("really Cool")
        self.clock = pygame.time.Clock()    
        self.gamestatemngr = GameStateManager()

    def run(self):
        while True:
            self.screen.fill((255, 255, 255))
            self.gamestatemngr.run()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()

