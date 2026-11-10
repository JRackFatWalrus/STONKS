import unittest

from stonks import average_cost, portfolio_value, position_value


class PositionValueTests(unittest.TestCase):
    def test_value_is_shares_times_price(self):
        self.assertEqual(position_value(10, 2.5), 25.0)

    def test_negative_input_is_refused(self):
        with self.assertRaises(ValueError):
            position_value(-1, 2.5)


class PortfolioValueTests(unittest.TestCase):
    def test_sums_every_holding(self):
        self.assertEqual(portfolio_value({"AAA": 2, "BBB": 3}, {"AAA": 10.0, "BBB": 1.0}), 23.0)

    def test_missing_price_is_an_error(self):
        with self.assertRaises(KeyError):
            portfolio_value({"AAA": 1}, {})


class AverageCostTests(unittest.TestCase):
    def test_weighted_by_shares(self):
        self.assertEqual(average_cost([(1, 10.0), (3, 20.0)]), 17.5)


if __name__ == "__main__":
    unittest.main()
