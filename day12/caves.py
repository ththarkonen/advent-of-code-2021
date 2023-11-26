
import common

file = open("./day12/data.txt")
lines = file.readlines()

map = common.parseMap( lines )
routes = common.computeRoutes( map, singleRepeat = False)
routesPart2 = common.computeRoutes( map, singleRepeat = True)

print( len(routes) )
print( len(routesPart2) )