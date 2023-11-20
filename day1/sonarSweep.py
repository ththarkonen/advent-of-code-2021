
import numpy as np

heights = np.genfromtxt("./day1/data.txt", delimiter = "\n")
changes = np.diff( heights )

increases = ( changes > 0 ).sum()
increases = str( increases )

firstKernel = np.array([0,1,1,1])
secondKernel = np.array([1,1,1,0])

firstWindowSums = np.convolve( heights, firstKernel, mode = "valid")
secondWindowSums = np.convolve( heights, secondKernel, mode = "valid")

windowChanges = secondWindowSums - firstWindowSums
windowIncreases = ( windowChanges > 0 ).sum()
windowIncreases = str( windowIncreases )

print( "Part 1: " + increases )
print( "Part 2: " + windowIncreases )


