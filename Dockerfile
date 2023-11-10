FROM python:3.11.1-buster

WORKDIR /

RUN pip install -r requirements.txt

ADD main.py .

CMD [ "python", "-u", "/main.py" ]
