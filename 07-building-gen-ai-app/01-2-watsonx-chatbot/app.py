"""_summary_
       수강생 과재 배포용 소스입니다.
    Returns:
        _type_: _description_
"""
import streamlit as st
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

st.title("watsonx.ai를 이용한 챗봇!")

# Create LLM
def create_llm(api_key, api_url, project_id):
   pass 
  
    
def watsonx_ai_api(prompt, api_key, api_url, project_id):
    
    response = ""
    print(response) 
    
    return response

with st.sidebar:
    watsonx_api_key = st.text_input('Enter API Key:')
    watsonx_api_url = st.text_input('Enter API Url:', value="https://us-south.ml.cloud.ibm.com")
    watsonx_project_id = st.text_input('Enter PROJECT_ID:')
  
    if not (watsonx_api_key and watsonx_api_url and watsonx_project_id):
        st.warning('Please enter your credentials!', icon='⚠️')
    else:
        st.success('Proceed to entering your prompt message!', icon='👉')


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