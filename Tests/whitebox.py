from sympy import Quaternion, symbols, I
import unittest


class TestQuaternion(unittest.TestCase):
    def test_pow(self):
        q = Quaternion(2, 2, 2, 2)

        # Inverse
        self.assertEqual(q.pow(-1), q.inverse())

        # Not integer
        self.assertEqual(q.pow(1.5), NotImplemented)

        # Do the loop 1 time and do the if inside the loop
        self.assertEqual(q.pow(1), q)

        # Test negative power. Do the loop twice and not the if inside the loop
        self.assertEqual(q.pow(-2), Quaternion(-1/32, -1/32, -1/32, -1/32))

        # Test the loop twice and only do the if inside loop the the first time
        self.assertEqual(q.pow(2), Quaternion(-8, 8, 8, 8))

        # Don't test loop
        self.assertEqual(q.pow(0), 1)

        # Test loop three times and the if inside the loop twice
        self.assertEqual(q.pow(3), Quaternion(-64, 0, 0, 0))

        # Test loop three times and the if inside the loop only once
        self.assertEqual(q.pow(4), Quaternion(-128, -128, -128, -128))


def run_tests():
    unittest.main()

if __name__ == "__main__":
    run_tests()
