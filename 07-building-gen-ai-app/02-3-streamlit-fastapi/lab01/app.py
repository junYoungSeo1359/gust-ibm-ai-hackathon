import streamlit as st
import requests, json

st.title("IBM watsonx.ai Prompt Lab!")

# Function for call serving of LLM 
def watsonx_ai_api(prompts):
    payload = {"prompt": prompts}
    response_data = requests.post(api_url, json = payload)
    response = response_data.json()
    print("generated_text:", response_data.json())
  
    return response['text']

with st.sidebar:
    api_url = st.text_input('Enter API Url:', value="http://localhost:8000/processing")
  
    if not (api_url):
        st.warning('Please enter your LLM Serving API Url!', icon='⚠️')
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
            response = watsonx_ai_api(prompt) 
            st.write(response) 
    st.session_state.messages.append({"role": "assistant", "content": response})