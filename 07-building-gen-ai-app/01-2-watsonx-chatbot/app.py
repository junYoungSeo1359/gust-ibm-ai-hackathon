"""_summary_
       수강생 과재 배포용 소스입니다.
    Returns:
        _type_: _description_
"""
import streamlit as st

from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods



st.title("watsonx.ai를 이용한 챗봇!")

model = None

# Create LLM
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
   

def watsonx_ai_api(prompt, api_key, api_url, project_id):
    
    if st.session_state.model is not None:
        model = st.session_state.model
        response = model.generate(prompt=prompt)['results'][0]['generated_text'].strip()
        print(response)
    else:
        print("LLM is not ready! Input correct credentials.")
        response = ""
    
    return response

with st.sidebar:

    watsonx_api_key = st.text_input('Enter API Key:')
    watsonx_api_url = st.text_input('Enter API Url:', value="https://us-south.ml.cloud.ibm.com")
    watsonx_project_id = st.text_input('Enter PROJECT_ID:')
  
    if not (watsonx_api_key and watsonx_api_url and watsonx_project_id):
        st.warning('Please enter your credentials!', icon='⚠️')
    else:
        if st.session_state.model is None:
            st.session_state.model = create_llm(watsonx_api_key, watsonx_api_url, watsonx_project_id)
        st.success('Proceed to entering your prompt message!', icon='👉')

if "model" not in st.session_state:
    st.session_state.model = None

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = watsonx_ai_api(prompt, watsonx_api_key, watsonx_api_url, watsonx_project_id) 
            st.write(response) 
    st.session_state.messages.append({"role": "assistant", "content": response})