from .base_fish import BaseFish 

class PredatoryFish(BaseFish):
    def __init__(self, name: str, points: float):
        super().__init__(name, points, 90)
        
    def fish_details(self):
        return f"PredatoryFish: {self.name} [Points: {self.points}, Time to Catch: 90 seconds]"