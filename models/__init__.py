#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

print(f"{type(os.getenv('HBNB_TYPE_STORAGE'))} >> {os.getenv('HBNB_TYPE_STORAGE')}")

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    print("Fetching data from Database")
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    print("Fetching data from file storage")
    storage = FileStorage()

storage.reload()
