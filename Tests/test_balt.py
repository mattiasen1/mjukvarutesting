from sympy import Quaternion, symbols, sqrt
import unittest
import math

w, x, y, z = symbols('w:z')

class TestQuaternion(unittest.TestCase):
  
  def test_inverse(self):
    #Test inverse of quaternions. Inverse is defined as Quaternion(w, -x, -y, -z) / (w**2 + x**2 + y**2 + z**2). Also tested with pow(-1) since this is equivalent to the inverse.
    q = Quaternion(w, x, y, z)
    self.assertEqual(q.inverse(), Quaternion(w, -x, -y, -z) / (w**2 + x**2 + y**2 + z**2))
    self.assertNotEqual(q.inverse(), Quaternion(w, -x, -y, -z) / (w**2 + x**2 + y**2 + z**3))
    self.assertEqual(q.inverse(), q.pow(-1))
  
  def test_quaternion_initialize(self):
    #Test if initializition of quaternions work. If correct errors are raised when wrong inputs are put in to the function.
    q = Quaternion(w, x, y, z)
    with self.assertRaises(NameError):
      q = Quaternion(w, x, y, i)
    with self.assertRaises(AttributeError):
      q = Quaternion([1,4,5])
    
    self.assertEqual(q + q, Quaternion(w*2, x*2, y*2, z*2))
  
  def test_norm(self):
    #By definition ||q|| = sqrt(w^2 + x^2 + y^2 + z^2). Tested from definition with both sqrt and raise to the power 0.5.
    q = Quaternion(w, x, y, z)
    self.assertEqual(q.norm(), sqrt(w**2 + x**2 + y**2 + z**2))
    self.assertEqual(q.norm(), (w**2 + x**2 + y**2 + z**2)**0.5)

  def test_add(self):
    #Testing if add function works. And also that addition without the add function works as well. Testing with negative inputs as well.
    q = Quaternion(w, x, y, z)
    self.assertEqual(q + q, Quaternion(2*w, 2*x, 2*y, 2*z))
    self.assertEqual(q.add(q), (q + q))
    self.assertEqual(q.add(-q), (q - q))
    self.assertEqual((-q).add(-q), (-q - q))

def run_tests():
  unittest.main()

if __name__ == "__main__":
  run_tests()


