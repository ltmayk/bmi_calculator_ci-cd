import unittest
from bmi_calculator.calculations import calculate_bmi, bmi_category

class TestBMICalculator(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertEqual(calculate_bmi(70, 1.75), 22.86)
        self.assertEqual(calculate_bmi(50, 1.6), 19.53)
        self.assertEqual(calculate_bmi(90, 1.8), 27.78)
        self.assertEqual(calculate_bmi(0, 1.75), 0)
        self.assertEqual(calculate_bmi(70, 0), "Height cannot be zero.")

    def test_bmi_category(self):
        self.assertEqual(bmi_category(22.86), "Normal weight")
        self.assertEqual(bmi_category(19.53), "Normal weight")
        self.assertEqual(bmi_category(27.78), "Overweight")
        self.assertEqual(bmi_category(16), "Underweight")
        self.assertEqual(bmi_category(32), "Obesity")

if __name__ == "__main__":
    unittest.main()
