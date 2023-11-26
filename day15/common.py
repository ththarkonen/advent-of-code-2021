
import numpy as np
import copy

def parseData( lines ):

    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    data = np.zeros(( nRows, nCols))

    for ii in range( nRows ):
        for jj in range( nCols ):
            data[ ii, jj] = int( lines[ii][jj] )

    return data

def computeBigMap( map ):

    n = 5

    stackedMap = map
    mapStack = map

    for ii in range(1,5):

        mapStack = mapStack + 1
        mapStack[ mapStack > 9 ] = 1

        print( stackedMap )
        stackedMap = np.hstack(( stackedMap, mapStack))

    mapRow = stackedMap

    for ii in range(1,5):

        mapRow = mapRow + 1
        mapRow[ mapRow > 9 ] = 1

        stackedMap = np.vstack(( stackedMap, mapRow))

    return stackedMap

def checkPointValidity( ii, jj, nRows, nCols):

    validPoint = ii >= 0 and jj >= 0
    validPoint = validPoint and ii <= nRows - 1 and jj <= nCols - 1

    return validPoint

def mapGreedyBestRoute( map, directions):

    ( nRows, nCols) = map.shape

    referenceRisk = map[:,0].sum() + map[0,:].sum()
    bestRisk = referenceRisk * np.ones(( nRows, nCols))
    bestRisk[0,0] = 0

    maxRouteRisk = 0

    route = {}
    route["positions"] = [(0,0)]
    route["risk"] = 0

    routes = [route]

    while True:

        newRoutes = []
        for route in routes:

            currentII = route["positions"][-1][0]
            currentJJ = route["positions"][-1][1]

            distanceL1 = nRows - 1 - currentII + nCols - 1 - currentJJ
            lowerRisksCloser = bestRisk[ currentII:, currentJJ:] <= route["risk"]
            lowerRisksCloser = np.any( lowerRisksCloser )

            if currentII == nRows - 1 and currentJJ == nCols - 1: continue
            if lowerRisksCloser: continue
            if distanceL1 > bestRisk[ nRows - 1, nCols - 1]: continue

            for dir in directions:
                    
                nextII = currentII + dir[0]
                nextJJ = currentJJ + dir[1]
                nextPosition = ( nextII, nextJJ)

                validPoint = checkPointValidity( nextII, nextJJ, nRows, nCols)
                if not validPoint: continue

                routeRisk = route["risk"] + map[ nextII, nextJJ]
                lowerRisk = bestRisk[ nextII, nextJJ] > routeRisk
                lowerRisk = lowerRisk and bestRisk[ nRows - 1, nCols - 1] > routeRisk

                if not lowerRisk: continue

                bestRisk[ nextII, nextJJ] = routeRisk

                newRoute = {}
                newRoute["positions"] = [ nextPosition ]
                newRoute["risk"] = routeRisk

                newRoutes.append( newRoute )

        minRisk = np.inf
        for newRoute in newRoutes:
            if newRoute["risk"] < minRisk:
                minRisk = newRoute["risk"]
                newRoutes2 = [newRoute]

        nNewRoutes = len( newRoutes )
        print( nNewRoutes )

        if nNewRoutes == 0:
            return bestRisk[ nRows - 1, nCols - 1]
        
        #print( (bestRisk == np.inf).sum() )
        #print( bestRisk )

        routes = newRoutes2

def mapBestRoute( map, directions, greedyRisk):

    ( nRows, nCols) = map.shape

    bestRisk = greedyRisk * np.ones(( nRows, nCols))
    bestRisk[0,0] = 0

    route = {}
    route["positions"] = [(0,0)]
    route["risk"] = 0

    routes = [route]

    while True:

        newRoutes = []
        for route in routes:

            currentII = route["positions"][-1][0]
            currentJJ = route["positions"][-1][1]

            distanceL1 = nRows - 1 - currentII + nCols - 1 - currentJJ

            if currentII == nRows - 1 and currentJJ == nCols - 1: continue
            if distanceL1 > bestRisk[ nRows - 1, nCols - 1] - route["risk"]: continue

            for dir in directions:
                    
                nextII = currentII + dir[0]
                nextJJ = currentJJ + dir[1]
                nextPosition = ( nextII, nextJJ)

                validPoint = checkPointValidity( nextII, nextJJ, nRows, nCols)
                if not validPoint: continue

                routeRisk = route["risk"] + map[ nextII, nextJJ]
                lowerRisk = bestRisk[ nextII, nextJJ] > routeRisk
                lowerRisk = lowerRisk and bestRisk[ nRows - 1, nCols - 1] > routeRisk

                if not lowerRisk: continue

                bestRisk[ nextII, nextJJ] = routeRisk

                newRoute = {}
                newRoute["positions"] = [ nextPosition ]
                newRoute["risk"] = routeRisk

                newRoutes.append( newRoute )
                #print("Risk: ", routeRisk)

        nNewRoutes = len( newRoutes )
        print( nNewRoutes )

        if nNewRoutes == 0:
            return bestRisk[ nRows - 1, nCols - 1]
        
        #print( (bestRisk == np.inf).sum() )
        #print( bestRisk )

        routes = newRoutes


