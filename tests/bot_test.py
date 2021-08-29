import sys
import os


import unittest
from unittest import mock
import bot

class TestSmoketest(unittest.TestCase):
    
    def test_smoke(self):
        self.assertTrue(True)

class TestApp(unittest.TestCase):

    def test_import(self):
        self.assertTrue(hasattr(bot, "on_ready"))
