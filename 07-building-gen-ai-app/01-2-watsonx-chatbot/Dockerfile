FROM python:3.10.11-slim
ENV PORT 8501
WORKDIR /app
# Create virtual environment
RUN python3 -m venv /ve

# Enable venv
ENV PATH="/ve/bin:$PATH"

# Copy requirements file
ADD requirements.txt .

# Copy source to target in docker
COPY . . 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE $PORT

ENTRYPOINT ["streamlit", "run", "app.py", "–server.port=8501", "–server.address=0.0.0.0"]
