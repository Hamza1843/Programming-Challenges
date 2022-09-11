import unittest

from main import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(joules(1), 1995262.31497)
        self.assertEqual(joules(3.4251), 8662634684.99)
        self.assertEqual(tnt(10), 15080242351.8)
        self.assertEqual(tnt(1), 0.00047687913)
        self.assertEqual(tnt(3.4251), 2.07041937978)

if __name__ == '__main__':
    unittest.main()
        