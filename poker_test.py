import unittest
from poker import check_royal_flush, check_straight, check_3ofa_kind

yes_straight1 = [2, 3, 4]
yes_straight2 = [7, 5, 6]
no_straight1 = [4, 7, 2]
no_straight2 = [11, 2, 8]
yes_three1 = [3, 3, 3]
yes_three2 = [8, 8, 8]
no_three1 = [5, 5, 8]
no_three2 = [5, 11, 2]


class PokerTest(unittest.TestCase):
    def test_is_royal(self):
        result = check_royal_flush(14)
        self.assertEqual(result, True)

    def test_not_royal(self):
        result = check_royal_flush(12)
        self.assertEqual(result, False)
        result = check_royal_flush(0)
        self.assertEqual(result, False)

    def test_is_straight(self):
        result = check_straight(yes_straight1)
        self.assertEqual(result, 4)
        result = check_straight(yes_straight2)
        self.assertEqual(result, 7)

    def test_not_straight(self):
        result = check_straight(no_straight1)
        self.assertEqual(result, 0)
        result = check_straight(no_straight2)
        self.assertEqual(result, 0)

    def test_is_3ofaKind(self):
        result = check_3ofa_kind(yes_three1)
        self.assertEqual(result, 3)
        result = check_3ofa_kind(yes_three2)
        self.assertEqual(result, 8)

    def test_not_3ofaKind(self):
        result = check_3ofa_kind(no_three1)
        self.assertEqual(result, 0)
        result = check_3ofa_kind(no_three2)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
