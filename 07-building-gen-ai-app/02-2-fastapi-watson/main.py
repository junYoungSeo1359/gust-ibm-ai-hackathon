import os
from fastapi import FastAPI, Form
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods
from model import Message, PromptMessage


def create_llm(api_key, api_url, project_id):
   
   parameters = { 
        GenParams.DECODING_METHOD: DecodingMethods.GREEDY.value,
        GenParams.MIN_NEW_TOKENS: 1,
        GenParams.MAX_NEW_TOKENS: 500,
        GenParams.STOP_SEQUENCES: ["<|endoftext|>"]
    }
   
   credentials = Credentials(
        url=api_url,
        api_key=api_key
    )

   model_id =  'ibm/granite-3-8b-instruct' # 'mistralai/mistral-large' # 'meta-llama/llama-3-1-70b-instruct' # ModelTypes.LLAMA_2_70B_CHAT.value #
   llm = ModelInference(
        model_id=model_id,
        params=parameters,
        credentials=credentials,
        project_id=project_id
    ) 
   
   return llm

load_dotenv()

# api_key =  "Your IBM Cloud API Key"
api_key = os.getenv("API_KEY", None)
api_url =  "https://us-south.ml.cloud.ibm.com"

# project_id = "Your PROJECT_ID"
project_id = os.getenv("PROJECT_ID", None)

print('api_key:', api_key)
print('project_id:', project_id)

model = create_llm(api_key, api_url, project_id)

app = FastAPI() 

@app.post("/processing", description="prompt message",     
          response_model = Message)
def watsonx_ai_api(promptMessage: PromptMessage):

    response = model.generate(prompt=promptMessage.prompt)['results'][0]['generated_text'].strip()
    print(response) 
    msg = {"text": response}
    
    return msg


