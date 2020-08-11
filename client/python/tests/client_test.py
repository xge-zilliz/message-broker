import sys

sys.path.append('../')
import random
from milvus_client.client import MilvusClient

url = 'pulsar://localhost:6650'
token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyLTEifQ.8oAwbbd8dd3ZYhCWKAiShP4Kd0nHSwvQbTMX7Iat_o0'
topic = 'persistent://public/default/topic0'

_DIM = 8
_VECTOR_NUM = 10

vectors = [[random.random() for _ in range(_DIM)] for _ in range(_VECTOR_NUM)]
ids = [i for i in range(_VECTOR_NUM)]
milvus = MilvusClient(url=url)

def test_insert():
    milvus.insert(token=token, topic=topic, records=vectors, ids=ids)

def test_delete():
    milvus.delete(token=token, topic=topic, records=vectors, ids=ids)

def test_update():
    milvus.update(token=token, topic=topic, records=vectors, ids=ids)

def test_search():
    milvus.search(token=token, topic=topic, records=vectors, ids=ids)

# Test Result
# ===============================================================================================
# Received message id=0 op=Op.insert topic_name=persistent://public/default/topic0-partition-0
# Received message id=2 op=Op.insert topic_name=persistent://public/default/topic0-partition-1
# Received message id=1 op=Op.insert topic_name=persistent://public/default/topic0-partition-0
# Received message id=4 op=Op.insert topic_name=persistent://public/default/topic0-partition-0
# Received message id=6 op=Op.insert topic_name=persistent://public/default/topic0-partition-0
# Received message id=7 op=Op.insert topic_name=persistent://public/default/topic0-partition-4
# Received message id=8 op=Op.insert topic_name=persistent://public/default/topic0-partition-2
# Received message id=3 op=Op.insert topic_name=persistent://public/default/topic0-partition-1
# Received message id=5 op=Op.insert topic_name=persistent://public/default/topic0-partition-1
# Received message id=0 op=Op.delete topic_name=persistent://public/default/topic0-delete-update
# Received message id=9 op=Op.insert topic_name=persistent://public/default/topic0-partition-1
# Received message id=1 op=Op.delete topic_name=persistent://public/default/topic0-delete-update
# Received message id=2 op=Op.delete topic_name=persistent://public/default/topic0-delete-update
# Received message id=3 op=Op.delete topic_name=persistent://public/default/topic0-delete-update
# Received message id=4 op=Op.delete topic_name=persistent://public/default/topic0-delete-update
# Received message id=5 op=Op.delete topic_name=persistent://public/default/topic0-delete-update
# Received message id=6 op=Op.delete topic_name=persistent://public/default/topic0-delete-update
# Received message id=7 op=Op.delete topic_name=persistent://public/default/topic0-delete-update
# Received message id=8 op=Op.delete topic_name=persistent://public/default/topic0-delete-update
# Received message id=9 op=Op.delete topic_name=persistent://public/default/topic0-delete-update
# Received message id=0 op=Op.update topic_name=persistent://public/default/topic0-delete-update
# Received message id=1 op=Op.update topic_name=persistent://public/default/topic0-delete-update
# Received message id=2 op=Op.update topic_name=persistent://public/default/topic0-delete-update
# Received message id=3 op=Op.update topic_name=persistent://public/default/topic0-delete-update
# Received message id=4 op=Op.update topic_name=persistent://public/default/topic0-delete-update
# Received message id=5 op=Op.update topic_name=persistent://public/default/topic0-delete-update
# Received message id=6 op=Op.update topic_name=persistent://public/default/topic0-delete-update
# Received message id=7 op=Op.update topic_name=persistent://public/default/topic0-delete-update
# Received message id=8 op=Op.update topic_name=persistent://public/default/topic0-delete-update
# Received message id=9 op=Op.update topic_name=persistent://public/default/topic0-delete-update
# Received message id=0 op=Op.query topic_name=persistent://public/default/topic0-partition-0
# Received message id=2 op=Op.query topic_name=persistent://public/default/topic0-partition-1
# Received message id=1 op=Op.query topic_name=persistent://public/default/topic0-partition-0
# Received message id=4 op=Op.query topic_name=persistent://public/default/topic0-partition-0
# Received message id=6 op=Op.query topic_name=persistent://public/default/topic0-partition-0
# Received message id=7 op=Op.query topic_name=persistent://public/default/topic0-partition-4
# Received message id=3 op=Op.query topic_name=persistent://public/default/topic0-partition-1
# Received message id=5 op=Op.query topic_name=persistent://public/default/topic0-partition-1
# Received message id=8 op=Op.query topic_name=persistent://public/default/topic0-partition-2
# Received message id=9 op=Op.query topic_name=persistent://public/default/topic0-partition-1
