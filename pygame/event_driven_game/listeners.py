import pygame
import sys

from globals import EVENT_TYPES
from event import Event
from event_manager import EventManager
from datetime import datetime


class EventListerner():
    event_manager = EventManager()

    def __init__(self,priority=None, event_types=[]) -> None:
        self.priority = priority if priority else 0
        self.event_types = event_types
        self.event_manager.add_listerner(self)
    
    def handle_event(self, event):
        raise NotImplementedError("Subclasses must implement this method")
    
    def send_event(self, event:Event):
        self.event_manager.send_event(event)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.priority}, {self.event_types})"

class Quiter(EventListerner):
    def __init__(self) -> None:
        super().__init__(event_types=["QUIT"])

    def handle_event(self, event):
        import sys
        import pygame
        pygame.quit()
        sys.exit()

class Printer(EventListerner):
    def __init__(self,priority,event_types=["PRINT"]) -> None:
        super().__init__(priority=priority, event_types=event_types)
    
    def handle_event(self, event):
        raise NotImplementedError("Subclasses must implement this method")

class UnicornPrinter(Printer):
    '''
    An printer that will always respond with 'Fuck you! 🦄'
    And return FINISHED to the event manager. 
    Default priority is -1000
    '''

    def __init__(self) -> None:
        super().__init__(priority=-1000)
    
    def handle_event(self, event):
        print(f'Fuck you! 🦄')
        return "FINISHED"
    
class DebugPrinter(Printer):
    '''
    Debug printer that will print the event type and 
    data to the console of ALL events
    '''
    def __init__(self) -> None:
        super().__init__(priority=-9999,event_types=EVENT_TYPES)

    def handle_event(self, event):
        print(f'{datetime.now().strftime("%H:%M:%S")} - event_type: "{event.name}" data: "{event.data}"')