import unittest

from solutions.common.readers import read_strings
from solutions.day02.solution_day02 import game_within_limit, game_limits, sum_games_within_limit, power_of_the_game, \
    sum_powers_of_games


class TestDay02Unit(unittest.TestCase):
    def test_check_the_game(self):
        self.assertEqual(game_within_limit("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", game_limits), True)
        self.assertEqual(game_within_limit("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", game_limits), True)
        self.assertEqual(game_within_limit("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", game_limits), False)
        self.assertEqual(game_within_limit("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", game_limits), False)
        self.assertEqual(game_within_limit("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", game_limits), True)

    def test_power_of_the_game(self):
        self.assertEqual(power_of_the_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"), 48)
        self.assertEqual(power_of_the_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"), 12)
        self.assertEqual(power_of_the_game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"), 1560)
        self.assertEqual(power_of_the_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"), 630)
        self.assertEqual(power_of_the_game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"), 36)



class TestDay02Solution(unittest.TestCase):
    def test_solution_part1(self):
        input_test_1 = read_strings("test1.txt")
        self.assertEqual(sum_games_within_limit(input_test_1), 8)

    def test_result_on_real_input_part1(self):
        _input = read_strings("input.txt")
        print(sum_games_within_limit(_input))

    def test_solution_part2(self):
        input_test_2 = read_strings("test2.txt")
        self.assertEqual(sum_powers_of_games(input_test_2), 2286)

    def test_result_on_real_input_part2(self):
        _input = read_strings("input.txt")
        print(sum_powers_of_games(_input))