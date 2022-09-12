import unittest

from main import *


class MyFirstTests(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(joules(10), 6.309573444801943e+19)
        self.assertEqual(joules(1), 1995262.3149688789)
        self.assertEqual(joules(3.4251), 8662634684.989311)
        self.assertEqual(tnt(10), 15080242458.895658)
        self.assertEqual(tnt(1), 0.00047687913837688307)
        self.assertEqual(tnt(3.4251), 2.07041937977756)

if __name__ == '__main__':
    unittest.main()
        