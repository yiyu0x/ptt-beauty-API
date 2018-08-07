FROM python:3-slim

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 5487

ENV NAME World

CMD ["python", "app.py"]