import unittest

from solutions.common.readers import read_strings
from solutions.day02.solution_day02 import game_within_limit, game_limits, sum_games_within_limit, power_of_the_game, \
    sum_powers_of_games
from solutions.day03.solution_day03 import row_sum, sum_of_part_numbers, indexed_numbers_in_line, sum_gear_ratios

lines = ["467..114..",
         "...*......",
         "..35..633.",
         "......#...",
         "617*......",
         ".....+.58.",
         "..592.....",
         "......755.",
         "...$.*....",
         ".664.598.."]

class TestDay03Unit(unittest.TestCase):
    def test_row_sum(self):
        self.assertEqual(467, row_sum(0, lines))
        self.assertEqual(0, row_sum(1, lines))
        self.assertEqual(35+633, row_sum(2, lines))
        self.assertEqual(617, row_sum(4, lines))
        self.assertEqual(0, row_sum(5, lines))
        self.assertEqual(592, row_sum(6, lines))
        self.assertEqual(755, row_sum(7, lines))
        self.assertEqual(0, row_sum(8, lines))
        self.assertEqual(664+598, row_sum(9, lines))

    def test_sum_of_part_numbers(self):
        self.assertEqual(4361, sum_of_part_numbers(lines))

    def test_indexed_numbers_in_line(self):
        self.assertEqual({range(0, 3): 467, range(5, 8): 114}, indexed_numbers_in_line("467..114.."))
        self.assertEqual({range(2, 4): 35, range(6, 9): 633}, indexed_numbers_in_line("..35..633."))
        self.assertEqual({range(0, 3): 617}, indexed_numbers_in_line("617*......"))
        self.assertEqual({range(2, 5): 592}, indexed_numbers_in_line("..592....."))
        self.assertEqual({range(1, 4): 664, range(5, 8): 598}, indexed_numbers_in_line(".664.598.."))

    def test_sum_gear_ratios(self):
        self.assertEqual(467835, sum_gear_ratios(lines))


class TestDay03Solution(unittest.TestCase):
    def test_solution_part1(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(4361, sum_of_part_numbers(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read_strings("input.txt")
        print(sum_of_part_numbers(_input))

    def test_solution_part2(self):
        input_test_2 = read_strings("test1.txt")
        self.assertEqual(467835, sum_gear_ratios(input_test_2))

    def test_result_on_real_input_part2(self):
        _input = read_strings("input.txt")
        print(sum_gear_ratios(_input))