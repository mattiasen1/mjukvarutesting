from sympy import vector, symbols, sqrt, Rational, SympifyError

import unittest
import math
import sys

C = vector.CoordSys3D('C')
R = vector.CoordSys3D('R')
i, j, k = C.base_vectors()
cross = vector.cross
Cross = vector.Cross
Vector = vector.Vector
Dot = vector.Dot


class TestVector(unittest.TestCase):
  def test_vector(self):
    v1 = C.x * i + C.z * C.z * j
    v2 = C.x * i + C.y * j + C.z * k
    self.assertRaises(TypeError, lambda: v1/v2) #Cant divide vectors, should throw typeerror
    #Weird inputs
    v1 = "Im a string"
    v2 = 5 * R.i + 5 * R.j + 5 * R.k
    self.assertRaises(TypeError, lambda: v1*v2)
    self.assertRaises(TypeError, lambda: v1+v2)

class TestDot(unittest.TestCase):
  def test_dot(self):
    #Complex Domain
    v1 = C.x * i + C.z * C.z * j
    v2 = C.x * i + C.y * j + C.z * k
    self.assertEqual(Dot(v1, v2), Dot(C.x*C.i + C.z**2*C.j, C.x*C.i + C.y*C.j + C.z*C.k))
    self.assertNotEqual(Dot(v1, v2), Dot(C.x*C.i + C.z**1337*C.j, C.x*C.i + C.y*C.j + C.z*C.k))    
    
    self.assertEqual(Dot(v1, v2).doit(), C.x**2 + C.y*C.z**2)
    self.assertEqual(Dot(v1, v2), Dot(v2, v1))

    v1 = C.x * i + C.y * j - C.z * k
    v2 = C.x * i - C.y * j - C.z * k
    self.assertEqual(Dot(v1,v2).doit(), C.x**2 - C.y**2 + C.z**2)

    #Real Domain
    v1 = 1 * R.i + 3 * R.j - 5 * R.k
    v2 = 4 * R.i - 2 * R.j + -1 * R.k
    self.assertEqual(Dot(v1,v2).doit(), 3)

    #Differnt length of vectors
    v1 = R.i + R.j
    v2 = 5 * R.i + 5 * R.j + 5 * R.k
    self.assertEqual(Dot(v1,v2).doit(), 10)

    v1 = Vector.zero
    v2 = 5 * R.i + 5 * R.j + 5 * R.k
    self.assertEqual(Dot(v1,v2).doit(), 0)

    #Weird inputs
    v1 = "Im a string"
    v2 = 5 * R.i + 5 * R.j + 5 * R.k
    self.assertRaises(SympifyError, lambda: Dot(v1,v2))
    v1 = float("inf") * R.i + float("inf") * R.j + float("inf") * R.k
    v2 = float("inf") * R.i + float("inf") * R.j + float("inf") * R.k
    self.assertEquals(math.isnan(Dot(v1,v2).doit()), True)



class TestCross(unittest.TestCase):
  def test_cross(self):
    v1 = C.x * i + C.z * C.z * j
    v2 = C.x * i + C.y * j + C.z * k
    self.assertEqual(Cross(v1, v2), Cross(C.x*C.i + C.z**2*C.j, C.x*C.i + C.y*C.j + C.z*C.k))
    self.assertEqual(Cross(v1, v2).doit(), C.z**3*C.i + (-C.x*C.z)*C.j + (C.x*C.y - C.x*C.z**2)*C.k)
    self.assertEqual(cross(v1, v2), C.z**3*C.i + (-C.x*C.z)*C.j + (C.x*C.y - C.x*C.z**2)*C.k)
    self.assertEqual(Cross(v1, v2), -Cross(v2, v1))
    self.assertEqual(Cross(v1, v2) + Cross(v2, v1), Vector.zero)


    #Real Domain
    v1 = 1 * R.i + 3 * R.j - 5 * R.k
    v2 = 4 * R.i - 2 * R.j + -1 * R.k
    self.assertEquals(Cross(v1,v2).doit(), (-13)*R.i + (-19)*R.j + (-14)*R.k)


    #Different length of vectors
    v1 = 1 * R.i + 3 * R.j
    v2 = 4 * R.i - 2 * R.j + -1 * R.k
    self.assertEquals(Cross(v1,v2).doit(), (-3)*R.i + R.j + (-14)*R.k)

    #Weird inputs
    v1 = "Im a string"
    v2 = 5 * R.i + 5 * R.j + 5 * R.k
    self.assertRaises(SympifyError, lambda: Cross(v1,v2))

class TestProjection(unittest.TestCase):
  def test_projection(self):
    v1 = i + j + k
    v2 = 3*i + 4*j
    v3 = 0*i + 0*j
    self.assertEqual(v1.projection(v1), i + j + k)
    self.assertEqual(v1.projection(v2), Rational(7, 3)*C.i + Rational(7, 3)*C.j + Rational(7, 3)*C.k)
    self.assertEqual(v1.projection(v1, scalar=True), 1)
    self.assertEqual(v1.projection(v2, scalar=True), Rational(7, 3))
    self.assertEqual(v3.projection(v1), Vector.zero)


if __name__ == "__main__":
   unittest.main() 