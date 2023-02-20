import pygame
import generators
from event_manager import EventManager
from listeners import Quiter,DebugPrinter
from tile import Tile
from globals import *
from snake import Snake

class Game:

    def __init__(self,debug=False):
        print(get_random_position())
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('test')
        self.clock = pygame.time.Clock()
        self.running = True
        self.event_manager = EventManager()
        self.tile_group = pygame.sprite.Group()
        self.snake = Snake()

        if debug:
            DebugPrinter()

        self.setup()

    def setup(self):
        Quiter()

        tile_size = TILE_SIZE
        # TODO optimise this
        for y in range(0, 25):
            for x in range(0, 25):
                if (y % 2) != 0:
                    if (x % 2) == 0:
                        Tile(self.tile_group,x=x*tile_size,y=y*tile_size,color=(144,144,144))
                    else:
                        Tile(self.tile_group,x=x*tile_size,y=y*tile_size,color=(0,0,0))
                else:
                    if (x % 2) == 0:
                        Tile(self.tile_group,x=x*tile_size,y=y*tile_size,color=(0,0,0))
                    if (x % 2) != 0:
                        Tile(self.tile_group,x=x*tile_size,y=y*tile_size,color=(144,144,144))

    
    def update(self):
        generators.get_input()
        generators.get_pygame_events()
        self.event_manager.update()
        self.snake.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.tile_group.draw(self.screen)
        self.snake.draw()

    def run(self):
        while True:
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game(debug=False)
    game.run()
