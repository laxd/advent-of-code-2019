from utils import load, parse_regex, manhatan_distance

def between(a, x1, x2):
    return (a > x1 and a < x2) or (a > x2 and a < x1)

class Range:
    range_from = [0,0];
    range_to = [0,0];

    def orientation(self):
        if self.range_from[0] == self.range_to[0]:
            return "v"
        elif self.range_from[1] == self.range_to[1]:
            return "h"
        else:
            return "wtf"

    def get_intersection(self, other_range):
        # Find out if the ranges are going in different orientations
        if self.orientation() == other_range.orientation():
            return None

        # We need to check that the y values for range_1 lie either side of the
        # y values of range_2
        # AND 
        # The x values for range_2 lie either side of the x values 
        # of range_1

        if self.orientation() == 'v':
            range_1 = self
            range_2 = other_range
        else:
            range_1 = other_range
            range_2 = self


        x_fixed = range_1.range_from[0]
        y_fixed = range_2.range_from[1]

        if between(y_fixed, range_1.range_from[1], range_1.range_to[1]) and between(x_fixed, range_2.range_from[0], range_2.range_to[0]):
            return [x_fixed, y_fixed]
        else:
            return None


    def __repr__(self):
        return str(self.range_from) + " -> " + str(self.range_to)

content = load()

def get_ranges(cable):
    cable_locations = []
    actions = cable.split(",")

    current_x = 0
    current_y = 0

    for action in actions:
        r = Range()
        magnitude = int(action[1:])
        if action.startswith("R"):
            r.range_from = [current_x, current_y]
            current_x = current_x + magnitude
            r.range_to = [current_x, current_y]
        if action.startswith("L"):
            r.range_from = [current_x, current_y]
            current_x = current_x - magnitude
            r.range_to = [current_x, current_y]
        if action.startswith("U"):
            r.range_from = [current_x, current_y]
            current_y = current_y + magnitude
            r.range_to = [current_x, current_y]
        if action.startswith("D"):
            r.range_from = [current_x, current_y]
            current_y = current_y - magnitude
            r.range_to = [current_x, current_y]

        cable_locations.append(r)

    return cable_locations

cable1 = get_ranges(content[0])
cable2 = get_ranges(content[1])

print(cable1)
for range1 in cable1:
    for range2 in cable2:
        intersection = range1.get_intersection(range2)
        if intersection is not None:
            print("Clashes at {} (range1: {}, range2: {})".format(intersection, range1, range2))
        
#for x_and_y in all_cable_locations[0]:
 #   if x_and_y in all_cable_locations[1]:
  #      print("CLASH at {}".format(x_and_y))
   #     print("distance: {}".format(manhatan_distance(x_and_y[0], x_and_y[1], 0, 0)))

