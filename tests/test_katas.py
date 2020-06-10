import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        """addition test"""
        # self.fail("TODO: Write add unit test")
        self.assertEqual(katas.add(2, 3), 5, "3+2 should be 5")

    def test_multiply(self):
        """ multiplication test """
        # self.fail("TODO: Write multiply unit test")
        self.assertEqual((katas.multiply(2, 3)), 6, "3 * 2 should be 6")

    def test_power(self):
        """ power test """
        # self.fail("TODO: Write power unit test")
        self.assertEqual((katas.power(2, 4)), 16, "2**4 should be 16")

    def test_factorial(self):
        """ factorial test """
        # self.fail("TODO: Write factorial unit test")
        self.assertEqual(katas.factorial(4), 24, "4 factorial should be 24")

    def test_fibonacci(self):
        """ fibonacci test for nth number = 0,1,1,2,3,5,8,..."""
        # self.fail("TODO: Write fibonacci unit test")
        self.assertEqual((katas.fibonacci(8)), 13,
                         "the 8th number in the fibonacci sequence should be 21")


if __name__ == '__main__':
    unittest.main()
