# 1. 내용
여기에서는 tokenization, embedding, vectordb, RAG 관련한 노트북 예제 코드를 제공합니다.


## 1-1. Lag 예제 코드
다음 3개의 노트북은 LAG를 사용하여 LLM을 통해 텍스트를 생성하는 예제코드 입니다. 
3개 모두 전체적으로 동일한 내용으로 구현되어 있으며 차이점은 어떤 플래폼이 제공하는 기본 모델을 사용하느냐 입니다.
각 노트북에는 해당 환경에서 필요한 python package 설치를 위한 requirements 파일이 함께 제공됩니다.
conda environment나 python virtual environment를 사용하여 python 3.10.12 기반의 독립적인 환경을 만든 후 pip install -r requirements_xxx.txt로 package를 설치 후에 노트북을 실행하시기 바랍니다.

  - lag-with-langchain-watsonx-ibmcloud : IBM Cloud상에서 SAS 형태로 제공되는 watsonx platform의 기본 모델 사용.
  - lag-with-langchain-watsonx-cp4d : On prem으로 설치된 IBM Cloud Pak for Data 형태로 제공되는 watsonx platform의 기본 모델 사용.
  - lag-with-langchain-openai : OpenAI가 사용하는 기본 모델 사용.
