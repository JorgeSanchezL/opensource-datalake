FROM python:3.10-slim

WORKDIR /app

COPY producer_local.py .

RUN pip install --no-cache-dir kafka-python

CMD ["python", "producer_local.py"]
