import numpy as np

file = open("./day2/data.txt")
lines = file.readlines()

directions = {}
directions["forward"] = np.array([1,0])
directions["up"] = np.array([0,-1])
directions["down"] = np.array([0,1])
directions["back"] = np.array([-1,0])

position = np.array([0.0,0.0])

for line in lines:

    instruction_ii = line.split()

    direction_ii = instruction_ii[0]
    amplitude_ii = instruction_ii[1]
    amplitude_ii = float( amplitude_ii )

    move_ii = amplitude_ii * directions[ direction_ii ]
    position += move_ii

result = position[0] * position[1]
print( result )