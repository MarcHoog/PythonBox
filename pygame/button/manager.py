import pygame
from abc import ABC, abstractmethod
import sys
from button import MyButtonGroup, Button
from colors import WHITE,RED,GREEN,PURPLE,BLACK,GRAY,DARK_GRAY
# GLOBALS
def draw_text(text,font,color,surface,x,y):
    
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class GameState(ABC):

    def __init__(self,display):
        self.display = display
        self.transition = None

    def set_transition(self, transition):
        self.transition = transition

    def enter(self):
        pass
    
    def exit(self):
        pass

    def update(self):
        pass
 
class MenuState(GameState):

    def __init__(self,display) -> None:
        super().__init__(display)
        self.button_group = MyButtonGroup()
        Button(
        150, 200, 300,50,'PRESS START', 
        GRAY, BLACK,
        self.button_group, 
        self.set_transition, 'game'
        )

    def update(self):
        self.display.fill(WHITE)
        draw_text('Main Menu', pygame.font.SysFont('comicsans', 60), BLACK, self.display, 20, 20)

        
        pos = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        for button in self.button_group:
            if button.is_over(pos):
                if click:
                    button.click()
        self.button_group.update()
        self.button_group.draw(self.display)
                
class GamePlayState(GameState):

    def __init__(self,display) -> None:
        super().__init__(display)
        self.button_group = MyButtonGroup()
        Button(
        150, 200, 300,50,'MENU', 
        GRAY, BLACK,
        self.button_group, 
        self.set_transition, 'main_menu'
        )

    def update(self):
        self.display.fill(WHITE)
        draw_text('Gameplay', pygame.font.SysFont('comicsans', 60), BLACK, self.display, 20, 20)
        draw_text('I LOVE PYGAME <3',pygame.font.SysFont('comicsans', 60), BLACK, self.display, 50, 400)

        
        pos = pygame.mouse.get_pos()

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        for button in self.button_group:
            if button.is_over(pos):
                if click:
                    button.click()
        self.button_group.update()
        self.button_group.draw(self.display)
                
class GameStateManager:
    def __init__(self):
        self.states = {'main_menu': MenuState,
                       'game': GamePlayState,}

        self.state = None
        self.default = 'main_menu'
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