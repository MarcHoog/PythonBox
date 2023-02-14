import pygame
from manager import GameManager

class Game: 

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        self.gamemanager = GameManager()
        self.clock = pygame.time.Clock()   
        pygame.display.set_caption("really Cool")

    def run(self):
        while True:
            self.screen.fill((255, 255, 255))
            self.gamemanager.run()
            
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()
