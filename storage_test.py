#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel

print(type(storage))

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
