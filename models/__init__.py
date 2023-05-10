#!/usr/bin/python3
"""to create a unique FileStorage instance for the AirBnB clone"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
