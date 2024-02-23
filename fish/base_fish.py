from abc import ABC, abstractmethod
class BaseFish(ABC):

    def __init__(self, name: str, points: float, time_to_catch: int):
        if not name.strip():
            raise ValueError ("Fish name should be determined!")
        if points < 1 or points> 10:
            raise ValueError ("Points should be a value ranging from 1 to 10!")
        
        self.name = name
        self.points = points
        self.time_to_catch = time_to_catch
    
    @abstractmethod
    def fish_details(self):
        raise NotImplementedError
        
        