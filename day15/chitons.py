
import numpy as np
import common

file = open("./day15/data.txt")
lines = file.readlines()

top = np.array([ 1, 0])
bot = np.array([ -1, 0])
left = np.array([ 0, -1])
right = np.array([ 0, 1])

directions = [ top, right]

map = common.parseData( lines )
bigMap = common.computeBigMap( map )

bestRiskGreedy = common.mapGreedyBestRoute( map, directions)
bestRiskGreedyBig = common.mapGreedyBestRoute( bigMap, directions)

directions = [ top, bot, left, right]

bestRisk = common.mapBestRoute( map, directions, bestRiskGreedy)
bestRiskBig = common.mapBestRoute( bigMap, directions, bestRiskGreedyBig)

print( bestRisk )
print( bestRiskBig )
