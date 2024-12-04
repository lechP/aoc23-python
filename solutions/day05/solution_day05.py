def lowest_location_number(data: str) -> int:
    seeds, maps_list = parse_input(data)
    locations = [end_location(seed, maps_list) for seed in seeds]
    return min(locations)

def end_location(start_location: int, mappings_list: list[tuple[tuple,list[tuple]]]) -> int:
    location = start_location
    for mapping in mappings_list:
        location = destination_location(location, mapping[1])
    return location

def destination_location(input_location: int, mappings: list[tuple]) -> int:
    for mapping in mappings:
        (destination_start, source_start, length) = mapping
        if source_start <= input_location < source_start + length:
            return destination_start + (input_location - source_start)
    return input_location

def parse_input(data: str) -> tuple:
    # Initialize the result dictionary
    maps_list = []

    # Split the data into sections
    sections = data.strip().split("\n\n")

    seeds = list(map(int, sections[0].split(": ")[1].split(" ")))

    for section in sections[1:]:
        # Split the section into lines
        lines = section.split("\n")
        # The first line is the key
        title = lines[0].replace(":", "").strip().split(" ")[0]
        from_to_raw = title.split("-")
        from_to = (from_to_raw[0], from_to_raw[-1])
        # Map entries are tuples of integers
        values = [tuple(map(int, line.split())) for line in lines[1:]]
        # Store in the result dictionary
        maps_list.append((from_to, values))

    return seeds, maps_list
