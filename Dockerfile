FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY main.py main.py

ENV RS_GCP_SA_KEY=$RS_GCP_SA_KEY

CMD ["python", "main.py"]







