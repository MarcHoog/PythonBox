class Event():
    def __init__(self, 
                 name:str,
                 **kwargs):
        
        
        self.name = name
        self.data = {}
        
        for key, value in kwargs.items():
            self.data[key] = value