
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


