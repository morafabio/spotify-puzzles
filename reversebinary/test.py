import unittest
from reversebinary import ReverseBinary

class TestCase(unittest.TestCase):
    def setUp(self):
        self.reverseBinary = ReverseBinary()

    def test_binary_conversion(self):
        self.assertEquals(self.reverseBinary.to_binary(16), '10000')

    def test_reverse_string(self):
        self.assertEquals(self.reverseBinary.reverse('10000'), '00001')

    def test_decimal_conversion(self):
        self.assertEquals(self.reverseBinary.to_decimal('10000'), 16)

    def test_four_is_10000_and_must_be_one_000001(self):
        self.assertEquals(self.reverseBinary.convert(16), 1)

    def test_powers_by_two_is_always_one(self):
        self.assertEquals(self.reverseBinary.convert(32), 1)
        self.assertEquals(self.reverseBinary.convert(64), 1)

    def test_upper_limit(self):
        self.assertEquals(self.reverseBinary.convert(1000000000), 1365623)

if __name__ == "__main__":
    unittest.main()
