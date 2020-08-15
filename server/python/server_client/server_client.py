import pulsar
from pulsar import AuthenticationToken
from pulsar import ConsumerType
from pulsar.schema import AvroSchema
from server_client.milvus_record import MilvusRecord, Op
import time
import string


class ServerClient(object):
    def __init__(self, url=None, topics=None, token="None", subscription_name="subscription"):
        self._url = url
        self._topics = topics
        self._token = token
        self._subscription_name = subscription_name

    def redeliver_message(self):
        client = pulsar.Client(service_url=self._url,
                               authentication=AuthenticationToken(token=self._token))

        consumer = client.subscribe(topic=self._topics,
                                    subscription_name=self._subscription_name,
                                    schema=AvroSchema(MilvusRecord),
                                    consumer_type=ConsumerType.KeyShared)

        delete_producers = []
        insert_producers = []

        for topic in self._topics:
            d_and_u_topic = topic + "-delete"
            delete_producers.append(client.create_producer(topic=d_and_u_topic, schema=AvroSchema(MilvusRecord)))
            i_and_q_topic = topic + "-insert"
            insert_producers.append(client.create_producer(topic=i_and_q_topic, schema=AvroSchema(MilvusRecord)))
        print("Service start successful !!!")

        while True:
            msg = consumer.receive()
            message_topic_name = msg.topic_name()
            for i, topic in enumerate(self._topics):
                if message_topic_name.find(topic) != -1:
                    if msg.value().op in [Op.insert, Op.query]:
                        insert_producers[i].send(content=msg.value(), event_timestamp=int(time.time() * 1000),
                                                 partition_key=str(msg.value().id))
                    else:
                        delete_producers[i].send(content=msg.value(), event_timestamp=int(time.time() * 1000),
                                                 partition_key=str(msg.value().id))
                    break
            consumer.acknowledge(msg)
