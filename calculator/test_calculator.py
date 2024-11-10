import unittest
from calculator import Calculator  # Importujemy kalkulator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Tworzy instancję kalkulatora przed każdym testem."""
        self.calc = Calculator()

    # Dodawanie
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(5, 0), 5)

    def test_add_large_numbers(self):
        self.assertEqual(self.calc.add(10 ** 6, 10 ** 6), 2000000)

    def test_add_floats(self):
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    # Odejmowanie
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_subtract_negative_numbers(self):
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtract_mixed_numbers(self):
        self.assertEqual(self.calc.subtract(-5, 3), -8)

    def test_subtract_with_zero(self):
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_subtract_large_numbers(self):
        self.assertEqual(self.calc.subtract(10 ** 6, 10 ** 5), 900000)

    def test_subtract_floats(self):
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    def test_subtract_small_numbers(self):
        self.assertEqual(self.calc.subtract(0.0001, 0.0002), -0.0001)

    # Mnożenie
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, -3), 6)

    def test_multiply_mixed_numbers(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)

    def test_multiply_large_numbers(self):
        self.assertEqual(self.calc.multiply(10 ** 6, 10 ** 3), 1000000000)

    def test_multiply_floats(self):
        self.assertEqual(self.calc.multiply(2.5, 4.0), 10.0)

    def test_multiply_small_numbers(self):
        self.assertEqual(self.calc.multiply(0.0001, 0.0002), 2e-08)

    # Dzielenie
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-6, -3), 2)

    def test_divide_mixed_numbers(self):
        self.assertEqual(self.calc.divide(-6, 3), -2)

    def test_divide_with_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_divide_large_numbers(self):
        self.assertEqual(self.calc.divide(10 ** 9, 10 ** 3), 1000000)

    def test_divide_floats(self):
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_divide_small_numbers(self):
        self.assertEqual(self.calc.divide(0.0001, 0.0002), 0.5)

    # Reszta z dzielenia (Modulus)
    def test_modulus_positive_numbers(self):
        self.assertEqual(self.calc.modulus(5, 3), 2)

    def test_modulus_negative_numbers(self):
        self.assertEqual(self.calc.modulus(-5, -3), -2)

    def test_modulus_with_zero(self):
        self.assertEqual(self.calc.modulus(5, 1), 0)
        self.assertEqual(self.calc.modulus(5, 5), 0)

    def test_modulus_large_numbers(self):
        self.assertEqual(self.calc.modulus(10 ** 9, 10 ** 6), 0)

    def test_modulus_floats(self):
        self.assertEqual(self.calc.modulus(7.5, 2.5), 0.0)

    def test_modulus_small_numbers(self):
        self.assertEqual(self.calc.modulus(0.0001, 0.0003), 0.0001)

    # Potęgowanie
    def test_power_positive_numbers(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_power_negative_numbers(self):
        self.assertEqual(self.calc.power(-2, 3), -8)

    def test_power_mixed_numbers(self):
        self.assertEqual(self.calc.power(-2, 2), 4)

    def test_power_with_zero(self):
        self.assertEqual(self.calc.power(0, 5), 0)
        self.assertEqual(self.calc.power(5, 0), 1)

    def test_power_large_numbers(self):
        self.assertEqual(self.calc.power(10, 2), 100)

    def test_power_floats(self):
        self.assertEqual(self.calc.power(2.5, 2), 6.25)


if __name__ == '__main__':
    unittest.main()
