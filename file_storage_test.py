#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")

my_model = BaseModel()
#my_model.name = "My_First_Model"
#my_model.my_number = 89
#my_model.save()

# print(my_model)

# fs = FileStorage()
# fs.new(my_model)
# fs.save()

new_model = BaseModel()
# new_model.save()

# fs.new(new_model)
# fs.save()

# print("---RELODING FILE__")
# fs.reload()
