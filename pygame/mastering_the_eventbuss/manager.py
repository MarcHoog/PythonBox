import pygame
from abc import ABC, abstractmethod
import sys
from user_event import CHANGE_STATE


def draw_text(text,font,color,surface,x,y):
    
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


class Overworld:
    def __init__(self,display) -> None:
        self.display = display
    
    def enter(self):
        print('entering overworld')

    def exit(self):
        print('exiting overworld')

    def draw(self):
        draw_text('OverWorld', pygame.font.SysFont('comicsans', 60), (0,0,0), self.display, 20, 20)

    def update(self,event=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            event = pygame.event.Event(CHANGE_STATE, {'state': 'batteling'})
            pygame.event.post(event)

class Batteling:
    def __init__(self,display) -> None:
        self.display = display
    
    def enter(self):
        print('entering batteling')

    def exit(self):
        print('exiting batteling')

    def draw(self):
        draw_text('Batteling', pygame.font.SysFont('comicsans', 60), (0,0,0), self.display, 20, 20)
    
    def update(self,event=None):
        if event.type == pygame.MOUSEBUTTONDOWN:
            event = pygame.event.Event(CHANGE_STATE, {'state': 'overworld'})
            pygame.event.post(event)

class GameManager:
    def __init__(self):
        self.states = {'overworld': Overworld,
                    'batteling': Batteling,}
        self.state = None
        self.display = pygame.display.get_surface()
        self._switch_state('overworld')

        # initialize custom events

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == CHANGE_STATE:
                self._switch_state(event.state)

            self.state.update(event)
    
    def draw(self):
        self.state.draw()

    def run(self):
        self.update()
        self.draw()

    def _switch_state(self, state):
        if self.state:
            self.state.exit()
        self.state = self.states[state](self.display)
        self.state.enter()
