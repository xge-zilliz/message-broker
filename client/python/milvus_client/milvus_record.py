from pulsar.schema import Record, Integer, Array, Float
from enum import Enum

class Op(Enum):
    insert = 0
    delete = 1
    update = 2
    query = 3

class MilvusRecord(Record):
    id = Integer()
    op = Op
    vector = Array(Float())
