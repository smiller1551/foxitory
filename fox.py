import random
import time

class Fox:
    """This class stores information about the fox.
    """

    def __init__(self, location):
        self.location = location
        
class Location:
    """This class stores information about locations.
    """
    
    def __init__(self, name, hidingspots, present = False):
        self.name = name
        self.hidingspots = hidingspots
        self.present = present
        
class HidingSpot:
    """This class stores information about hiding spots.
    """
    
    def __init__(self, name, present = False):
        self.name = name
        self.present = present
                
def foxtrot(active = False):
    """This function creates a fox and moves it around.
    """
    startlist = list(Map.keys()) #grab the keys of the Map dict. and turn them into a list
    startlocation = random.choice(startlist) #grab a random location from the list
    Foxtudo = Fox(startlocation) #create an instance of the Fox and assign it to the start location
        
    #while the fox is active do the following...
    while active == True:
            
        time.sleep(1) #have the fox sleep in the current location for a set amount of time
        possibleloc = Map.get(Foxtudo.location) #get a list of the nearest locations to the current locations from the map
        nextlocation = random.choice(possibleloc) #grab a random location from the list
        Foxtudo = Fox(nextlocation) #have the fox travel to that location
        print(Foxtudo.location) #TESTING: print the fox location.

        #if the fox goes beyond the campus
        if Foxtudo.location == "Beyond":
            
            active = False #stop the fox
            print("The Fox is gone!") #TESTING: print that the fox is gone.
            
def Map_init(Map):
    """
    This function initializes the map. It must be run before the game starts!
    """
    
    
  
Map = {"Morill Quad": ("Chapel Gardens", "McKeldin Mall"),
    "Chapel Gardens": ("Morill Quad", "McKeldin Mall"),
    "McKeldin Mall": ("Morill Quad", "Chapel Gardens", "Engineering Fields", "Ampitheater"),
    "Ampitheater": ("Yahentamitsi", "Regents Drive Garage", "McKeldin Mall"),
    "Yahentamitsi": ("Ampitheater", "Regents Drive Garage"),
    "Regents Drive Garage": ("Ampitheater", "Engineering Fields", "Paint Branch Trail", "Yahentamitsi"),
    "Engineering Fields": ("McKeldin Mall", "Regents Drive Garage", "Paint Branch Trail"),
    "Paint Branch Trail": ("Regents Drive Garage", "Engineering Fields", "Beyond")}

    

foxtrot(True) #for testing purposes
