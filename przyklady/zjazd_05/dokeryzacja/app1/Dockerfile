FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN pip install flask

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]