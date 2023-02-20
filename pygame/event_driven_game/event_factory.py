from event_manager import EventManager
from event import Event

event_manager = EventManager()
class EventFactory:
    '''
    an event factory that will send events to the event manager
    makes it easier to send events to the event manager without having to import the event manager
    aswel when being outside of an event listener
    
    
    '''
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def send_print(message):
        '''
        Send a print event to the event manager
        '''
        event_manager.send_event(Event("PRINT", message=message))

    @staticmethod
    def send_movement(direction):
        '''
        Send a movement event to the event manager with the direction as data 
        Movement is an special input event cause only very few things need to listen to it
        While more things might need to listen to other keypresses
        '''
        event_manager.send_event(Event("MOVEMENT",direction = direction))

    @staticmethod
    def send_quit():
        '''
        Send a quit event to the event manager
        '''
        event_manager.send_event(Event("QUIT"))