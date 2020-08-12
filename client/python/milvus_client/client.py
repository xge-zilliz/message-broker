from milvus_client import Producer
from milvus_client.milvus_record import Op

class MilvusClient:
    def __init__(self, url=None):
        self._url = url

    def _produce(self, token: str, topic: str, records, op: Op, ids=None):
        producer = Producer(url=self._url, token=token, topic=topic, op=op)
        producer.send(vectors=records, ids=ids)

    def insert(self, token: str, topic: str, records, ids=None):
        op = Op.insert
        self._produce(token, topic, records, op, ids)

    def delete(self, token: str, topic: str, records, ids=None):
        op = Op.delete
        topic = topic + "-delete-update"
        self._produce(token, topic, records, op, ids)

    def update(self, token: str, topic: str, records, ids=None):
        op = Op.update
        topic = topic + "-delete-update"
        self._produce(token, topic, records, op, ids)

    def search(self, token: str, topic: str, records, ids=None):
        op = Op.query
        self._produce(token, topic, records, op, ids)
