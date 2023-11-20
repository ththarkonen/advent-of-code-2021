import numpy as np

def binaryToDecimal( x ):
    
    decimal = 0.0
    nBits = len( x )

    for p in range( nBits ):

        power = nBits - p - 1
        decimal += x[p] * 2 ** power
    
    return decimal


def reportScraper( report, keepCommon = True):

    reportShape = report.shape
    nBits = reportShape[1]

    validIndeces = report[:,0] >= -np.Inf 
    columnLength = validIndeces.astype(int).sum()

    for columnInd in range(nBits):

        column = report[ :, columnInd]
        filteredColumn = report[ validIndeces, columnInd]

        cutoff = 0.5 * columnLength

        onesCommon = filteredColumn.sum( axis = 0 ) >= cutoff

        if keepCommon:
            if onesCommon:
                validIndeces = validIndeces & ( column == 1.0 )
            else:
                validIndeces = validIndeces & ( column == 0.0 )
        else:
            if onesCommon:
                validIndeces = validIndeces & ( column == 0.0 )
            else:
                validIndeces = validIndeces & ( column == 1.0 )
        
        columnLength = validIndeces.astype(int).sum()

        if columnLength == 1:
            return report[ validIndeces, :].flatten()