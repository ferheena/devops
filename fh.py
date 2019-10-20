import app
import unittest
import json
from random import randint

mocked_value = randint(0,255)

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
