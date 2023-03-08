#!/usr/bin/python3
"""
Testing the base_model
"""
from models.base_model import BaseModel
import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """The test class"""

    def test_object_type(self):
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime.datetime)
        self.assertIsInstance(bm.updated_at, datetime.datetime)
        self.assertIsInstance(bm.id, str)
