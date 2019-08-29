Build & run:
~~~~
docker build . -t kafka-messages-to-avro-file
docker run -d --env-file=env.list kafka-messages-to-avro-file
~~~~