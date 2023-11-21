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

                try:
                    adjacentHeight = map[ nextII, nextJJ]
                    lowPoint = lowPoint and adjacentHeight >= currentHeight
                except:
                    continue

                if not lowPoint:
                    break

            if lowPoint:
                
                lowPoints = lowPoints + 1
                riskLevel = riskLevel + 1 + currentHeight

    return ( lowPoints, riskLevel)