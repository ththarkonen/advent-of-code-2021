import numpy as np

def parseHeightMap( lines ):

    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    heightMap = np.zeros([ nRows, nCols])

    for ii in range( nRows ):
        for jj in range( nCols ):

            heightString = lines[ii][jj]
            heightMap[ ii, jj] = float( heightString )

    return heightMap

def countLowPoints( map, directions):

    ( nRows, nCols) = map.shape

    lowPoints = 0
    riskLevel = 0

    for ii in range( nRows ):
        for jj in range( nCols ):

            lowPoint = True
            currentHeight = map[ ii, jj]

            for dir in directions:
                
                nextII = ii + dir[0]
                nextJJ = jj + dir[1]

                validPoint = checkPointValidity( nextII, nextJJ, nRows, nCols)
                
                if validPoint:
                    adjacentHeight = map[ nextII, nextJJ]
                    if adjacentHeight <= currentHeight: lowPoint = False

                if not lowPoint:
                    break

            if lowPoint:
                
                lowPoints = lowPoints + 1
                riskLevel = riskLevel + 1 + currentHeight

    return ( lowPoints, riskLevel)


def checkPointValidity( ii, jj, nRows, nCols):

    validPoint = ii >= 0 and jj >= 0
    validPoint = validPoint and ii <= nRows - 1 and jj <= nCols - 1

    return validPoint


def computeBasins( map, directions):

    ( nRows, nCols) = map.shape

    mapped = []
    basins = []

    for ii in range( nRows ):
        for jj in range( nCols ):

            if map[ ii, jj] == 9: mapped.append( ( ii, jj) )
            if ( ii, jj) in mapped: continue

            mapped.append( ( ii, jj) )
            nextPositions = [( ii, jj)]

            basin = [( ii, jj)]
            moving = True

            while moving:

                currentPositions = nextPositions
                nextPositions = []
                
                for position in currentPositions:

                    currentII = position[0]
                    currentJJ = position[1]

                    for dir in directions:
                        
                        nextII = currentII + dir[0]
                        nextJJ = currentJJ + dir[1]
                        nextPosition = ( nextII, nextJJ)

                        validPoint = checkPointValidity( nextII, nextJJ, nRows, nCols)

                        if not validPoint: continue
                        
                        if map[ nextII, nextJJ] == 9:
                            mapped.append( nextPosition )

                        if nextPosition not in mapped:

                            mapped.append( nextPosition )

                            nextPositions.append( nextPosition )
                            basin.append( nextPosition )

                if not nextPositions: moving = False

            basins.append( basin )

    return basins

    