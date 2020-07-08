import unittest
from scrubbish.calc import Calc

class TestCalc(unittest.TestCase):
    def setUp(self):
        args = {
            'price': 120000,
            'rates': 85,
            'years': 25,
            'deposit_percentage': 10.0
        }
        self.calc = Calc(args)

    def test_deposit(self):
        result = self.calc.deposit()

        self.assertEqual(result, 12000)

    def test_fxd_95_LTV_2yrs(self):
        result = self.calc.fxd_95_LTV_2yrs()
        expected = {'25yrs 10.0% 3.99% (2yr fxd 95% LTV)': 562.39}

        self.assertEqual(result, expected)

    def test_fxd_75_LTV_2yrs(self):
        result = self.calc.fxd_75_LTV_2yrs()
        expected = {'25yrs 10.0% 1.49% (2yr fxd 75% LTV)': 424.34}

        self.assertEqual(result, expected)

    def test_fxd_75_LTV_3yrs(self):
        result = self.calc.fxd_75_LTV_3yrs()
        expected = {'25yrs 10.0% 1.7% (3yr fxd 75% LTV)': 435.07}

        self.assertEqual(result, expected)

    def test_fxd_75_LTV_5yrs(self):
        result = self.calc.fxd_75_LTV_5yrs()
        expected = {'25yrs 10.0% 1.99% (5yr fxd 75% LTV)': 450.16}

        self.assertEqual(result, expected)

    def test_std_var_rate(self):
        result = self.calc.std_var_rate()
        expected = {'25yrs 10.0% 4.33% (Std Var Rate)': 582.85}

        self.assertEqual(result, expected)

    def test_trkr_75_LTV(self):
        result = self.calc.trkr_75_LTV()
        expected = {'25yrs 10.0% 2.34% (Trkr 75% LTV)': 468.77}

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
