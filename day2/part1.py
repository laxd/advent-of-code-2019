#!/usr/bin python
import math

lines = open('input', 'r').readlines()

def do_function(vars, opcode_index):
    opcode = vars[opcode_index]
    if opcode == 99:
        return vars

    val1_index = vars[opcode_index + 1]
    val2_index = vars[opcode_index + 2]
    output_index = vars[opcode_index + 3]
    val1 = vars[val1_index]
    val2 = vars[val2_index]

    print("opcode: {}, vals: {}, {}, output: {}".format(opcode, val1, val2, output_index))

    if opcode == 1:
        vars[output_index] = val1 + val2
        print("result: {}".format(vars))
        return do_function(vars, opcode_index + 4)
    elif opcode == 2:
        vars[output_index] = val1 * val2
        print("result: {}".format(vars))
        return do_function(vars, opcode_index + 4)
    else:
        print("Unknown opcode " + opcode)
        exit(1)
    
line = lines[0]

# Split on commas
ints = [int(x) for x in line.split(",")]

print(ints)

result = do_function(ints, 0)

print(result)

