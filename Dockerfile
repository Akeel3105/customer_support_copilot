FROM python:3.10-slim

WORKDIR /app

# Install system deps (FAISS needs gcc & g++)
RUN apt-get update && apt-get install -y build-essential

# Upgrade pip
RUN pip install --upgrade pip


# Install remaining packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "run_1.py", "--server.port=8501", "--server.address=0.0.0.0"]

