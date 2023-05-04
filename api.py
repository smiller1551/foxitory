import os
import openai



def createImage(user_input):
    """Create an image through DALL-E via user prompt.

        prompt (str): required, description of desired image, <1000 characters
        n (int): amount of images desired
        size (str): size of image
    """
    #openai.organization = "YOUR_ORG_ID"
    openai.api_key = os.getenv("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")
    
    response = openai.Image.create(
    prompt= user_input,
    n=1,
    size="512x512"
    )
    
    image_url = response['data'][0]['url']
    #pull image through GUI 

createImage("a fox at the University of Maryland College Park McKeldin Mall")