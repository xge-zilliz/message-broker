from milvus_client import Producer
from milvus_client.milvus_record import Op

class MilvusClient:
    def __init__(self, url=None):
        self._url = url

    def insert(self, token: str, topic: str, records, ids=None):
        op = Op.insert
        producer = Producer(url=self._url, token=token, topic=topic, op=op)
        producer.send(vectors=records, ids=ids)

    def delete(self, token: str, topic: str, records, ids=None):
        op = Op.delete
        producer = Producer(url=self._url, token=token, topic=topic, op=op)
        producer.send(vectors=records, ids=ids)

    def search(self, token: str, topic: str, records, ids=None):
        op = Op.query
        producer = Producer(url=self._url, token=token, topic=topic, op=op)
        producer.send(vectors=records, ids=ids)
