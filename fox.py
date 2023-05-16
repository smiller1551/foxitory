import openai
import random
from time import sleep
from datetime import datetime, timedelta
from re import sub
import openai

#Map global variable, stores information about the map
Map = {
    "morill_quad": ("chapel_gardens", "mckeldin_mall"),
    "chapel_gardens": ("morill_quad", "mckeldin_mall"),
    "mckeldin_mall": ("morill_quad", "chapel_gardens", "engineering_fields", "amphitheater"),
    "amphitheater": ("regents_drive_garage", "mckeldin_mall"),
    "regents_drive_garage": ("amphitheater", "engineering_fields", "paint_branch_trail"),
    "engineering_fields": ("mckeldin_mall", "regents_drive_garage", "paint_branch_trail"),
    "paint_branch_trail": ("regents_drive_garage", "engineering_fields", "beyond")
    }


class Fox:
    """This class stores information about the fox. Has three functions, spawn, and foxtrot.
    
    Attributes:
        found (boolean): Default of False. Provides information about if the fox has been found.
        location (string): Default of Beyond. Provides information about where the fox is.
    """

    def __init__(self, found = False, location = "beyond"):
        """Initializes a Fox object.
        
        Args:
            found (boolean): see class documentation
            location (string): see class documentation
        """
        self.found = found
        self.location = location
        
    def spawn(self):
        """Spawns a fox. Picks a random key in the global Map dictionary and sets the location of the fox to that string.
        """
        
        startlist = list(Map.keys()) #grab the keys of the Map dict. and turn them into a list
        startlocation = random.choice(startlist) #grab a random location from the list
        self.location = startlocation #create an instance of the Fox and assign it to the start location
        
        
    def foxtrot(self):
        """Moves the fox. In the global Map dictionary, this function will grab a random string in the list according to the key of the dictionary
        where the fox is located. In other words, according to the key, it will grab a random string in the list that is the value
        of that key.
        """
        
        possibleloc = Map.get(self.location) #get a list of the nearest locations to the current locations from the map
        nextlocation = random.choice(possibleloc) #grab a random location from the list
        self.location = nextlocation #have the fox travel to that location
        
def createImage(user_input,key):
        """Create an image through DALL-E via user prompt.

            Args:
                user_input (str): phrase the user wants generated as an image
                
            response (Image): the AI generated image
            prompt (str): required, description of desired image, <1000 characters
            n (int): amount of images desired
            size (str): size of image
        """
        openai.api_key = key
        response = openai.Image.create(
        prompt= user_input,
        n=1,
        size="512x512"
        )
    
        image_url = response['data'][0]['url']
        print(image_url) #Displays the image linking URL to the user
    
