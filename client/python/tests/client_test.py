import sys

sys.path.append('../')
import random
from milvus_client.client import MilvusClient

url = 'pulsar://localhost:6650'
token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyLTEifQ.8oAwbbd8dd3ZYhCWKAiShP4Kd0nHSwvQbTMX7Iat_o0'
topic = 'persistent://public/default/topic0'

_DIM = 8
_VECTOR_NUM = 10


def test_insert():
    vectors = [[random.random() for _ in range(_DIM)] for _ in range(_VECTOR_NUM)]
    ids = [i for i in range(_VECTOR_NUM)]

    milvus = MilvusClient(url=url)
    milvus.insert(token=token, topic=topic, records=vectors, ids=ids)


def test_delete():
    vectors = [[random.random() for _ in range(_DIM)] for _ in range(_VECTOR_NUM)]
    ids = [i for i in range(_VECTOR_NUM)]

    milvus = MilvusClient(url=url)
    milvus.delete(token=token, topic=topic, records=vectors, ids=ids)


def test_search():
    vectors = [[random.random() for _ in range(_DIM)] for _ in range(_VECTOR_NUM)]
    ids = [i for i in range(_VECTOR_NUM)]

    milvus = MilvusClient(url=url)
    milvus.search(token=token, topic=topic, records=vectors, ids=ids)
