#!/usr/bin/python3

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()

# print(my_model)

fs = FileStorage()
fs.new(my_model)
fs.save()

print("---RELODING FILE__")
fs.reload()
