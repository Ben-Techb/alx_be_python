import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        # Basic addition
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        # Floating-point addition
        self.assertAlmostEqual(self.calc.add(2.5, 3.2), 5.7)
        # Large numbers
        self.assertEqual(self.calc.add(1e9, 1e9), 2e9)

    def test_subtraction(self):
        """Test the subtract method."""
        # Basic subtraction
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # Floating-point subtraction
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)
        # Large numbers
        self.assertEqual(self.calc.subtract(1e9, 1e8), 9e8)

    def test_multiplication(self):
        """Test the multiply method."""
        # Basic multiplication
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 3), 0)
        # Floating-point multiplication
        self.assertAlmostEqual(self.calc.multiply(2.5, 3.2), 8.0)
        # Large numbers
        self.assertEqual(self.calc.multiply(1e6, 1e6), 1e12)

    def test_division(self):
        """Test the divide method."""
        # Basic division
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(0, 3), 0)
        # Floating-point division
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        # Division by zero
        self.assertIsNone(self.calc.divide(6, 0))

    def test_edge_cases(self):
        """Test additional edge cases."""
        # Very large numbers
        self.assertEqual(self.calc.add(1e12, 1e12), 2e12)
        self.assertEqual(self.calc.multiply(1e6, 1e6), 1e12)
        # Very small numbers
        self.assertAlmostEqual(self.calc.add(1e-10, 1e-10), 2e-10)
        self.assertAlmostEqual(self.calc.divide(1e-10, 1e-5), 1e-5)

if __name__ == "__main__":
    unittest.main()

