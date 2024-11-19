import unittest

from solutions.common.readers import read_strings
from solutions.day04.solution_day04 import card_value, sum_card_values, sum_cards

cards = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
         "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
         "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
         "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
         "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
         "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]


class TestDay04Unit(unittest.TestCase):
    def test_card_value(self):
        self.assertEqual(8, card_value(cards[0]))
        self.assertEqual(2, card_value(cards[1]))
        self.assertEqual(2, card_value(cards[2]))
        self.assertEqual(1, card_value(cards[3]))
        self.assertEqual(0, card_value(cards[4]))
        self.assertEqual(0, card_value(cards[5]))

    def test_sum_card_values(self):
        self.assertEqual(13, sum_card_values(cards))

    def test_sum_cards(self):
        self.assertEqual(30, sum_cards(cards))


class TestDay04Solution(unittest.TestCase):
    def test_solution_part1(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(13, sum_card_values(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read_strings("input.txt")
        print(sum_card_values(_input))

    def test_solution_part2(self):
        input_test_2 = read_strings("test1.txt")
        self.assertEqual(30, sum_cards(input_test_2))

    def test_result_on_real_input_part2(self):
        _input = read_strings("input.txt")
        print(sum_cards(_input))
