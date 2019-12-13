from utils import load, parse_regex

content = load()

def matches_requirements(val):
    str_val = str(val)

    prev_val = -1

    for char in str_val:
        num = int(char)
        
        if num < prev_val:
            return False
        else:
            prev_val = num

    for i in range(0, 10):
        if str(i) + str(i) in str_val:
            return True

    return False


from_val = content[0]
to_val = content[1]

count = 0

for i in range(int(from_val), int(to_val)):
    if matches_requirements(i):
        print("Matches! {}".format(i))
        count += 1
    else:
        print("Doesn't match {}".format(i))

print(count)
