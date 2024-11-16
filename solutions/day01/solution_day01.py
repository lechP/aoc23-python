import re

def get_number(string):
    for i in string:
        if i.isdigit():
            first_digit = i
            break
    for i in reversed(string):
        if i.isdigit():
            last_digit = i
            break
    return int(first_digit + last_digit)

def get_sum(strings):
    _sum = 0
    for string in strings:
        _sum += get_number(string)
    return _sum

def part1(strings):
    return get_sum(strings)


def get_number_part2(string):
    # Define number map in descending order of word length
    glued_numbers = {
        "eightwo": "eighttwo",
        "eighthree" : "eightthree",
        "oneight": "oneeight",
        "threeight": "threeeight",
        "fiveight": "fiveeight",
        "sevenine": "sevennine",
        "nineight": "nineeight",
        "twone": "twoone",
    }

    # Replace glued numbers with their correct spelling
    for glued, correct in glued_numbers.items():
        string = string.replace(glued, correct)

    # Map of spelled-out numbers to digits
    number_map = {
        "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    # List to store extracted digits
    digits = []

    # Use regex to find potential matches (digits or spelled-out words)
    matches = re.finditer(r"\d|one|two|three|four|five|six|seven|eight|nine", string)

    for match in matches:
        token = match.group()
        if token.isdigit():
            digits.append(int(token))
        elif token in number_map:
            digits.append(number_map[token])

    if digits:
        return int(str(digits[0])+ str(digits[-1]))
    return None, None  # Handle cases where no digits are found

def get_sum_part2(strings):
    _sum = 0
    for string in strings:
        number = get_number_part2(string)
        if number:
            _sum += number
    return _sum

def part2(strings):
    return get_sum_part2(strings)