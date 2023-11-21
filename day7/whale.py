import numpy as np

file = open("./day7/data.txt")
line = file.readline()

positions = np.fromstring( line, sep = ",", dtype=int)

minPosition = np.min( positions )
maxPosition = np.max( positions )
nPositions = maxPosition - minPosition

fuelConsumptions = np.zeros([ nPositions, 1])
fuelConsumptionsCrabEngineering = np.zeros([ nPositions, 1])

counter = 0
for ii in range( minPosition, maxPosition):

    steps = np.abs( positions - ii )
    fuelConsumption_ii = np.abs( positions - ii ).sum()

    fuelConsumptionCE_ii = 0.5 * steps * ( steps + 1 )
    fuelConsumptionCE_ii = fuelConsumptionCE_ii.sum()

    fuelConsumptions[counter] = fuelConsumption_ii
    fuelConsumptionsCrabEngineering[counter] = fuelConsumptionCE_ii

    counter = counter + 1

optimalFuelConsumption = np.min( fuelConsumptions )
optimalFuelConsumptionCE = np.min( fuelConsumptionsCrabEngineering )

print( optimalFuelConsumption )
print( optimalFuelConsumptionCE )