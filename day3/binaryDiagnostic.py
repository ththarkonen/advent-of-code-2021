import numpy as np
import common

file = open("./day3/data.txt")
data = file.readlines()

nLines = len( data )
nBits = len( data[0] ) - 1

cutOff = 0.5 * nLines
diagnosticReport = np.empty([ nLines, nBits] )

for ii in range( nLines ):
    for jj in range( nBits ):

        bit_ii_jj = data[ii][jj]
        diagnosticReport[ii][jj] = float( bit_ii_jj )


gammaRate = diagnosticReport.sum( axis = 0 ) > cutOff
powerRate = ~gammaRate

gammaRate = gammaRate.astype( float )
powerRate = powerRate.astype( float )

gammaDecimal = common.binaryToDecimal( gammaRate )
powerDecimal = common.binaryToDecimal( powerRate ) 

result = gammaDecimal * powerDecimal
result = int( result )

print( result )
        