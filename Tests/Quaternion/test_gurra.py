from sympy import Quaternion, symbols, S, trigsimp, cos, sin, acos, sqrt, pi
import unittest
import math

w, x, y, z = symbols('w:z')


class TestQuaternion(unittest.TestCase):
    def test_rotate_point(self):
        # 1. testing that points cannot rotate around undefined quateunion
        # 2. trying to break function with to many parameters
        # 3. No rotation should lead to same quaternion
        # 4. "Normal" random rotation test 

        q_var = Quaternion(w, x, y, z)
        q1 = Quaternion(1, 0, 0, 0)
        q2 = Quaternion(1, 2, 3, 4)
        
        with self.assertRaises(AttributeError):
            Quaternion.rotate_point((1, 1, 1), q_var)

        with self.assertRaises(TypeError):
            Quaternion.rotate_point((1, 1, 1), q1, 666)

        self.assertEqual(Quaternion.rotate_point((2, 2, 2), q1), (2, 2, 2))
        self.assertEqual(Quaternion.rotate_point((1, 1, 1), q2), (S.One / 5, 1, S(7) / 5))


    def test_to_axis_angle(self):
        # 1. Testing to see if simple quaternion has 0 angle
        # 2. and 3. testing more complex quaternion to test axis and angle
        # 4. Should not be possible to calculate axis and angle of undefined quaternion
        # 5. Another random test to see if axis and angle are correct

        q = Quaternion(1, 0, 0, 0)
        q1 = Quaternion(0, 1, 1, 1)
        q2 = Quaternion(1, 2, 3, 4)
        q_var = Quaternion(1, x, y, z)

        (axis, angle) = q.to_axis_angle()
        self.assertEqual(angle, 0)
        
        (axis, angle) = q1.to_axis_angle()
        self.assertEqual(axis, (sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))
        self.assertEqual(angle, pi)

        with self.assertRaises(AttributeError):
            (axis, angle) = q_var.to_axis_angle()
        
        self.assertTrue(q2.to_axis_angle() == ((2 * sqrt(29)/29,
                                   3 * sqrt(29)/29,
                                   4 * sqrt(29)/29),
                                   2 * acos(sqrt(30)/30)))

    def test_pow_cos_sin(self):
        # 1. Testing to square a complex quaternion
        # 2. Something raised to 0 should be 1
        # 3. Something raised to 1 should be the same
        # 4. Testing to square again
        # 5. Testing to raise to the third power
        # 6. Should not be possible to raise a quaternion by a quaternion

        q1 = Quaternion(1, 2, 3, 4)
        q2 = Quaternion(0, 0, 0, 1)

        self.assertTrue(q1.pow_cos_sin(2) == Quaternion(30 * cos(2 * acos(sqrt(30)/30)),
                                            60 * sqrt(29) * sin(2 * acos(sqrt(30)/30)) / 29,
                                            90 * sqrt(29) * sin(2 * acos(sqrt(30)/30)) / 29,
                                            120 * sqrt(29) * sin(2 * acos(sqrt(30)/30)) / 29))

        self.assertEqual(q2.pow_cos_sin(0), Quaternion(1,0,0,0))
        self.assertEqual(q2.pow_cos_sin(1), Quaternion(0,0,0,1))
        self.assertEqual(q2.pow_cos_sin(2), Quaternion(-1,0,0,0))
        self.assertEqual(q2.pow_cos_sin(3), Quaternion(0,0,0,-1))


        with self.assertRaises(ValueError):
            q1.pow_cos_sin(q2)



if __name__ == "__main__":
    unittest.main()
