
import numpy as np
import common

file = open("./day11/data.txt")
lines = file.readlines()

directions = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]

octopiEnergies = common.parseOctopiEnergies( lines )

( nRows, nCols) = octopiEnergies.shape

simulationSteps = 195

flashed = 0

print("After step :", 0)
print( octopiEnergies )

step = 0
while True:

    octopiEnergies = octopiEnergies + 1

    iterationFlashes = np.argwhere( octopiEnergies > 9 )

    newFlashed = iterationFlashes
    nFlashed = len( newFlashed )

    while nFlashed > 0:

        nextFlashes = []

        for inds in newFlashed:

            ii = inds[0]
            jj = inds[1]
            
            for direction in directions:

                nextII = ii + direction[0]
                nextJJ = jj + direction[1]
                indArray = np.array([ nextII, nextJJ])

                validInds = 0 <= nextII and nextII < nRows
                validInds = validInds and 0 <= nextJJ and nextJJ < nCols

                if not validInds: continue

                octopiEnergies[ nextII, nextJJ] += 1
                
                if octopiEnergies[ nextII, nextJJ] == 10:
                    nextFlashes.append( indArray )


        newFlashed = nextFlashes
        nFlashed = len( newFlashed )

    flashInds = octopiEnergies > 9
    flashed = flashInds.astype(int).sum()

    octopiEnergies[ octopiEnergies > 9 ] = 0

    if flashed == nRows * nCols: break
    step = step + 1

print("After step :", step + 1)
print( octopiEnergies )
print( flashed )