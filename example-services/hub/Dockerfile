FROM python:3.11.2-slim

WORKDIR home

COPY requirements.txt .

EXPOSE 6000

RUN pip3 install -r requirements.txt

COPY main.py .

ENTRYPOINT uvicorn --host 0.0.0.0 --port 6000 main:app
