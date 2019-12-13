import re

class Object:
    pass

def load():
    with open('input', 'r') as f:
        return [l.rstrip() for l in f.readlines()]

def parse_regex(line, regex, *keys):
    l = re.match(regex, line)
    vals = l.groups()

    return {keys[i]: vals[i] for i in range(len(keys))}

def manhatan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
