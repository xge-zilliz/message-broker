import sys
sys.path.append('../')

import pulsar
from pulsar import AuthenticationToken
from pulsar import ConsumerType
from pulsar.schema import AvroSchema
from milvus_client.milvus_record import MilvusRecord

def consume(topic):
    url = 'pulsar://localhost:6650'
    token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyLTEifQ.8oAwbbd8dd3ZYhCWKAiShP4Kd0nHSwvQbTMX7Iat_o0'

    client = pulsar.Client(service_url=url,
                           authentication=AuthenticationToken(token=token))
    consumer = client.subscribe(topic=topic,
                                subscription_name=topic,
                                schema=AvroSchema(MilvusRecord),
                                consumer_type=ConsumerType.Shared)

    while True:
        msg = consumer.receive()
        ex = msg.value()
        try:
            print("Received message id={} op={} topic_name={}"
                  .format(ex.id, ex.op, msg.topic_name()))
            # Acknowledge successful processing of the message
            consumer.acknowledge(msg)
        except:
            # Message failed to be processed
            consumer.negative_acknowledge(msg)

def test_consume():
    from multiprocessing import Process
    p1 = Process(target=consume, args=("persistent://public/default/topic0",))
    p2 = Process(target=consume, args=("persistent://public/default/topic0-delete-update",))
    p1.start()
    p2.start()
