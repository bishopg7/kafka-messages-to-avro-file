import logging, avro.schema, os, sys

from avro.datafile import DataFileWriter
from avro.io import DatumWriter
from kafka import KafkaConsumer

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

bootstrap_servers = os.environ["KAFKA_SERVERS"]
topic = os.environ["KAKFA_TOPIC"]
group_id = os.environ["KAFKA_GROUP_ID"]
auto_offset_reset  = os.environ["KAFKA_OFFSET_RESET"]

def msg_to_avro():
    consumer = KafkaConsumer(topic,
                             group_id=group_id,
                             bootstrap_servers=bootstrap_servers,
                             auto_offset_reset=auto_offset_reset,
                             enable_auto_commit=True,
                             max_poll_records=5000,
                             fetch_max_wait_ms=1000
                             )

    schema = avro.schema.Parse(open("schema.avsc","r").read())
    dataFile = open("out.avro", "ab")
    writer = DataFileWriter(dataFile, DatumWriter(), schema)

    for message in consumer:
        msg_str = message.value.decode('utf-8')
        msg_list = msg_str.split(";")
        #print("%s;%s;%s" %(msg_list[1], msg_list[0], msg_list[5]))
        writer.append({"timestamp":  int(msg_list[1]),
                       "short_link": msg_list[0],
                       "long_link":  msg_list[4]
                       })
    writer.close()

msg_to_avro()
