import numpy as np

file = open("./day2/data.txt")
lines = file.readlines()

def forward( x, position):

    aim = position[2]
    return np.array([ x, x * aim, 0])

def up( x, position):
    return np.array([ 0, 0, -x])

def down( x, position):
    return np.array([ 0, 0, x])

directions = {}
directions["forward"] = forward
directions["up"] = up
directions["down"] = down

position = np.array([ 0.0, 0.0, 0.0])

for line in lines:

    instruction_ii = line.split()

    direction_ii = instruction_ii[0]
    amplitude_ii = instruction_ii[1]
    amplitude_ii = float( amplitude_ii )

    move_ii = directions[ direction_ii ]( amplitude_ii, position)
    position += move_ii

result = position[0] * position[1]
print( result )