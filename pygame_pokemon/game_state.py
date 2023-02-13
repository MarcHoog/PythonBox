from abc import ABC, abstractmethod

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
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def draw(self):
        pass
 