import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,3), 9)
        self.assertEqual(mul(1,5), 5)
        self.assertEqual(mul(4,3), 12)


    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(3, 30), 3.0)
        self.assertAlmostEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(0.5, 1), 2.0)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(7, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(6, 8), 10.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)

    def test_sqrt(self): # 3 assertions
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(4), 2.0)
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()