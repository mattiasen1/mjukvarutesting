from sympy import vector, symbols, sqrt, Rational

import unittest
import math

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


class TestDot(unittest.TestCase):
  def test_dot(self):
    v1 = C.x * i + C.z * C.z * j
    v2 = C.x * i + C.y * j + C.z * k
    self.assertEqual(Dot(v1, v2), Dot(C.x*C.i + C.z**2*C.j, C.x*C.i + C.y*C.j + C.z*C.k))
    self.assertNotEqual(Dot(v1, v2), Dot(C.x*C.i + C.z**1337*C.j, C.x*C.i + C.y*C.j + C.z*C.k))    
    
    self.assertEqual(Dot(v1, v2).doit(), C.x**2 + C.y*C.z**2)
    self.assertEqual(Dot(v1, v2), Dot(v2, v1))

    v3 = C.x * i + C.y * j - C.z * k
    v4 = C.x * i - C.y * j - C.z * k
    self.assertEqual(Dot(v3,v4).doit(), C.x**2 - C.y**2 + C.z**2)


class TestCross(unittest.TestCase):
  def test_cross(self):
    v1 = C.x * i + C.z * C.z * j
    v2 = C.x * i + C.y * j + C.z * k
    self.assertEqual(Cross(v1, v2), Cross(C.x*C.i + C.z**2*C.j, C.x*C.i + C.y*C.j + C.z*C.k))
    self.assertEqual(Cross(v1, v2).doit(), C.z**3*C.i + (-C.x*C.z)*C.j + (C.x*C.y - C.x*C.z**2)*C.k)
    self.assertEqual(cross(v1, v2), C.z**3*C.i + (-C.x*C.z)*C.j + (C.x*C.y - C.x*C.z**2)*C.k)
    self.assertEqual(Cross(v1, v2), -Cross(v2, v1))
    self.assertEqual(Cross(v1, v2) + Cross(v2, v1), Vector.zero)


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