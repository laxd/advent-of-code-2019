from utils import load, parse_regex, manhatan_distance

content = load()

all_cable_locations = []

for line in content:
    cable_locations = {}
    actions = line.split(",")

    length = 0
    current_x = 0
    current_y = 0

    for action in actions:
        if action.startswith("R"):
            for i in range(0, int(action[1:])):
                length += 1
                current_x += 1
                cable_locations[str(current_x) + "," + str(current_y)] = length
        if action.startswith("L"):
            for i in range(0, int(action[1:])):
                length += 1
                current_x -= 1
                cable_locations[str(current_x) + "," + str(current_y)] = length
        if action.startswith("U"):
            for i in range(0, int(action[1:])):
                length += 1
                current_y += 1
                cable_locations[str(current_x) + "," + str(current_y)] = length
        if action.startswith("D"):
            for i in range(0, int(action[1:])):
                length += 1
                current_y -= 1
                cable_locations[str(current_x) + "," + str(current_y)] = length

    all_cable_locations.append(cable_locations)

for key in all_cable_locations[0].keys():
    if key in all_cable_locations[1].keys():
        cable1_length = all_cable_locations[0][key]
        cable2_length = all_cable_locations[1][key]
        print("CLASH at {}".format(key))
        print("Cable 1 length: {}".format(cable1_length))
        print("Cable 2 length: {}".format(cable2_length))
        print("Sum of lengths: {}".format(int(cable1_length)+int(cable2_length)))
        print("distance: {}".format(manhatan_distance(int(key.split(",")[0]), int(key.split(",")[1]), 0, 0)))

