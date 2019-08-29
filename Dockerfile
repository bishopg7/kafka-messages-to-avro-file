FROM python:3

RUN pip install kafka-python avro-python3

RUN mkdir /srv/shortlinks-to-avro
WORKDIR /srv/shortlinks-to-avro
COPY study.py schema.avsc ./

CMD["python", "./study.py"]



