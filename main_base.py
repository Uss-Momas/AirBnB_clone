#!/usr/bin/python3

from models.base_model import BaseModel

# help(BaseModel)
bm = BaseModel()
bm.name = "My first Model"
bm.my_number = 98

print(bm)
bm.save()
print(bm)

my_model_json = bm.to_dict()
print(my_model_json)

print("JSON of my_model: ")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
# bm.save()
# print("Datetime updated:", bm.updated_at)
# print(dictionary)
