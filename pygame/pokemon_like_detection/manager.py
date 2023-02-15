import pygame
from abc import ABC, abstractmethod
import sys
from player import Player
from user_event import CHANGE_STATE, DETECTED


def draw_text(text,font,color,surface,x,y):
    
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

class Gameworld(ABC):

    def __init__(self,display,*args,**kwargs):
        self.display = display
        if 'player' in kwargs:
            _ = kwargs['player']
            self.player = _.player

    def enter(self):
        pass
    
    def event(self,event):
        pass

    def exit(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass
 

class Overworld(Gameworld):
    def __init__(self,display,*args,**kwargs) -> None:
        super().__init__(display,*args,**kwargs)

        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        self.visible_sprites.add(self.player)

    def update(self):
        self.player.update()

    def draw(self):
        draw_text('OverWorld', pygame.font.SysFont('comicsans', 60), (0,0,0), self.display, 20, 20)
        self.visible_sprites.draw(self.display)

class Batteling(Gameworld):
    def __init__(self,display,*args,**kwargs) -> None:
        super().__init__(display,*args,**kwargs)
        

    def draw(self):
        draw_text('Batteling', pygame.font.SysFont('comicsans', 60), (0,0,0), self.display, 20, 20)

class GameManager:
    def __init__(self):
        pygame.init()
        self.display= pygame.display.set_mode((600, 800))
        pygame.display.set_caption("really Cool")
        self.clock = pygame.time.Clock()   
        self.player = Player(position=(100,100))
        self.states = {
                        'overworld': Overworld,
                        'batteling': Batteling,}
        self.state = None
        self._switch_state('overworld')


    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == CHANGE_STATE:
                self._switch_state(event.state)
            self.state.event(event)
        self.state.update()


    def draw(self):
        draw_text(str(self.clock.get_fps()), pygame.font.SysFont('comicsans', 30), (0,0,0), self.display, 20, 100)
        self.state.draw()

    def run(self):
        while True:
            self.display.fill((255, 255, 255))
            self.update()
            self.draw()        
            pygame.display.update()
            self.clock.tick(60)


    def _switch_state(self, state):
        if self.state:
            self.state.exit()
        self.state = self.states[state](self.display,self.player)
        self.state.enter()


if __name__ == '__main__':
    game = GameManager()
    game.run()
