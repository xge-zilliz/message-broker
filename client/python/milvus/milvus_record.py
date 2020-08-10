from pulsar.schema import Record, Integer, Array, Float
from enum import Enum

class Op(Enum):
    insert = 0
    delete = 1
    query = 2

class MilvusRecord(Record):
    id = Integer()
    op = Op
    vector = Array(Float())
