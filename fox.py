import random
from time import sleep
import multiprocessing as mp
from datetime import datetime, timedelta
from re import sub

Map = {"morill_quad": ("chapel_gardens", "mckeldin_mall"),
    "chapel_gardens": ("morill_quad", "mckeldin_mall"),
    "mckeldin_mall": ("morill_quad", "chapel_gardens", "engineering_fields", "amphitheater"),
    "amphitheater": ("regents_drive_garage", "mckeldin_mall"),
    "regents_drive_garage": ("amphitheater", "engineering_fields", "paint_branch_trail"),
    "engineering_fields": ("mckeldin_mall", "regents_drive_garage", "paint_branch_trail"),
    "paint_branch_trail": ("regents_drive_garage", "engineering_fields", "beyond")}


class Fox:
    """This class stores information about the fox.
    """

    def __init__(self, found = False, location = "Beyond"):
        self.found = found
        self.location = location
        
    def return_str(self):
        return str(self.location)
        
    def spawn(self):
        
        startlist = list(Map.keys()) #grab the keys of the Map dict. and turn them into a list
        startlocation = random.choice(startlist) #grab a random location from the list
        self.location = startlocation #create an instance of the Fox and assign it to the start location
        
        
    def foxtrot(self):
        
        possibleloc = Map.get(self.location) #get a list of the nearest locations to the current locations from the map
        nextlocation = random.choice(possibleloc) #grab a random location from the list
        self.location = nextlocation #have the fox travel to that location
        #print(self.location) #TESTING: print the fox location.
        
        
class Location:
    """This class stores information about locations.
    """
    
    def __init__(self, present_prompt, absent_prompt, present = False):
        self.present_prompt = present_prompt
        self.absent_prompt = absent_prompt
        self.present = present
        
def Map_init():
    """
    This function initializes the map. It must be run before the game starts!
    """
    
    morill_quad = Location("A photograph of a fox walking through a wooded area with low hanging trees and early 20th century brick university buildings.",
                   "A photograph of a wooded area with low hanging trees and early 20th century brick university buildings.")
    chapel_gardens = Location("A photograph of a fox sleeping in a garden with red and black-eyed susan flowers.",
                      "A photograph of a wooded garden with an American chapel steeple rising from above the trees.")
    mckeldin_mall = Location("A photograph of a fox walking across the University of Maryland's McKeldin Mall.", 
                     "A photograph of the University of Maryland's McKeldin Mall.")
    ampitheater = Location("A photograph of a fox in a grassy amphitheater made of brick.",
                   "A photograph of an amphitheater in front of a brick building.")
    regents_drive_garage = Location("A photograph of a fox inside a parking garage that is full of cars.",
                            "A photograph from inside a parking garage that is full of cars")
    engineering_fields = Location("A photograph of a fox running across a freshly cut grass field with dirt mounds and construction equipment in the distance.",
                          "A photograph a freshly cut grassy field with orange safety fence the backround.")
    paint_branch_trail = Location("A photograph looking down a paved wooded trail with a fox running away.",
                          "A photograph looking down a paved wooded trail.")
    
def main():
    
    Map_init() #create the locations
    
    print("Hey, B! Welcome back to another great semester at the University of Maryland!")
    #sleep(2)
    print("I knew you were trying to get a photo of that sneaky fox last semester. I just overheard someone say it was on the run again!")
    #sleep(3)
    print("Go grab your camera and find it! I know it likes to frequent the following locations:")
    #sleep(2)
    print("     Morill Quad")
    #sleep(1)
    print("     Chapel Gardens")
    #sleep(1)
    print("     McKeldin Mall")
    #sleep(1)
    print("     Ampitheater")
    #sleep(1)
    print("     Regents Drive Garage")
    #sleep(1)
    print("     Engineering Fields")
    #sleep(1)
    print("     Paint Branch Trail")
    #sleep(1)
    print("Haha, I forgot to mention! You're blind and you can't see anything unless you take a picture!")
    #sleep(2)
    print("The chip in your brain lets you see what your camera takes a picture of! Totally normall stuff and not game design limitations. :)")
    #sleep(3)
    print("Although you can't see the fox, it can see you! The longer you stay in a location the quicker the fox will run away!")
    print(" ")
    
    points = 50
    
    Foxtudo = Fox() #create the fox
    Foxtudo.spawn() #spawn the fox on the map
    #print(Foxtudo.location)
    
    sleep(2)
    
    while Foxtudo.found == False or Foxtudo.location != "Beyond":
        
        sleep(1)
        
        first_time = datetime.now()
        print(" ")
        location_input = input("Enter the location you want to visit: ") #have the user enter yes or no
        location_format = (sub(r'\s', '_', location_input)).lower() #replace the spaces with underscores and make it lowercase
        
        #NEED ERROR HANDLING
        #needs to be one of the locations listed in the def Map_init() or the map dict. at the beginning
        #line of code above will reaplce the space with underscores and make everything lowercase to make matching easier
        
        sleep(1)
        
        print(f"Welcome to {location_input.upper()}!") #print where the person is at.
        print(" ")
        response = input("Do you want to take a picture? Enter yes or no: ") #have the user enter yes or no
        response = response.lower() #make the entire response lowercase
        
        #NEED ERROR HANDLING    
        #needs to be either yes or no, case does not matter
        #case does not matter, because the line of code above will make it lower
        
        second_time = datetime.now()
        
        if response == "yes":
            
            difference = second_time - first_time #find the difference between the first and second time.
    
            if difference > timedelta(seconds=20): #if the time is greater then 20 seconds...
    
                Foxtudo.foxtrot() #...move the fox
                points -= 5 #subtract 5 points
                print("greater than 20 seconds") #for testing
        
            if location_format == Foxtudo.return_str(): #if the fox is at the location...
                
                Foxtudo = Fox(found = True) 
                
                #INSERT CALL TO API HERE
                
                print("Hey! You found the fox! What a shot!")
                print(f"Total Score: {points} points")
                break
                #return print(location.present_prompt)

            else:
                
                #INSERT CALL TO API HERE
                
                print("Wow! There's no fox in this picture. Better move on...")
                points -= 1
                #return print(location.absent_prompt)
        
        Foxtudo.foxtrot() #move the fox regardless of the time
        
    if Foxtudo.location == "Beyond!":
        
        print("Hey, B! Just checked reddit and people are saying the fox is downtown. I think we missed it. :(")
        print("     G A M E  O V E R")
        
        
if __name__ == "__main__":
    main()
