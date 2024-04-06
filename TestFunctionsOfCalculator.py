import unittest
from Calculator import add, subtract, multiply, divide, calculate

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(-4, 2), -2)
        self.assertEqual(divide(5, 0), "Error! Division by zero!")

    def test_calculate_add(self):
        self.assertEqual(calculate('1', 1, 2), 3)

    def test_calculate_subtract(self):
        self.assertEqual(calculate('2', 5, 3), 2)

    def test_calculate_multiply(self):
        self.assertEqual(calculate('3', 2, 3), 6)

    def test_calculate_divide(self):
        self.assertEqual(calculate('4', 6, 2), 3)
        self.assertEqual(calculate('4', 5, 0), "Error! Division by zero!")

if __name__ == '__main__':
    unittest.main()
