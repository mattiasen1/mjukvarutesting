from sympy import Quaternion, symbols
import unittest

w, x, y, z = symbols('w:z')

class TestQuaternion(unittest.TestCase):
  
  def TestAddittion(self):
    q = Quaternion(w, x, y, z)
    self.assertEqual(q + q, Quaternion(2*w, 2*x, 2*y, 2*z))


if __name__ == "__main__":
  unittest.main()

