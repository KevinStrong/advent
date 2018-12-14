# Also builds the source_to_size dictionary, which maps sources to their "territory" size.
def count_closest_source(x, y, all_sources):
    closest_distance = 9e5
    closest_source = 0
    two_sources_at_this_distance = False
    for source_x, source_y in all_sources:
        current_distance = abs(source_x - x) + abs(source_y - y)
        if closest_distance == current_distance:  # No closest source, 2 (or more) are tied
            two_sources_at_this_distance = True
        if closest_distance > current_distance:  # Current closest source
            two_sources_at_this_distance = False
            closest_source = source_x * 1000 + source_y  # hack to convert coordinates into hashable value
            closest_distance = current_distance
    if two_sources_at_this_distance:
        return -1
    if closest_source in source_to_size:
        source_to_size[closest_source] += 1
    else:
        source_to_size[closest_source] = 1
    return closest_source


def remove_edge_sources(x, y):
    # Mark the closest source to this location as "ineligable"
    if location_to_source[x, y] in source_to_size:
        source_to_size.pop(location_to_source[x, y])


all_sources = []
for coordinate in open("day_6/input.txt").read().splitlines():
    all_sources.append(list(map(int, coordinate.split(','))))

max_x = 0
max_y = 0

for coordinate in all_sources:
    max_x = max(coordinate[0], max_x)
    max_y = max(coordinate[1], max_y)


location_to_source = {}
source_to_size = {}

for x in range(0, max_x + 1):
    for y in range(0, max_y + 1):
        location_to_source[x, y] = count_closest_source(x, y, all_sources)


# If a source is closest to an edge then it's size is infinite
# for x in range(0, max_x - 1):
#     remove_edge_sources(x, max_y)
#     remove_edge_sources(x, 0)
# for y in range(0, max_y - 1):
#     remove_edge_sources(0, y)
#     remove_edge_sources(max_x, y)

# 166,260 has area = 3909

# Get a list of all locations

# Iterate over the locations:
    # Remove location from list
    # Check if the sum of all it's source distances is < 10000
    # If yes then build out it's area
    # If no then remove from list and move on
