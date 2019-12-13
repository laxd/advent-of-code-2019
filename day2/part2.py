#!/usr/bin python
import math

lines = open('input', 'r').readlines()

def load():
    line = lines[0]

    # Split on commas
    return [int(x) for x in line.split(",")]

def do_function(vars, opcode_index):
    opcode = vars[opcode_index]
    if opcode == 99:
        return vars

    val1_index = vars[opcode_index + 1]
    val2_index = vars[opcode_index + 2]
    output_index = vars[opcode_index + 3]
    val1 = vars[val1_index]
    val2 = vars[val2_index]

    if opcode == 1:
        vars[output_index] = val1 + val2
        return do_function(vars, opcode_index + 4)
    elif opcode == 2:
        vars[output_index] = val1 * val2
        return do_function(vars, opcode_index + 4)
    else:
        print("Unknown opcode " + opcode)
        exit(1)

result = 0

for verb in range(0,99):
    for noun in range(0,99):
        ints = load()
        ints[1] = noun
        ints[2] = verb
        result = do_function(ints, 0)

        if result[0] == 19690720:
            print("noun={}, verb={}".format(noun, verb))
            total = 100 * noun + verb
            print(total)
            exit(0)

