import unittest

from solutions.common.readers import read_strings
from solutions.day05.solution_day05 import parse_seeds, parse_mappings, lowest_location_number

lines = """seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4""".splitlines()


class TestDay04Unit(unittest.TestCase):
    def test_parse_seeds(self):
        line = "seeds: 79 14 55 13"
        self.assertEqual([79, 14, 55, 13], parse_seeds(line))

    def test_sum_card_values(self):
        self.assertEqual(
            [
                [[50, 98, 2], [52, 50, 48]],
                [[0, 15, 37], [37, 52, 2], [39, 0, 15]],
                [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]]
            ]

            , parse_mappings(lines))


class TestDay04Solution(unittest.TestCase):
    def test_solution_part1(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(13, lowest_location_number(input_test_1))
