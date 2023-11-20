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


oxygenRating = common.reportScraper( diagnosticReport, keepCommon = True)
co2Rating = common.reportScraper( diagnosticReport, keepCommon = False)

oxygenDecimal = common.binaryToDecimal( oxygenRating )
co2Decimal = common.binaryToDecimal( co2Rating )

result = oxygenDecimal * co2Decimal
result = int( result )

print( result )