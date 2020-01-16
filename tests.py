from sympy import Quaternion, symbols, sqrt, Matrix, cos, sin, trigsimp, Rational, pi, acos, S
import unittest


w, x, y, z = symbols('w:z')
phi = symbols('phi')

class TestQuaternion(unittest.TestCase):
  #Test the normalization.
  #The first test checks that the normalization function works accurate according to their norm-function
  #The second test checks if it works correctly with the the variables w, x, y and z.
  #The third test checks that the normalize function differ from the written one. Here, the exponent in the square root part is four instead of one. 
  #The fourth function checks so that a quaternion of zeros isn't equal to zero in the actual calculations

  def test_normalize(self):
    q = Quaternion(w,x,y,z)
    q0 = Quaternion(0, 0, 0, 0)
    q1 = Quaternion(1,2,3,4)
    self.assertEqual(q1.normalize(), Quaternion(1,2,3,4) * (1/q1.norm()))
    self.assertEqual(q.normalize(), Quaternion(w, x, y, z)/ sqrt(w**2 + x**2 + y**2 + z**2))
    self.assertNotEqual(q.normalize(), Quaternion(w,x,y,z)/ sqrt(w**4 + x**4 + y**4 + z**4))
    self.assertNotEqual(q0.normalize(), Quaternion(0, 0, 0, 0)/ sqrt(0**2 + 0**2 + 0**2 + 0**2))
  

  def test_from_rotation_matrix(self):
    #Test the from_rotation_matrix function
    #The first test checks that a normal matrix becomes a correct quaternion. 
    #The second test checks that the outcome from our test is incorrect with the normalization function. 
    #The third test is with variables and checks that the formula of how to calculate from rotation matrix is accurate
    a= 2
    b= 2 
    c= 2 
    d= 2 
    e= 2
    f= 2 
    g= 2
    h= 2 
    i= 2

    m = Matrix([[cos(phi), -sin(phi), 0], [sin(phi), cos(phi), 0], [0,0,1]])
    m1 = Matrix([[1,0,0],[0,0,-1],[0,1,0]])
    m2 = Matrix([[a,b,c],[d,e,f],[g,h,i]])

    q = trigsimp(Quaternion.from_rotation_matrix(m))
    q1 = trigsimp(Quaternion.from_rotation_matrix(m1))
    q2 = trigsimp(Quaternion.from_rotation_matrix(m2))
    
    self.assertEqual(q, Quaternion(sqrt(2) * sqrt(cos(phi) + 1)/2, 0, 0, sqrt(-2*cos(phi) + 2)/2))
    self.assertNotEqual(q1, Quaternion(sqrt(1) * sqrt(cos(phi) + 2), 0, 0, sqrt(-1*cos(phi) + 1)))
    self.assertEqual(q2, Quaternion(sqrt(a + e + i)/2, (h-f)/(2*(sqrt(a + e + i))), (c-g)/(2*(sqrt(a + e + i))), (d-b)/(2*(sqrt(a + e + i)))))


  def test_to_rotation_matrix(self):
    #Test the to_rotation_matrix function.
    #The first test checks whether the to_ration_matrix returns an equal matrix as the one expected
    #The second test checks whether the function returns a different matrix than the one expected
    #The third test sends in a quaternion with variables and it is supposed to be equal to the values in the matrix, but there code does not handle variables. Therefor we made it raise an exception. 
    q = Quaternion(1,2,3,4)
    q1 = Quaternion(w,x,y,z)
    self.assertEqual(q.to_rotation_matrix(), Matrix([[Rational(-2,3), Rational(2,15), Rational(11,15)], [Rational(2,3), Rational(-1,3), Rational(2,3)], [Rational(1,3), Rational(14,15), Rational(2,15)]]))
    self.assertNotEqual(q.to_rotation_matrix(), Matrix([[Rational(2,3), Rational(2,15), Rational(-11,15)], [Rational(2,3), Rational(-1,3), Rational(2,3)], [Rational(1,3), Rational(2,15), Rational(5,15)]]))
    with self.assertRaises(ValueError):
      Matrix([1- 2*(y*y + z*z), 2*(x*y-z*w), 2*(x*z + y*w)], [2*(x*y + z*w), 1- 2*(x*x +z*z), 2* (y*z -x*w)], [2* (x*z -y*w),2 *(y*z + x*w), 1-2*(x*x + y*y)])
 


if __name__ == "__main__":
    unittest.main()