from utils import load, parse_regex, manhatan_distance

class Range():
    range_from;
    range_to;

content = load()

all_cable_locations = []

for line in content:
    cable_locations = []
    actions = line.split(",")

    current_x = 0
    current_y = 0

    for action in actions:
        if action.startswith("R"):
            for i in range(0, int(action[1:])):
                current_x += 1
                cable_locations.append([current_x, current_y])
        if action.startswith("L"):
            for i in range(0, int(action[1:])):
                current_x -= 1
                cable_locations.append([current_x, current_y])
        if action.startswith("U"):
            for i in range(0, int(action[1:])):
                current_y += 1
                cable_locations.append([current_x, current_y])
        if action.startswith("D"):
            for i in range(0, int(action[1:])):
                current_y -= 1
                cable_locations.append([current_x, current_y])

    all_cable_locations.append(cable_locations)

for x_and_y in all_cable_locations[0]:
    if x_and_y in all_cable_locations[1]:
        print("CLASH at {}".format(x_and_y))
        print("distance: {}".format(manhatan_distance(x_and_y[0], x_and_y[1], 0, 0)))

