""" create API for fox """
import openai
import os

class Api:
   
    def __init__(self):
     openai.api_key = os.getenv("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")
     openai.Model.list()
    def create_image(self,description):
        print(self.create_image(prompt = description, n =2, size = "820x820"))
        
