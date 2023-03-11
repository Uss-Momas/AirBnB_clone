#!/usr/bin/python3

from models.base_model import BaseModel

# help(BaseModel)
bm = BaseModel()
bm.name = "My first Model"
bm.my_number = 98

print(bm.id)
print(bm)
print(type(bm.created_at))

print("----")
my_model_json = bm.to_dict()
print(my_model_json)

print("JSON of my_model: ")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")

new_model = BaseModel(**my_model_json)
print(new_model.id)
print(new_model)
print(type(new_model.created_at))


print("=----")
print(bm is new_model)

print("---")

base = BaseModel(None, None)
print(base)
