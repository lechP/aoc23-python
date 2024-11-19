def row_sum(line_index: int, lines: list[str]):
    line = lines[line_index]
    index_in_row = 0
    sum_row = 0
    while index_in_row < len(line):
        if line[index_in_row].isdigit():
            temp_index = index_in_row
            number_str = ""
            while temp_index < len(line) and line[temp_index].isdigit():
                number_str += line[temp_index]
                temp_index += 1
            index_in_row = temp_index
            if has_special_sign_neighbour(line_index, index_in_row - len(number_str), index_in_row - 1, lines):
                sum_row += int(number_str)
        else:
            index_in_row += 1

    return sum_row


def has_special_sign_neighbour(row: int, col_begin: int, col_end: int, lines: list[str]):
    left = max(col_begin - 1, 0)
    right = min(col_end + 1, len(lines[row]) - 1)
    if not (lines[row][left] == "." or lines[row][left].isdigit()):
        return True
    if not (lines[row][right] == "." or lines[row][right].isdigit()):
        return True

    for i in range(left, right + 1):
        if row > 0:
            _char = lines[row - 1][i]
            if not (_char == "." or _char.isdigit()):
                return True
        if row < len(lines) - 1:
            _char = lines[row + 1][i]
            if not (_char == "." or _char.isdigit()):
                return True

    return False

# part1
def sum_of_part_numbers(lines: list[str]):
    _sum = 0
    for i in range(len(lines)):
        _sum += row_sum(i, lines)
    return _sum


def indexed_numbers_in_line(line: str):
    index = 0
    indexed_numbers: dict[range, int] = {}
    while index < len(line):
        if line[index].isdigit():
            temp_index = index
            number_str = ""
            while temp_index < len(line) and line[temp_index].isdigit():
                number_str += line[temp_index]
                temp_index += 1
            index = temp_index
            # 'stop' param in range is exclusive
            indexed_numbers.update({range(index - len(number_str), index): int(number_str)})
        else:
            index += 1
    return indexed_numbers


# part2
def sum_gear_ratios(lines: list[str]):
    numbers = []
    _sum = 0
    for row in range(len(lines)):
        line = lines[row]
        numbers.append(indexed_numbers_in_line(line))

    for row in range(len(lines)):
        line = lines[row]
        for col in range(len(line)):
            if line[col] == "*":
                neighbours = []
                if row > 0: # consider the row above
                    for _rng, _val in numbers[row - 1].items():
                        if col - 1 in _rng or col in _rng or col + 1 in _rng:
                            neighbours.append(_val)
                if row < len(lines) - 1: # consider the row below
                    for _rng, _val in numbers[row + 1].items():
                        if col - 1 in _rng or col in _rng or col + 1 in _rng:
                            neighbours.append(_val)
                for _rng, _val in numbers[row].items():
                    if col - 1 in _rng: # consider the left neighbour
                        neighbours.append(_val)
                    if col + 1 in _rng: # consider the right neighbour
                        neighbours.append(_val)
                if len(neighbours) == 2:
                    _sum += neighbours[0] * neighbours[1]
    return _sum
