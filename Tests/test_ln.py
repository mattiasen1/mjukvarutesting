import unittest
from sympy import re, im, conjugate, sign
from sympy import sqrt, sin, cos, acos, exp, ln, log
from sympy import zoo, nan, pi
from sympy import symbols
from sympy import trigsimp
from sympy import integrate
from sympy import Matrix
from sympy import sympify
from sympy import Quaternion

class TestLn(unittest.TestCase):
    #The tests several different quaternions the _ln function either should be able to proccess or throw an error
    def setUp(self):
        self.q0 = Quaternion(0, 0, 0, 0)
        self.q1 = Quaternion(1, 1, 1, 1)
        self.q2 = Quaternion(0, 1, 2, 3)
        self.q3 = Quaternion(1, 0, 0, 0)
        self.q4 = Quaternion('a', 0, 0, 0)
        self.q5 = Quaternion(1, 2, 3, 4)
        self.q6 = Quaternion('a', 'b', 'c', 'd')
        self.q7 = Quaternion('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 2, 3, 4)
        self.q8 = Quaternion(0, 0, 0, 'a')

    def tearDown(self):
       pass

    def test_ln(self):
        #Tests a quaternion with both real part as well as the quaternion units being zero. 
        self.assertEqual(self.q0._ln(), Quaternion(zoo,
               nan,
               nan,
               nan))
        #Tests a quaternion with real part and quaternion units being non-zero values.
        self.assertEqual(self.q1._ln(), Quaternion(log(2),
                sqrt(3)*pi/9,
                sqrt(3)*pi/9,
                sqrt(3)*pi/9))
        #Tests a quaternion with zero valued real part and non-zero valued quaternion units.
        self.assertEqual(self.q2._ln(), Quaternion(log(sqrt(14)),
                sqrt(14)*pi/28,
                sqrt(14)*pi/14,
                3*sqrt(14)*pi/28))
        #Tests a quaternion with non-zero valued real part but zero valued quaternion units.
        self.assertEqual(self.q3._ln(), Quaternion(0,
               nan,
               nan,
               nan))
        #Tests a quaternion with a symbolic varibale as real part value. The quaternion units are zero.
        self.assertEqual(self.q4._ln(), Quaternion(log(sqrt(symbols('a')**2)),
               nan,
               nan,
               nan))
        #Tests a quaternion that has other values > 1 as quaternion units.
        self.assertEqual(self.q5._ln(), Quaternion(log(sqrt(30)),
               2 * sqrt(29) * acos(sqrt(30)/30) / 29,
               3 * sqrt(29) * acos(sqrt(30)/30) / 29,
               4 * sqrt(29) * acos(sqrt(30)/30) / 29))
        #Tests a quaternion where all parameters a symbolic variables.
        self.assertEqual(self.q6._ln(), Quaternion(log(sqrt(symbols('a')**2 + symbols('b')**2 + symbols('c')**2 + symbols('d')**2)),
                symbols('b')*acos(symbols('a')/sqrt(symbols('a')**2 + symbols('b')**2 + symbols('c')**2 + symbols('d')**2))/sqrt(symbols('b')**2 + symbols('c')**2 + symbols('d')**2),
                symbols('c')*acos(symbols('a')/sqrt(symbols('a')**2 + symbols('b')**2 + symbols('c')**2 + symbols('d')**2))/sqrt(symbols('b')**2 + symbols('c')**2 + symbols('d')**2),
                symbols('d')*acos(symbols('a')/sqrt(symbols('a')**2 + symbols('b')**2 + symbols('c')**2 + symbols('d')**2))/sqrt(symbols('b')**2 + symbols('c')**2 + symbols('d')**2)))
        #Tests a quaternion where the real part is a string.
        self.assertEqual(self.q7._ln(), Quaternion(log(sqrt(symbols('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')**2 + 29)),
                2*sqrt(29)*acos(symbols('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')/sqrt(symbols('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')**2 + 29))/29,
                3*sqrt(29)*acos(symbols('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')/sqrt(symbols('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')**2 + 29))/29,
                4*sqrt(29)*acos(symbols('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')/sqrt(symbols('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')**2 + 29))/29))
        #Tests a quaternion with one of the quaternion units being a symbolic variable and the rest zero.
        self.assertEqual(self.q8._ln(), Quaternion(log(sqrt(symbols('a')**2)),
                0,
                0,
                pi*symbols('a')/(2*sqrt(symbols('a')**2)) ))


#Just so the testfile can be compiled normally.
def run_tests():
		unittest.main()

if __name__ == "__main__":
		run_tests()

