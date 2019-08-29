FROM python:alpine

RUN pip install kafka-python avro-python3

RUN mkdir /srv/kafka-messages-to-avro-file
WORKDIR /srv/kafka-messages-to-avro-file
COPY start.py schema.avsc ./

CMD["python", "./start.py"]



