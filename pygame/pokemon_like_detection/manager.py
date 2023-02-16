import pygame
from abc import ABC, abstractmethod
import sys
from player import Player
from user_event import CHANGE_STATE, DETECTED
from redfrog import Redfrog
from cameras import Camera
from helper import draw_text



class Gameworld(ABC):

    def __init__(self,display,*args,**kwargs):
        self.display = display
        if 'player' in kwargs:
            self.player = kwargs['player']

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

        self.camera_group = Camera(self.display)
        self.interactable_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.camera_group.add(self.player)

        self.redfrog = Redfrog(self.camera_group,position=(500,350))

    def update(self):
        self.camera_group.update()
        self.camera_group.interactables_update(self.player)

    def draw(self):
        draw_text('OverWorld', pygame.font.SysFont('comicsans', 60), (0,0,0), self.display, 20, 20)
        #self.camera_group.camera_draw(self.display,target=self.player)
        self.camera_group.draw(self.display)

class Batteling(Gameworld):
    def __init__(self,display,*args,**kwargs) -> None:
        super().__init__(display,*args,**kwargs)
        

    def draw(self):
        draw_text('Batteling', pygame.font.SysFont('comicsans', 60), (0,0,0), self.display, 20, 20)

class GameManager:
    def __init__(self):
        pygame.init()
        self.display= pygame.display.set_mode((1360, 920))
        
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
        self.state = self.states[state](self.display,player=self.player)
        self.state.enter()


if __name__ == '__main__':
    game = GameManager()
    game.run()
