import openai

class Image:

    def __init__(self, key):
        """Access to DALLE-E API via key.
        """
        self.key = key
        openai.api_key = self.key
        
    def createImage(self, user_input):
        """Create an image through DALL-E via user prompt.

            Args:
                user_input (str): phrase the user wants generated as an image
                
            response (Image): the AI generated image
            prompt (str): required, description of desired image, <1000 characters
            n (int): amount of images desired
            size (str): size of image
        """
    
        response = openai.Image.create(
        prompt= user_input,
        n=1,
        size="512x512"
        )
    
        image_url = response['data'][0]['url']
        print(image_url) #Displays the image linking URL to the user

fox_E = Image('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')
img = fox_E.createImage("university of maryland campus with a fox")

#assert(fox_E.key == "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")