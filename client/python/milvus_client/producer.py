import pulsar
import random
from milvus_client.milvus_record import Op, MilvusRecord


# TODO: get ids from server
def generate_ids(ids_num=10000):
    ids = [random.random() for _ in range(ids_num)]
    return ids

class Producer:
    def __init__(self, client: pulsar.Client, client_id: int, topic: str, op: Op):
        self._client = client
        self._topic = topic
        self._op = op
        self._client_id = client_id

    def send(self, vectors, ids=None):
        from pulsar.schema import AvroSchema

        producer = self._client.create_producer(self._topic,
                                                schema=AvroSchema(MilvusRecord),
                                                batching_enabled=True)

        if ids is None:
            ids = generate_ids()
        assert (len(ids) >= len(vectors))

        # TODO: batch sending
        for i in range(len(vectors)):
            producer.send(MilvusRecord(client_id=self._client_id,
                                       id=ids[i],
                                       op=self._op,
                                       vector=vectors[i]),
                          partition_key=str(ids[i]))
