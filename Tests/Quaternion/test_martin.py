from sympy import Quaternion, symbols, I, E, cos, sin, sqrt, pi
import unittest
import math
import sys

w, x, y, z = symbols('w:z')


class TestQuaternion(unittest.TestCase):
    def test_eval_conjugate(self):
        # Calculates the conjugate of a Quaternion.
        # Tested with integers, variables, infinity, and nan

        q1 = Quaternion(1, 2, 3, 4)
        q2 = Quaternion(1, x, 1, y)
        q3 = Quaternion(0, 0, 0, 0)
        q4 = Quaternion(math.inf, math.inf, math.inf, math.inf)
        q5 = Quaternion(float("nan"), float("nan"), float("nan"), float("nan"))

        self.assertEqual(q1._eval_conjugate(), Quaternion(1, -2, -3, -4))
        self.assertEqual(q2._eval_conjugate(), Quaternion(1, -x, -1, -y))
        self.assertEqual(q3._eval_conjugate(), Quaternion(0, 0, 0, 0))
        self.assertEqual(q4._eval_conjugate(), Quaternion(
            math.inf, -math.inf, -math.inf, -math.inf))
        self.assertEqual(q5._eval_conjugate(), Quaternion(
            float("nan"), float("nan"), float("nan"), float("nan")))

        self.assertRaises(TypeError, q1._eval_conjugate, 1)

    def test_exp(self):
        # Calculates the exponential of a Quaternion q (e^q).
        # Tested with integers, variables, infinity, and nan

        q1 = Quaternion(1, 2, 3, 4)
        q2 = Quaternion(1, x, 1, y)
        q3 = Quaternion(0, 0, 0, 0)
        q4 = Quaternion(math.inf, math.inf, math.inf, math.inf)
        q5 = Quaternion(float("nan"), float("nan"), float("nan"), float("nan"))

        self.assertEqual(q1.exp(), Quaternion(E*cos(sqrt(29)), 2*sqrt(29)*E*sin(
            sqrt(29))/29,  3*sqrt(29)*E*sin(sqrt(29))/29, 4*sqrt(29)*E*sin(sqrt(29))/29))
        self.assertEqual(q2.exp(), Quaternion(E*cos(sqrt(x**2 + y**2 + 1)), E*x*sin(sqrt(x**2 + y**2 + 1))/sqrt(x**2 + y**2 + 1),
                                              E*sin(sqrt(x**2 + y**2 + 1))/sqrt(x**2 + y**2 + 1), E*y*sin(sqrt(x**2 + y**2 + 1))/sqrt(x**2 + y**2 + 1)))
        self.assertEqual(q3.exp(), Quaternion(
            1, float("nan"), float("nan"), float("nan")))
        self.assertEqual(q4.exp(), Quaternion(
            float("nan"), float("nan"), float("nan"), float("nan")))
        self.assertEqual(q5.exp(), Quaternion(
            float("nan"), float("nan"), float("nan"), float("nan")))

        self.assertRaises(TypeError, q1.exp, "a")

    def test_from_axis_angle(self):
        # Returns a rotation quaternion given the axis and the angle of rotation.
        # Tested with positive integers, negative integers, variables, zero and nan

        a1 = 2*pi/3
        v1 = (sqrt(3)/3, sqrt(3)/3, sqrt(3)/3)

        a2 = -pi
        v2 = -x

        a3 = 0
        v3 = 0

        a4 = float("nan")
        v4 = float("nan")

        self.assertEqual(Quaternion.from_axis_angle(
            v1, a1), Quaternion(1/2, 1/2, 1/2, 1/2))

        self.assertRaises(
            TypeError, Quaternion.from_axis_angle, v2, a2)
        self.assertRaises(
            TypeError, Quaternion.from_axis_angle, v3, a3)
        self.assertRaises(
            TypeError, Quaternion.from_axis_angle, v4, a4)


if __name__ == "__main__":
    unittest.main()
