import numpy as np
import common

file = open("./day5/data.txt")
lines = file.readlines()

( vents, ventsAll) = common.parseVents( lines )

numberOfHighPoints = ( vents >= 2 ).sum()
numberOfHighPointsAll = ( ventsAll >= 2 ).sum()

print( numberOfHighPoints )
print( numberOfHighPointsAll )
