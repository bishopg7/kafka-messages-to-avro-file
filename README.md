App in docker, which read messages from kafka's topic splited ";" and write some data in avro file according to schema.avsc.

Build & run:
~~~~
docker build . -t kafka-messages-to-avro-file
docker run -d --env-file=env.list kafka-messages-to-avro-file
~~~~

example message in kafka's topic:
~~~~
cnMqU2S;1571910386260;XXXX;YYYY;mayor/themes/18299/5698050/
tP1dfOy;1571732580266;ХХХХ;YYYY;services/catalog
~~~~