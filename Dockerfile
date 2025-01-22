FROM python:3.9-slim

WORKDIR /app

COPY ./src/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/

EXPOSE 8000

ENV PYTHONUNBUFFERED 1

CMD ["python", "prometheus_metrics.py"]