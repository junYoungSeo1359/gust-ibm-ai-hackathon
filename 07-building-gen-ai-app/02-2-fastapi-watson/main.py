from fastapi import FastAPI, Form
from dotenv import load_dotenv
from ibm_watson_machine_learning.foundation_models import Model 
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams 
from model import Message, PromptMessage
import os 

load_dotenv()

# api_key =  "Your IBM Cloud API Key"
api_key = os.getenv("API_KEY", None)
api_url =  "https://us-south.ml.cloud.ibm.com"

# project_id = "Your PROJECT_ID"
project_id = os.getenv("PROJECT_ID", None)

print('api_key:', api_key)
print('project_id:', project_id)

app = FastAPI() 

@app.post("/processing", description="prompt message",     
          response_model = Message)
def watsonx_ai_api(promptMessage: PromptMessage):
    # call create_llm
    response = ""
    print(response) 
    msg = {"text": response}
    
    return msg


def create_llm():
    pass 