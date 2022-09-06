import unittest

from main_2 import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(meters(10), 50.292)

    def test_custom_num_list(self):
        self.assertEqual(len(create_list(10)), 10)
        