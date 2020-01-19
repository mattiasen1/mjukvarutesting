from sympy import Quaternion, symbols
import unittest

w, x, y, z = symbols('w:z')

class TestQuaternion(unittest.TestCase):
  
  def test_inverse(self):
    q = Quaternion(w, x, y, z)
    self.assertEqual(q.inverse(), Quaternion(w, -x, -y, -z) / (w**2 + x**2 + y**2 + z**2))
    self.assertNotEqual(q.inverse(), Quaternion(w, -x, -y, -z) /w**2 + x**2 + y**2 + z**3)
    self.assertEqual(q.inverse(), q.pow(-1))
  
  def test_quaternion_initialize(self):
    q = Quaternion(w, x, y, z)
    with self.assertRaises(NameError):
      q = Quaternion(w, x, y, i)
    with self.assertRaises(AttributeError):
      q = Quaternion([1,4,5])
    
    self.assertEqual(q + q, Quaternion(w*2, x*2, y*2, z*2))


def run_tests():
  unittest.main()

if __name__ == "__main__":
  run_tests()

