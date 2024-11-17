import math

game_limits = {
    "blue": 14,
    "red": 12,
    "green": 13
}


def game_within_limit(desc: str, limits: dict[str, int]):
    game_id_str, samples_str = desc.split(": ")
    samples = samples_str.split("; ")
    for sample in samples:
        if not sample_within_limit(sample, limits):
            return False
    return True


def sample_within_limit(sample: str, limits: dict[str, int]):
    cubes = sample.split(", ")
    for cube in cubes:
        count, color = cube.split(" ")
        if color not in limits:
            return False
        if int(count) > limits[color]:
            return False
    return True


def sum_games_within_limit(games: list[str]):
    _sum = 0
    for game in games:
        if game_within_limit(game, game_limits):
            game_id_str, _ = game.split(": ")
            game_id = int(game_id_str.split(" ")[1])
            _sum += game_id
    return _sum


# part2
def power_of_the_game(desc: str):
    mincubes = {
        "blue": 0,
        "red": 0,
        "green": 0
    }
    game_id_str, samples_str = desc.split(": ")
    samples = samples_str.split("; ")
    for sample in samples:
        cubes = sample.split(", ")
        for cube in cubes:
            count, color = cube.split(" ")
            if mincubes[color] < int(count):
                mincubes[color] = int(count)

    return math.prod(mincubes.values())

def sum_powers_of_games(games: list[str]):
    _sum = 0
    for game in games:
        _sum += power_of_the_game(game)
    return _sum