#!/usr/bin/python3

from models.base_model import BaseModel

# help(BaseModel)
bm = BaseModel()
dictionary = bm.to_dict()
# print("First datetime:", bm.updated_at)
# bm.save()
# print("Datetime updated:", bm.updated_at)
print(dictionary)
