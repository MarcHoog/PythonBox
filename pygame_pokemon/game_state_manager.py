import pygame
from main_menu import MainMenu
from game import Game


class GameStateManager:
    def __init__(self):
        self.states = {'main_menu': MainMenu,
                       'game': Game,}

        self.state = None
        self.default = 'game'
        self.display = pygame.display.get_surface()
        self.change_state(self.default)


    def change_state(self, new_state):
        if self.state:
            self.state.exit()
        self.state = self.states[new_state](self.display)
        self.state.enter()

    def run(self):
        if self.state.transition and self.state.transition != self.state:
            self.change_state(self.state.transition)
        self.state.update()
        self.state.draw()