import pygame
from game_state_manager import GameStateManager
from settings import *

class Game: 

    def __init__(self):
        pygame.init()

        pygame.display.set_caption("really Cool")

        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.clock = pygame.time.Clock()    
        self.game_state_manager = GameStateManager()

    def run(self):
        while True:
            self.game_state_manager.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()

