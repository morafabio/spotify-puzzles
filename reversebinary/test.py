import unittest
from reversebinary import ReverseBinary

class TestCase(unittest.TestCase):
	def setUp(self):
		self.reverseBinary = ReverseBinary()

	def testConversion(self):
		assert self.reverseBinary.convert(1) == 1
		assert self.reverseBinary.convert(13) == 11
		assert self.reverseBinary.convert(47) == 61
		assert self.reverseBinary.convert(1000000000) == 1365623

if __name__ == "__main__":
	unittest.main();
