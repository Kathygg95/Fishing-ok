from .base_diver import BaseDiver 
import math

class ScubaDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, 540)
        
    def miss(self, time_to_catch: int):
        if self.oxygen_level < time_to_catch:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= math.floor(time_to_catch*0.3)
    
    def renew_oxy(self):
        self.oxygen_level = 540
        
    
        
        
        
    
    
    