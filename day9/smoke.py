
import numpy as np
import common

file = open("./day9/data.txt")
lines = file.readlines()

top = np.array([ 1, 0])
bot = np.array([ -1, 0])
left = np.array([ 0, -1])
right = np.array([ 0, 1])

directions = [ top, bot, left, right]

map = common.parseHeightMap( lines )
( lowPoints, riskLevel) = common.countLowPoints( map, directions)

print( lowPoints )
print( riskLevel )

basins = common.computeBasins( map, directions)

basinSizes = []
for basin in basins:

    basinSize = len( basin )
    basinSizes.append( basinSize )

sortedBasinSizes = sorted( basinSizes, reverse = True)
print( sortedBasinSizes[0] * sortedBasinSizes[1] * sortedBasinSizes[2] )