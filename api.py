import os
import openai

#"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"

class Image:

    def __init__(self, key):
        """Access to DALLE-E API via key.
        """
        self.key = key
        openai.api_key = os.getenv(self.key)
        
    def createImage(user_input):
        """Create an image through DALL-E via user prompt.

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
        return image_url
        #pull image through GUI 

fox_E = Image("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")
img = fox_E.createImage("a fox at the University of Maryland College Park McKeldin Mall")

assert(fox_E)
assert(fox_E.key == "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")
assert(img)