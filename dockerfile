FROM python:3.8-alpine

WORKDIR /app

ADD requirements.txt /app

RUN pip install -r requirements.txt

ADD . /app

ENV ENV=DEV HOST=0.0.0.0 PORT=80

CMD ["python3", "main.py"]