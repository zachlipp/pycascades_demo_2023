FROM python:3.11.2-slim

WORKDIR home

COPY requirements.txt .

RUN pip3 install -r requirements.txt

EXPOSE 6001

COPY main.py .

ENTRYPOINT python main.py
