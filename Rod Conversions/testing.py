import unittest

from main import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(meters(100), 502.92)
        self.assertEqual(meters(999999), 5029194.9708)
        self.assertEqual(feet(10), 165)
        self.assertEqual(feet(100), 1650)
        self.assertEqual(feet(999999), 16499983.5)
        self.assertEqual(miles(999999), 3125.004642151441)
        self.assertEqual(furlongs(10), 0.25)
        self.assertEqual(furlongs(100), 2.5)
        self.assertEqual(furlongs(999999), 24999.975)
        self.assertEqual(time_to_walk(999999), 60483.96081583434)
        
        