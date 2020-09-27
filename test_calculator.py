import unittest
from random import randint
from calculator import Calculator
from datetime import datetime


class MyCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(randint(-1000000, 1000000))

    def test_power_0(self):
        print('test_power_0')
        print('start time: ', str(datetime.now().time()))
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(0).value, calc_value**0)
        print('end time: ', str(datetime.now().time()))

    def test_power_1(self):
        print('\ntest_power_1')
        print('start time: ', str(datetime.now().time()))
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(1).value, calc_value)
        print('end time: ', str(datetime.now().time()))

    def test_power_2(self):
        print('\ntest_power_2')
        print('start time: ', str(datetime.now().time()))
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(2).value, calc_value**2)
        print('end time: ', str(datetime.now().time()))

    def test_power_neg(self):
        print('\ntest_power_neg')
        print('start time: ', str(datetime.now().time()))
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(-1).value, 1/calc_value)
        print('end time: ', str(datetime.now().time()))

    def test_power_long(self):
        print('\ntest_power_long')
        print('start time: ', str(datetime.now().time()))
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(2, 2, 3).value, calc_value**12)
        print('end time: ', str(datetime.now().time()))

    def test_power_combo(self):
        print('\ntest_power_combo')
        print('start time: ', str(datetime.now().time()))
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.power(1, -1, 2, 3, 0.5).value, (1/calc_value)**3)

    def test_power_float(self):
        print('\ntest_power_float')
        print('start time: ', str(datetime.now().time()))
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.power(0.5).value, calc_value**0.5)
        print('end time: ', str(datetime.now().time()))

    def test_root_1(self):
        print('\ntest_root_1')
        print('start time: ', str(datetime.now().time()))
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(1).value, calc_value)
        print('end time: ', str(datetime.now().time()))

    def test_root_2(self):
        print('\ntest_root_2')
        print('start time: ', str(datetime.now().time()))
        calc_value = self.calculator.value
        self.assertEqual(self.calculator.root(2).value, calc_value**(1/2))
        print('end time: ', str(datetime.now().time()))

    def test_root_0(self):
        print('\ntest_root_0')
        print('start time: ', str(datetime.now().time()))
        self.assertEqual(self.calculator.root(0).value, 'division by zero')
        print('end time: ', str(datetime.now().time()))

    def test_root_long(self):
        print('\ntest_root_long')
        print('start time: ', str(datetime.now().time()))
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.root(1, 2, 3, 5).value, calc_value**(1/(2*3*5)))
        print('end time: ', str(datetime.now().time()))


if __name__ == '__main__':
    unittest.main()
