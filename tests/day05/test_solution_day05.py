import unittest

from solutions.common.readers import read
from solutions.day05.solution_day05 import parse_input, lowest_location_number

data = """
seeds: 79 14 55 13

seed-to-soil map:
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
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


class TestDay05Unit(unittest.TestCase):

    def test_parse_mappings(self):
        seeds, mappings = parse_input(data)
        self.assertEqual([79, 14, 55, 13], seeds)
        self.assertEqual(('seed', 'soil'), mappings[0][0])
        self.assertEqual((52, 50, 48), mappings[0][1][1])

    def test_lowest_location_number(self):
        result = lowest_location_number(data)
        self.assertEqual(35, result)


class TestDay05Solution(unittest.TestCase):
    def test_solution_part1(self):
        input_test_1 = read("test1.txt")
        self.assertEqual(35, lowest_location_number(input_test_1))

    def test_result_on_real_input_part1(self):
        _input = read("input.txt")
        print(lowest_location_number(_input))
