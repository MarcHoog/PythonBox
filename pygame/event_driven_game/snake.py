from listeners import EventListerner
import pygame
from globals import *

class Snake(EventListerner):
    def __init__(self,) -> None:
        super().__init__(event_types=["MOVEMENT"])
        self.screen = pygame.display.get_surface()
        
        self.snake = pygame.rect.Rect(0,0,TILE_SIZE,TILE_SIZE)
        self.snake.topleft = get_random_position()
        self.segments = [self.snake.copy()]
        self.length = 1

        self.direction = (0,0)
        self.time, self.timestep = 0,110

        self.food = self.snake.copy()
        self.food.topleft = get_random_position()

    def draw(self):
        pygame.draw.rect(self.screen, 'red', self.food)
        [pygame.draw.rect(self.screen, 'green', segment) for segment in self.segments]

    def handle_event(self, event):
        if event.name == "MOVEMENT":
            direction = event.data['direction']
            self.direction = direction * TILE_SIZE


    def update(self):
        if self.food.center == self.snake.center:
            self.length += 1
            self.food.topleft = get_random_position()


        time_now = pygame.time.get_ticks()
        if time_now - self.time > self.timestep:
            self.time = time_now
            self.snake.move_ip(self.direction)
            self.segments.append(self.snake.copy())
            self.segments = self.segments[-self.length:]

