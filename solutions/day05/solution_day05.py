def parse_seeds(line: str):
    return list(map(int, line.split(": ")[1].split(" ")))

# first two lines skipped
def parse_mappings(lines: list[str]):
    list_of_maps = []
    _map = []
    for i in range(len(lines)):
        if lines[i] == "":
            list_of_maps.append(_map)
            _map = []
        else:
            if lines[i][0].isdigit():
                mapping = list(map(int, lines[i].split(" ")))
                _map.append(mapping)
    list_of_maps.append(_map)
    return list_of_maps


def lowest_location_number(lines: list[str]) -> int:
    seeds = parse_seeds(lines[0])
    mappings = parse_mappings(lines[2:])
    print(seeds)
    print(mappings)
    # and here comes real implementation
    return 0