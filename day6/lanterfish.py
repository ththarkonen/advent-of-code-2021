import numpy as np

file = open("./day6/data.txt")
line = file.readline()

fish = np.fromstring( line, sep = ",")

fishPerState = np.zeros( [9, 1], dtype = int)
transitionMatrix = np.loadtxt('./day6/transition.txt')

for time in range(9):

    count = ( fish == time ).sum()
    fishPerState[time,0] = count

# Part 1
#simulationSteps = 80
# Part 2
simulationSteps = 256

for ii in range(simulationSteps):

    fishPerState = transitionMatrix @ fishPerState

totalFish = fishPerState.sum()
totalFish = int( totalFish )
print( totalFish )
