#!/usr/bin/python3
"""
Testing the base_model
"""
from models.base_model import BaseModel
import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """The test class"""

    def test_save(self):
        bm = BaseModel()
        self.assertEquals(bm.updated_at, datetime.datetime.now())
