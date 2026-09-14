from main import divide
import unittest

test_cases = [(12, 3, 4), (9, 2, 4), (-6, 2, -3), (-20, -5, 4), (0.5, 12, 0)]

class TestDivide(unittest.TestCase):
    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, divide, 10, 0)

    def test_divide(self):
        for a, b, c in test_cases:
            with self.subTest(dividend = a, divisor = b, expected_result = c):
                self.assertEqual(divide(a,b), c)
                
unittest.main()




      