import unittest

from solutions.common.readers import read_strings
from solutions.day01.solution_day01 import get_number, get_sum, part1


class TestDay01Unit(unittest.TestCase):
    def test_get_number(self):
        self.assertEqual(get_number("1abc2"), 12)
        self.assertEqual(get_number("pqr3stu8vwx"), 38)
        self.assertEqual(get_number("a1b2c3d4e5f"), 15)
        self.assertEqual(get_number("treb7uchet"), 77)

    def test_get_sum(self):
        self.assertEqual(get_sum(["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]), 142)

class TestDay01Solution(unittest.TestCase):
    def test_solution(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(part1(input_test_1), 142)

    def test_result_on_real_input(self):
        input_1 = read_strings("input1.txt")
        print(part1(input_1))

if __name__ == '__main__':
    unittest.main()