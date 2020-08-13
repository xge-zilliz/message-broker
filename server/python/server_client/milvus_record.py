from pulsar.schema import Record, Integer, Array, Float
from enum import Enum

class Op(Enum):
    insert = 0
    delete = 1
    update = 2
    query = 3

# NOTE: Use command `pulsar-admin schemas delete <topic-name>` to update schema
class MilvusRecord(Record):
    client_id = Integer()
    id = Integer()
    op = Op
    vector = Array(Float())
