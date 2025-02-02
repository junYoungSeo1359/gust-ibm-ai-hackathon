## install streamlit
python3 -m venv .venv
source .venv/bin/activate
pip install streamlit python_dotenv

## export package libraries
pip freeze > requirements.txt
