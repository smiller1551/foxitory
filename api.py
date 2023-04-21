import os
import openai

#openai.organization = "YOUR_ORG_ID"
openai.api_key = os.getenv("OPENAI_API_KEY")


def createImage():
    """Create an image through DALL-E via user prompt.

        prompt (str): required, description of desired image, <1000 characters
        n (int): amount of images desired
        size (str): size of image
    """
    response = openai.Image.create(
    prompt= "a fox at the University of Maryland College Park McKeldin Mall",
    n=1,
    size="512x512"
    )
    image_url = response['data'][0]['url']