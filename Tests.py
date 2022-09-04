import unittest
from quain_func import *

class TestProject(unittest.TestCase):

    def setUp(self):
        self.quain = Quain()

    def testsolv1(self):
        self.assertEqual(self.quain.solving("(x·y·z)"),"(x·y·z)")

    def testsolv2(self):
        self.assertEqual(self.quain.solving("(x · y  · z) + (x · y  · ¬z) + (¬x · y  · z)"), "(x·y) + (y·z)")

    def testsolv3(self):
        self.assertEqual(self.quain.solving(""),"()")



if __name__ == "__main__":
  unittest.main()