import pulsar
from pulsar import AuthenticationToken
from pulsar import ConsumerType
from pulsar.schema import AvroSchema
from server_client.milvus_record import MilvusRecord
import time

class ServerClient(object):
    def __init__(self, url=None):
        self._url = url

    def redeliver_message(self, token: str, consumer_topic: str, subscription_name: str, produce_topic: str):
        client = pulsar.Client(service_url=self._url,
                               authentication=AuthenticationToken(token=token))

        consumer = client.subscribe(topic=consumer_topic,
                                    subscription_name=subscription_name,
                                    schema=AvroSchema(MilvusRecord),
                                    consumer_type=ConsumerType.KeyShared)

        produce = client.create_producer(topic=produce_topic, schema=AvroSchema(MilvusRecord))

        print("Service start successful !!!")

        while True:
              msg = consumer.receive()
              produce.send(content=msg.value(), event_timestamp=int(time.time() * 1000), partition_key=str(msg.value().id))
              consumer.acknowledge(msg)
