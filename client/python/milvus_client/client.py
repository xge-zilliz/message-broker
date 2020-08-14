import random
import pulsar
from milvus_client import Producer, Consumer
from milvus_client.milvus_record import Op

# TODO: get client id from server
def generate_client_id():
    # client_id = random.randint(0, 10)
    client_id = 1
    return client_id

class MilvusClient:
    def __init__(self, url=None, token=None):
        if not isinstance(url, str) or not isinstance(token, str):
            assert 0

        from pulsar import AuthenticationToken

        self._client = pulsar.Client(url, authentication=AuthenticationToken(token))
        self._client_id = generate_client_id()

    def __del__(self):
        self._client.close()

    def client(self):
        return self._client

    def client_id(self):
        return self._client_id

    def _produce(self, topic: str, records: list, op: Op, ids=None):
        producer = Producer(client=self._client, topic=topic, op=op, client_id=self._client_id)
        producer.send(vectors=records, ids=ids)

    def _consume(self, num_of_result: int):
        consumer = Consumer(client=self._client, client_id=self._client_id)
        return consumer.subscribe_result(num_of_result=num_of_result)

    def insert(self, topic: str, records, ids=None):
        op = Op.insert
        self._produce(topic, records, op, ids)
        res = self._consume(len(records))
        return res

    def delete(self, topic: str, records, ids=None):
        op = Op.delete
        self._produce(topic, records, op, ids)
        res = self._consume(len(records))
        return res

    def update(self, topic: str, records, ids=None):
        op = Op.update
        self._produce(topic, records, op, ids)
        res = self._consume(len(records))
        return res

    def search(self, topic: str, records, ids=None):
        op = Op.query
        self._produce(topic, records, op, ids)
        res = self._consume(len(records))
        return res
