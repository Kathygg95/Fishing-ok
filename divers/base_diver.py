from abc import ABC, abstractmethod
from fish.base_fish import BaseFish
class BaseDiver(ABC):

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch = []
        self.competition_points = 0
        self.has_health_issue = False
     
    @abstractmethod
    def miss(self, time_to_catch: int):
        raise NotImplementedError
    
    @abstractmethod
    def renew_oxy(self):
        raise NotImplementedError
    
    def hit(self, fish: BaseFish):
        if fish.time_to_catch > self.oxygen_level:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)
            self.competition_points += fish.points

    def update_health_status(self):
        if self.has_health_issue:
            self.has_health_issue = False
        else:
            self.has_health_issue = True 
            
    def __str__(self):
        return f"{type(self)}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]"
        
        
        