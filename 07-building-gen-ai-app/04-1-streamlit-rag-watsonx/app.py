import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_ibm import WatsonxLLM
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import PyPDF2
from io import BytesIO

# Streamlit 애플리케이션 설정
st.set_page_config(layout="wide")
st.title("Watsonx 기반 RAG 애플리케이션")

# Watsonx 설정을 위한 사이드바
with st.sidebar:
    st.header("Watsonx 설정")
    model_id = st.text_input("모델 ID", "meta-llama/llama-3-70b-instruct")
    apikey = st.text_input("API Key", type="password")
    url = st.text_input("API URL", "https://us-south.ml.cloud.ibm.com")
    project_id = st.text_input("프로젝트 ID")

    decoding_method = st.selectbox("Decoding Method", options=["greedy", "sample"], index=0)
    min_new_tokens = st.slider("Min New Tokens", min_value=0, max_value=50, value=10)
    max_new_tokens = st.slider("Max New Tokens", min_value=100, max_value=400, value=400)
    temperature = st.slider("Temperature", min_value=0.0, max_value=2.0, value=1.0)

    params = {
        "decoding_method": decoding_method,
        "min_new_tokens": min_new_tokens,
        "max_new_tokens": max_new_tokens,
        "temperature": temperature
    }

# 파일 업로드 및 로컬 저장
uploaded_file = st.sidebar.file_uploader("PDF 파일을 업로드하세요", type="pdf")
save_path = None
if uploaded_file:
    save_dir = "upload_files"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    save_path = os.path.join(save_dir, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.sidebar.success(f"파일이 로컬에 '{save_path}'로 저장되었습니다.")

# 페이지 레이아웃 설정: 채팅과 PDF 뷰어 탭으로 구성
tabs = st.tabs(["채팅", "PDF 뷰어"])

# PDF 뷰어 탭
with tabs[1]:
    st.header("PDF 뷰어")
    if save_path:
        # PDF 뷰어 표시
        st.write("PDF 파일 내용:")
        pdf_reader = PyPDF2.PdfReader(BytesIO(uploaded_file.read()))
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            st.text(page.extract_text())

# 채팅 탭
with tabs[0]:
    st.header("채팅")
    question = st.text_input("질문을 입력하세요")

    if st.button("질문"):
        if question:
            if 'llm' not in st.session_state:
                # LLM 모델 초기화
                st.session_state.llm = []

            if save_path:
                # 문서 로드 및 텍스트 분리
 
                feedback = st.radio("이모티콘으로 답변에 피드백 주세요:", ("😊", "😐", "😞"))
                if feedback:
                    st.write(f"선택한 피드백: {feedback}")
            else:
                st.error("PDF 파일이 업로드되지 않았습니다.")
        else:
            st.warning("질문을 입력하세요.")



