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