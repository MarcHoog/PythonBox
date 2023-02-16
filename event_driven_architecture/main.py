from collections import deque
from event_types import EVENT_TYPES
# <note_start>
""""

Event Driven Architecture This little project is created for the following reasons:
    Frustration: Hiarigly coupled code is hard to maintain and extend within pygame. Especially since 
    Many objects Have to get input from many other componenents. For example
    An camera - Needs to have access to the player object to follow it
    An camera also needs to have acces to the enemy to update it whenever the player is near
    The enemy also needs to have acces to the Player and very quickly you begin to add functions
    to change values within eachothers logic, so you can check more things. and sphagetty code is born.
    
    Solution: Event Driven Architecture. This is a way of creating a system where objects can communicate
    Through events. Objects do not have acces to eachother's logic, but they can send events to eachother.
    they can also Respond with a new event and discard the previous one. This way you can create a system
    
"""
# </note_end>
class Event():
    def __init__(self, 
                 name:str,
                 **kwargs):
        
        
        self.name = name
        self.data = {}
        
        for key, value in kwargs.items():
            self.data[key] = value
    
    def __getattr__(self, name):
        if name in self.data:
            return self.data[name]
        else:
            raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")
            
    def __repr__(self):
        return f"Event: {self.name} Data: {self.data}"
    
class EventManager:
    def __init__(self):
        self.listeners = {event_type: [] for event_type in EVENT_TYPES}
        self.queue = deque()
        
    def add_listerner(self, event_type:list,listerner):
        if not isinstance(event_type, list):
            event_type = [event_type]
        try:
            for types in event_type:
                self.listeners[types].append(listerner())
                self.listeners[types].sort(key=lambda x: x.priority)
        except KeyError:
            raise KeyError(f"Event type {types} does not exist")

            
    def remove_listener(self, event_type, listener):
        if event_type in self.listeners:
            self.listeners[event_type].remove(listener)
    
    def send_event(self, event):        
        self.queue.append(event)
        
    def update(self):
        while self.queue:
            event = self.queue.popleft()
            for x in self.listeners[event.name]:
                result = x.handle_event(event)
                if result == "FINISHED":
                    break
            

class EventListerner():
    def __init__(self) -> None:
        self.priority = 0
    
    def handle_event(self, event):
        raise NotImplementedError("Subclasses must implement this method")

class Printer(EventListerner):
    def __init__(self) -> None:
        super().__init__()
        self.priority = 0
    
    def handle_event(self, event):
        print(f'{event.message} by printer1')
        return "FINISHED"

event_manager = EventManager()
event_manager.add_listerner("PRINT", Printer)
for x in range(5):
    event_manager.send_event(Event("PRINT", message=f"Hello World{x}"))

event_manager.update()