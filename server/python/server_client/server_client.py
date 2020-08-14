import pulsar
from pulsar import AuthenticationToken
from pulsar import ConsumerType
from pulsar.schema import AvroSchema
from server_client.milvus_record import MilvusRecord, Op
import time

class ServerClient(object):
    def __init__(self, url=None):
        self._url = url

    def redeliver_message(self, token: str, consumer_topic: str, subscription_name: str, insert_topic: str, delete_topic: str):
        client = pulsar.Client(service_url=self._url,
                               authentication=AuthenticationToken(token=token))

        consumer = client.subscribe(topic=consumer_topic,
                                    subscription_name=subscription_name,
                                    schema=AvroSchema(MilvusRecord),
                                    consumer_type=ConsumerType.KeyShared)

        insert_produce = client.create_producer(topic=insert_topic, schema=AvroSchema(MilvusRecord))

        delete_produce = client.create_producer(topic=delete_topic, schema=AvroSchema(MilvusRecord))

        print("Service start successful !!!")

        while True:
              msg = consumer.receive()
              if msg.op is Op.insert:
                  insert_produce.send(content=msg.value(), event_timestamp=int(time.time() * 1000), partition_key=str(msg.value().id))
              else:
                  delete_produce.send(content=msg.value(), event_timestamp=int(time.time() * 1000), partition_key=str(msg.value().id))
              consumer.acknowledge(msg)
