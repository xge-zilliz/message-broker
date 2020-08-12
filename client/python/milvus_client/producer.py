import pulsar
import random
from milvus_client.milvus_record import Op, MilvusRecord

def generate_ids(ids_num=10000):
    ids = [random.random() for _ in range(ids_num)]
    return ids

class Producer:
    def __init__(self, url: str, token: str, topic: str, op: Op):
        self._url = url
        self._token = token
        self._topic = topic
        self._op = op

    def send(self, vectors, ids=None):
        from pulsar import AuthenticationToken
        from pulsar.schema import AvroSchema

        client = pulsar.Client(self._url, authentication=AuthenticationToken(self._token))
        producer = client.create_producer(self._topic, schema=AvroSchema(MilvusRecord))

        if ids is None:
            ids = generate_ids()
        assert(len(ids) >= len(vectors))

        for i in range(len(vectors)):
            producer.send(MilvusRecord(id=ids[i], op=self._op, vector=vectors[i]), partition_key=str(ids[i]))
        
        client.close()
