#!/usr/bin/python3
"""
This module initializes the storage for the application
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
