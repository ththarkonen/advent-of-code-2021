
import numpy as np
import common

file = open("./day13/data.txt")
lines = file.readlines()

( dots, axises) = common.parseData( lines )

print( dots )
print( axises )

nDots = dots.shape[1]
print( nDots )

for axis in axises:

    axis = np.tile( axis, ( nDots, 1))
    dots = dots - axis.transpose()

    if axis[0][0] == 0: dots[1,:] = -np.abs( dots[1,:] )
    else: dots[0,:] = -np.abs( dots[0,:] )

    dots = dots + axis.transpose()
    #break

dots = np.unique( dots, axis = 1)
nDots = len( dots.transpose() )

print( nDots )

common.plotDots( dots)

