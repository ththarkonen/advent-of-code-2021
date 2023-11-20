import numpy as np

def parseVents( lines ):

    maxX = 0
    maxY = 0

    for line in lines:

        line = line.replace("\n", "")
        line = line.replace(",", "->")
        points = line.split("->")

        x0 = points[0]
        y0 = points[1]

        x1 = points[2]
        y1 = points[3]

        x0 = int( x0 )
        y0 = int( y0 )

        x1 = int( x1 )
        y1 = int( y1 )

        if np.max([ x0, x1]) > maxX:
            maxX = np.max([ x0, x1])

        if np.max([ y0, y1]) > maxY:
            maxY = np.max([ y0, y1])

    vents = np.zeros([ maxY + 1, maxX + 1])
    ventsAll = np.zeros([ maxY + 1, maxX + 1])

    for line in lines:

        line = line.replace("\n", "")
        line = line.replace(",", "->")
        points = line.split("->")

        x0 = points[0]
        y0 = points[1]

        x1 = points[2]
        y1 = points[3]

        x0 = int( x0 )
        y0 = int( y0 )

        x1 = int( x1 )
        y1 = int( y1 )

        xStart = np.min([ x0, x1])
        xStop = np.max([ x0, x1])

        yStart = np.min([ y0, y1])
        yStop = np.max([ y0, y1])

        nX = xStop - xStart + 1
        nY = yStop - yStart + 1

        if xStart == xStop or yStart == yStop:
            vents[ yStart:yStop+1, xStart:xStop+1] += 1
            ventsAll[ yStart:yStop+1, xStart:xStop+1] += 1

        elif nX == nY:

            xDirection = np.sign( x1 - x0 )
            yDirection = np.sign( y1 - y0 )

            for ii in range( nX ):

                xMove = ii * xDirection
                yMove = ii * yDirection

                ventsAll[ y0 + yMove, x0 + xMove] += 1

    return ( vents, ventsAll)