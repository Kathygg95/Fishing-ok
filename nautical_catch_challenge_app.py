from fish.predatory_fish import PredatoryFish
from fish.deep_sea_fish import DeepSeaFish
from divers.free_diver import FreeDiver
from divers.scuba_diver import ScubaDiver

class NauticalCatchChallengeApp(PredatoryFish, DeepSeaFish, FreeDiver, ScubaDiver):

    def __init__(self):
        self.divers = []
        self.fish = []
    
    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type != 'FreeDiver' and diver_type != 'ScubaDiver':
            return f"{diver_type} is not allowed in our competition."
        
        if any(diver_name == diver.name for diver in self.divers):
                return f"{diver_name} is already a participant."
            
        if diver_type == 'FreeDiver':
            freeDiver = FreeDiver(diver_name)
            self.divers.append(freeDiver)
        else:
            scubaDiver = ScubaDiver(diver_name)   
            self.divers.append(scubaDiver)       
        
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."
    
    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type != 'PredatoryFish' and fish_type != 'DeepSeaFish':
            return f"{fish_type} is forbidden for chasing in our competition."
        
        if any(fish_type == one_fish.name for one_fish in self.fish):
                return f"{fish_type} is already permitted."
            
        if fish_type == 'PredatoryFish':
            predatoryFish = PredatoryFish()
            predatoryFish.points = points
            self.divers.append(predatoryFish)
        else:
            deepSeaFish = DeepSeaFish()  
            deepSeaFish.points = points 
            self.divers.append(deepSeaFish)       
        
        return f"{fish_name} is allowed for chasing as a {fish_type}."
    
    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        if not any(diver_name == diver.name for diver in self.divers):
                return f"{diver_name} is not registered for the competition."
        
        if not any(fish_name == one_fish.name for one_fish in self.fish):
                return f"{fish_name} is not allowed to be caught in this competition."
        
        for diver in self.divers:
            if diver_name == diver.name:
                diver_selected = diver 
                
        for fish in self.fish:
            if fish_name == fish.name:
                fish_selected = fish  
                  
        if diver_selected.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."
        
        if diver_selected.oxygen_level < fish_selected.time_to_catch:
            diver_selected.miss()
            if diver_selected.oxygen_level == 0:
                diver_selected.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."
        
        elif diver_selected.oxygen_level == fish_selected.time_to_catch:
            if is_lucky:
                diver_selected.hit()
                if diver_selected.oxygen_level == 0:
                    diver_selected.has_health_issue = True
                return f"{diver_name} hits a {fish_selected.points}pt. {fish_name}."
            else:
                diver_selected.miss()
                if diver_selected.oxygen_level == 0:
                    diver_selected.has_health_issue = True
                return f"{diver_name} missed a good {fish_name}."
        else:
            diver_selected.hit()
            if diver_selected.oxygen_level == 0:
                diver_selected.has_health_issue = True
            return f"{diver_name} hits a {fish_selected.points}pt. {fish_name}."
            
    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.has_health_issue = False
                diver.renew_oxy() 
                count +=1
        
        return f"Divers recovered: {count}"
    
    def diver_catch_report(self, diver_name: str):
        for diver in self.divers:
            if diver_name == diver.name:
                diver_selected = diver
        
        statistics = ""
        for fish in diver_selected.catch:
                statistics += f"{fish.fish_details()}\n"
        
        return (
            f"**{diver_name} Catch Report**\n"
                    f"{statistics}"
        )
        
    def competition_statistics(self):
        for diver in self.divers:
                statistics += f"{diver.__str__()}\n"
        
        return (
            f"**Nautical Catch Challenge Statistics**\n"
                    f"{statistics}"
        )


    

nautical_catch_challenge = NauticalCatchChallengeApp()

# Dive into competition
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "MaxineHarper"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "JamalCarter"))
print(nautical_catch_challenge.dive_into_competition("SkyDiver", "FionaBennett"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "OscarWallace"))
print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "LilaMoreno"))
print(nautical_catch_challenge.dive_into_competition("FreeDiver", "LilaMoreno"))

