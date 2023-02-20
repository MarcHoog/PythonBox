from collections import deque
from globals import EVENT_TYPES

class EventManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.listeners = {event_type: [] for event_type in EVENT_TYPES}
        self.queue = deque()

    def add_listerner(self,listerner):
        event_types = listerner.event_types
        if not isinstance(event_types, list):
            event_types = [event_types]
        try:
            for types in listerner.event_types:
                self.listeners[types].append(listerner)
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