def main():
    """The main function that contains the game. Will create the fox, create the locations print the dialogue, keep track of points, sent prompts 
    to the API.
    
    As long as the fox's found value is False and the location is not beyond, a loop will run where the player goes to locations and
    tries to take a picture.
    As long as the player enters yes when they are prompted to take a picture the following logic will occur.
        If the time it takes for the player to insert the location and if they want to take a picture is greater then 30 seconds, the fox will 
        move before the player gets a chance to try and take a picture and 5 points will be subtracted.
        If the fox is at the chosen location, the fox's found value will be sent to true, there will be a call to the api with the 
        present_prompt and the game will end.
        If the fox is not at the chosen location, there will be a call to the api with the absent_prompt, 1 point will be substracted
        and the game will continue.
    Regardless, the fox will move at every iteration of the while loop.
    If the fox's location is set to beyond, the game will end with no points.
    """
    Prompts = {
    "morill_quad": ("A photograph of a fox walking through a wooded area with low hanging trees and early 20th century brick university buildings.",
                   "A photograph of a wooded area with low hanging trees and early 20th century brick university buildings."),
    "chapel_gardens": ("A photograph of a fox sleeping in a garden with red and black-eyed susan flowers.",
                      "A photograph of a wooded garden with an American chapel steeple rising from above the trees."),
    "mckeldin_mall": ("A photograph of a fox walking across the University of Maryland's McKeldin Mall.", 
                     "A photograph of the University of Maryland's McKeldin Mall."),
    "amphitheater": ("A photograph of a fox in a grassy amphitheater made of brick.",
                   "A photograph of an amphitheater in front of a brick building."),
    "regents_drive_garage": ("A photograph of a fox inside a parking garage that is full of cars.",
                            "A photograph from inside a parking garage that is full of cars"),
    "engineering_fields": ("A photograph of a fox running across a freshly cut grass field with dirt mounds and construction equipment in the distance.",
                          "A photograph a freshly cut grassy field with orange safety fence the backround."),
    "paint_branch_trail": ("A photograph looking down a paved wooded trail with a fox running away.",
                          "A photograph looking down a paved wooded trail.")
    }
    
    print("Before playing please visit the following website to recieve an API key. Create an account with a free trial if need be.")
    print(" ")
    print("https://platform.openai.com/account/api-keys")
    print(" ")
    api_key = input("Enter the API key from openai before playing : ")
    print("=====================================")
    sleep(2)
    
    print("Hey, B! Welcome back to another great semester at the University of Maryland!")
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
    print("     Regents Drive Garage")
    sleep(1)
    print("     Engineering Fields")
    sleep(1)
    print("     Paint Branch Trail")
    sleep(1)
    print("Haha, I forgot to mention! You're blind and you can't see anything unless you take a picture!")
    sleep(2)
    print("The chip in your brain lets you see what your camera takes a picture of! Totally normall stuff and not game design limitations. :)")
    sleep(3)
    print("Although you can't see the fox, it can see you! The longer you stay in a location the quicker the fox will run away!")
    print(" ")
    
    points = 50 #set a starting number of points
    
    Foxtudo = Fox() #create the fox
    Foxtudo.spawn() #spawn the fox on the map
    
    sleep(2)
    
    while Foxtudo.found == False: #while the fox isn't found...
        
        if Foxtudo.location == "beyond": #if the fox is at beyond...
        
            print("Hey, B! Just checked reddit and people are saying the fox is downtown. I think we missed it. :(")
            print("     Total Score: 0 points")
            print("     G A M E  O V E R")
        
        sleep(1)
        
        first_time = datetime.now() #grab the time
        print(" ")
        location_input = input("Enter the location you want to visit: ") #have the user enter yes or no
        location_format = (sub(r'\s', '_', location_input)).lower() #replace the spaces with underscores and make it lowercase
        
        sleep(1)
        print(" ")
        print("=====================================")
        print(f"Welcome to {location_input.upper()}!") #print where the person is at.
        print("=====================================")
        print(" ")
        sleep(1)
        
        response = input("Do you want to take a picture? Enter yes or no: ") #have the user enter yes or no
        response = response.lower() #make the entire response lowercase
        
        second_time = datetime.now() #grab the time
        
        if response == "yes":

            difference = second_time - first_time #find the difference between the first and second time.
    
            if difference > timedelta(seconds=30): #if the time is greater then 20 seconds...
    
                Foxtudo.foxtrot() #...move the fox
                points -= 5 #subtract 5 points
                print("greater than 30 seconds") #for testing
        
            if location_format == str(Foxtudo.location): #if the fox is at the location...
                
                Foxtudo = Fox(found = True) #set the fox to found
                
                createImage(Prompts[location_format][0],api_key)
                
                print("Hey! You found the fox! What a shot!")
                print(f"    Total Score: {points} points")
                break

            else: #if the fox isn't at the location
                
                
                createImage(Prompts[location_format][1],api_key)
                
                print("Wow! There's no fox in this picture. Better move on...")
                points -= 1
                #return print(location.absent_prompt)
        
        Foxtudo.foxtrot() #move the fox regardless of the time
         
if __name__ == "__main__":
    main()
