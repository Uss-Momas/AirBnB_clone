#!/usr/bin/python3
from models.engine.file_storage import FileStorage

# storage will become kind a global variable
storage = FileStorage()
storage.reload()
