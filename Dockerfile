FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
RUN apt-get update 
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pyton3", "app.py"]