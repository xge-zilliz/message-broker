import sys

sys.path.append('../')
import random
from milvus_client.client import MilvusClient
from multiprocessing import Process

url = 'pulsar://localhost:6650'
token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyLTEifQ.8oAwbbd8dd3ZYhCWKAiShP4Kd0nHSwvQbTMX7Iat_o0'
topic = 'persistent://public/default/topic0'

_DIM = 8
_VECTOR_NUM = 10

vectors = [[random.random() for _ in range(_DIM)] for _ in range(_VECTOR_NUM)]
ids = [i for i in range(_VECTOR_NUM)]
milvus = MilvusClient(url=url, token=token)

def mock_running():
    from milvus_client.client import generate_client_id
    from milvus_client.consumer import get_result_topic_name
    result_topic = get_result_topic_name(generate_client_id())
    client = milvus.client()
    producer = client.create_producer(result_topic)

    # TODO: batch sending
    for i in range(len(vectors)):
        producer.send(bytes(i))

def insert():
    milvus.insert(topic=topic, records=vectors, ids=ids)

def delete():
    milvus.delete(topic=topic, records=vectors, ids=ids)

def update():
    milvus.update(topic=topic, records=vectors, ids=ids)

def search():
    milvus.search(topic=topic, records=vectors, ids=ids)

def test_client():
    # test insert
    Process(target=insert).start()
    Process(target=mock_running).start()

    # test delete
    Process(target=delete).start()
    Process(target=mock_running).start()

    # test update
    Process(target=update).start()
    Process(target=mock_running).start()

    # test search
    Process(target=search).start()
    Process(target=mock_running).start()
