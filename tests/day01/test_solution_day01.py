import unittest

from solutions.common.readers import read_strings
from solutions.day01.solution_day01 import get_number, get_sum, part1, get_sum_part2, get_number_part2, part2


class TestDay01Unit(unittest.TestCase):
    def test_get_number(self):
        self.assertEqual(get_number("1abc2"), 12)
        self.assertEqual(get_number("pqr3stu8vwx"), 38)
        self.assertEqual(get_number("a1b2c3d4e5f"), 15)
        self.assertEqual(get_number("treb7uchet"), 77)

    def test_get_sum(self):
        self.assertEqual(get_sum(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]), 142)

    def test_get_number_part2(self):
        self.assertEqual(get_number_part2("two1nine"), 29)
        self.assertEqual(get_number_part2("eightwothree"), 83)
        self.assertEqual(get_number_part2("abcone2threexyz"), 13)
        self.assertEqual(get_number_part2("xtwone3four"), 24)
        self.assertEqual(get_number_part2("4nineeightseven2"), 42)
        self.assertEqual(get_number_part2("zoneight234"), 14)
        self.assertEqual(get_number_part2("7pqrstsixteen"), 76)
        self.assertEqual(get_number_part2("3xtwone"), 31)

class TestDay01Solution(unittest.TestCase):

    def test_solution_part1(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(part1(input_test_1), 142)

    def test_result_on_real_input_part1(self):
        _input = read_strings("input.txt")
        print(part1(_input))

    def test_solution_part2(self):
        input_test_2 = read_strings("test2.txt")
        self.assertEqual(part2(input_test_2), 281)

    def test_result_on_real_input_part2(self):
        _input = read_strings("input.txt")
        print(part2(_input))
        # 53500 too low

if __name__ == '__main__':
    unittest.main()