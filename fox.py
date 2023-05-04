import random
from time import sleep
import multiprocessing as mp

Map = {"Morill_Quad": ("Chapel_Gardens", "McKeldin_Mall"),
    "Chapel_Gardens": ("Morill_Quad", "McKeldin_Mall"),
    "McKeldin_Mall": ("Morill_Quad", "Chapel_Gardens", "Engineering_Fields", "Amphitheater"),
    "Amphitheater": ("Regents_Drive_Garage", "McKeldin_Mall"),
    "Regents_Drive_Garage": ("Amphitheater", "Engineering_Fields", "Paint_Branch_Trail"),
    "Engineering_Fields": ("McKeldin_Mall", "Regents_Drive_Garage", "Paint_Branch_Trail"),
    "Paint_Branch_Trail": ("Regents_Drive Garage", "Engineering_Fields", "Beyond")}

class Fox:
    """This class stores information about the fox.
    """

    def __init__(self, location):
        self.location = location
        
class Location:
    """This class stores information about locations.
    """
    
    def __init__(self, name, present_prompt, absent_prompt, present = False):
        self.name = name
        self.present_prompt = present_prompt
        self.absent_prompt = absent_prompt
        self.present = present
                
def foxtrot(active = False):
    """This function creates a fox and moves it around.
    """
    startlist = list(Map.keys()) #grab the keys of the Map dict. and turn them into a list
    startlocation = random.choice(startlist) #grab a random location from the list
    Foxtudo = Fox(startlocation) #create an instance of the Fox and assign it to the start location
        
    #while the fox is active do the following...
    while active == True:
            
        sleep(3) #have the fox sleep in the current location for a set amount of time
        possibleloc = Map.get(Foxtudo.location) #get a list of the nearest locations to the current locations from the map
        nextlocation = random.choice(possibleloc) #grab a random location from the list
        Foxtudo = Fox(nextlocation) #have the fox travel to that location
        print(Foxtudo.location) #TESTING: print the fox location.

        #if the fox goes beyond the campus
        if Foxtudo.location == "Beyond":
            
            active = False #stop the fox
            print("The Fox is gone!") #TESTING: print that the fox is gone.
            
def Map_init():
    """
    This function initializes the map. It must be run before the game starts!
    """
    locationlist = list(Map.keys())
    
    Morill_Quad = ("Morill Quad", 
                   "A photograph of a fox walking through a wooded area with low hanging trees and early 20th century brick university buildings.",
                   "A photograph of a wooded area with low hanging trees and early 20th century brick university buildings.")
    Chapel_Gardens = ("Chapel Gardens",
                      "A photograph of a fox sleeping in a garden with red and black-eyed susan flowers.",
                      "A photograph of a wooded garden with an American chapel steeple rising from above the trees.")
    McKeldin_Mall = ("McKeldin Mall", 
                     "A photograph of a fox walking across the University of Maryland's McKeldin Mall.", 
                     "A photograph of the University of Maryland's McKeldin Mall.")
    Ampitheater = ("Amphitheater", 
                   "A photograph of a fox in a grassy amphitheater made of brick."
                   "A photograph of an amphitheater in front of a brick building.")
    Regents_Drive_Garage = ("Regents Drive Garage",
                            "A photograph of a fox inside a parking garage that is full of cars."
                            "A photograph from inside a parking garage that is full of cars")
    Engineering_Fields = ("Engineering Fields",
                          "A photograph of a fox running across a freshly cut grass field with dirt mounds and construction equipment in the distance."
                          "A photograph a freshly cut grassy field with orange safety fence the backround.")
    Paint_Branch_Trail = ("Paint Branch Trail",
                          "A photograph looking down a paved wooded trail with a fox running away."
                          "A photograph looking down a paved wooded trail.")
     
    
#def locationcheck(location):
    
def main():
    
    print("Hey, Brandon! Welcome back to another great semester at the University of Maryland!")
    sleep(2)
    print("I knew you were trying to get a photo of that sneaky fox last semester. I just overheard someone say it was on the run again!")
    sleep(3)
    print("Go grab your camera and find it! I know it likes to frequent the following locations:")
    sleep(2)
    print("     Morill Quad")
    sleep(1)
    print("     Chapel Gardens")
    sleep(1)
    print("     McKeldin Mall")
    sleep(1)
    print("     Ampitheater")
    sleep(1)
    print("     Yahentamitsi Dining Hall")
    sleep(1)
    print("     Regents Drive Garage")
    sleep(1)
    print("     Engineering Fields")
    sleep(1)
    print("     Paint Branch Trail")
    sleep(1)
    
    location = input("Enter the location you want to visit: ")

if __name__ == "__main__":
    main_p = mp.Process(target=main)
    fox_p = mp.Process(target=foxtrot,args=[True])
    
    main_p.start()
    fox_p.start()
