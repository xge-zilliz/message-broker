import sys
sys.path.append('../')

import pulsar
from pulsar import AuthenticationToken
from pulsar import ConsumerType
from pulsar.schema import AvroSchema
from milvus_client.milvus_record import MilvusRecord

def test_consumer():
    url = 'pulsar://localhost:6650'
    token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyLTEifQ.8oAwbbd8dd3ZYhCWKAiShP4Kd0nHSwvQbTMX7Iat_o0'
    topic = "persistent://public/default/topic0"

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
            print("Received message id={} op={} vector={}".format(ex.id, ex.op, ex.vector))
            # Acknowledge successful processing of the message
            consumer.acknowledge(msg)
        except:
            # Message failed to be processed
            consumer.negative_acknowledge(msg)

    client.close()
