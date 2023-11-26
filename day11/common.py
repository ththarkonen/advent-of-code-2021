
import numpy as np

def parseOctopiEnergies( lines ):

    nRows = len( lines )
    nCols = len( lines[0] ) - 1

    octopiEnergies = np.zeros([ nRows, nCols])

    for ii in range( nRows ):
        for jj in range( nCols ):
            octopiEnergies[ ii, jj] = int( lines[ii][jj] )

    return octopiEnergies