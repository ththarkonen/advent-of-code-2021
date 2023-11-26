
def parseMap( lines ):

    map = {}

    for line in lines:

        line = line.replace("\n", "")
        connection = line.split("-")
        
        startNode = connection[0]
        stopNode = connection[1]

        if startNode in map: map[ startNode ].append( stopNode )
        else: map[ startNode ] = [stopNode]

        if stopNode in map: map[ stopNode ].append( startNode )
        else: map[ stopNode ] = [startNode]

    return map

def checkNodeRepeat( route ):
    for node in route:
        if node.islower() and node != "start" and node != "end":

            n = route.count( node )
            if n == 2:
                return True
            
    return False


def addToRoute( route, nextNodes, singleRepeat):

    newRoutes = []

    for node in nextNodes:

        isSmallCave = node.islower()
        isInRoute = node in route
        smallCaveRepeatedInRoute = checkNodeRepeat( route )

        if singleRepeat and node != "start" and node != "end":
            nodeOccurrence = route.count( node )
            if nodeOccurrence < 2 and not checkNodeRepeat( route ):
                isInRoute = False

        notValidNode = isSmallCave and isInRoute

        if notValidNode: continue

        newRoute = route.copy()

        newRoute.append( node )
        newRoutes.append( newRoute )

    return newRoutes


def computeRoutes( map, singleRepeat):

    routesNext = [["start"]]
    noNewRoutes = False

    completeRoutes = []

    while not noNewRoutes:

        routes = routesNext
        routesNext = []
        noNewRoutes = False

        for route in routes:

            currentRouteNode = route[-1]

            if currentRouteNode == "end" and route not in completeRoutes:
                completeRoutes.append( route )
                continue

            nextNodes = map[ currentRouteNode ]

            routesTemp = addToRoute( route, nextNodes, singleRepeat)

            if routesTemp:
                for routeTemp in routesTemp:
                    routesNext.append( routeTemp )

        if not routesNext: break

    return completeRoutes