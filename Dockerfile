FROM python:3

RUN pip install kafka-python avro-python3

RUN mkdir /srv/shortlinks-to-avro
WORKDIR /srv/shortlinks-to-avro
COPY start.py schema.avsc ./

CMD["python", "./start.py"]



