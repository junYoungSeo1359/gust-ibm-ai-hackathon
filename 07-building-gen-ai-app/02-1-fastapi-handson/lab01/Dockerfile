FROM python:3.10.11-slim
ENV PORT 8000

# Create virtual environment
RUN python3 -m venv /ve
WORKDIR /app
# Enable venv
ENV PATH="/ve/bin:$PATH"

# Copy requirements file
ADD requirements.txt .

# Copy source to target in docker
COPY . . 

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE $PORT

# CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

CMD uvicorn --host=0.0.0.0 --port $PORT  main:app