#!/usr/bin/python3
"""This script creates a storage object.
- If the 'HBNB_TYPE_STORAGE' environment variable is set to 'db',
  it creates a database storage engine (DBStorage).
- If not, it creates a file storage engine (FileStorage).
"""

from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
