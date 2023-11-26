import numpy as np

def parseData( lines ):

    dots = np.empty([2,0])
    axises = np.empty([2,0])

    mode = "dots"

    for line in lines:

        line = line.replace("\n", "")
        print( line )

        if not line:
            mode = "folds"
            continue

        if mode == "dots":

            line = line.split(",")

            x = int( line[0] )
            y = int( line[1] )

            dot = np.array([[x], [y]])
            dots = np.hstack(( dots, dot))

        elif mode == "folds":

            line = line.split("=")
            axis = line[0][-1]
            location = int( line[1] )

            print( axis, location)

            if axis == "x":
                v = np.array([[location], [0]])
            else:
                v = np.array([[0], [location]])

            axises = np.hstack(( axises, v))

    return ( dots, axises.transpose())

def plotDots( dots ):

    x = dots[0,:]
    y = dots[1,:]

    nDots = len( x )
    print( nDots )

    minX = np.min( x )
    maxX = np.max( x )

    minY = np.min( y )
    maxY = np.max( y )

    nX = maxX - minX + 1
    nY = maxY - minY + 1

    nX = int( nX )
    nY = int( nY )

    dotMatrix = np.zeros(( nY, nX))

    for ii in range( nDots ):
        
        dotII = y[ii] - minY
        dotJJ = x[ii] - minX

        dotII = int( dotII )
        dotJJ = int( dotJJ )

        dotMatrix[ dotII, dotJJ] = int(1)

    print( dotMatrix )
    np.savetxt( "mat.txt", dotMatrix, fmt='%.1d')
