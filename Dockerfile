FROM python:3.11.1-buster

WORKDIR /

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD zephyr/ ./zephyr
ADD superflows/ ./superflows

ADD main.py .

ARG HF_TOKEN
ENV HF_TOKEN=${HF_TOKEN}

CMD [ "python", "-u", "/main.py" ]
