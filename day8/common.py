
display = {}
display["abcefg"] = 0
display["cf"] = 1
display["acdeg"] = 2
display["acdfg"] = 3
display["bcdf"] = 4
display["abdfg"] = 5
display["abdefg"] = 6
display["acf"] = 7
display["abcdefg"] = 8
display["abcdfg"] = 9

def parseInputLine( inputLine ):

    inputs = inputLine.split(" ")
    inputs.pop()

    segmentMapping = {}
    segmentMapping["a"] = ""
    segmentMapping["b"] = ""
    segmentMapping["c"] = ""

    segmentMapping["d"] = ""
    segmentMapping["e"] = ""
    segmentMapping["f"] = ""
    segmentMapping["g"] = ""

    mapped = set()

    # Parse d-segment
    one = ""
    four = ""
    seven = ""
    eight = ""

    for code in inputs:

        n = len( code )
        if n == 2: one = set( code )
        if n == 3: seven = set( code )
        if n == 4: four = set( code )
        if n == 7: eight = set( code )

    segmentToA = one.symmetric_difference( seven )
    segmentToA = "".join( segmentToA )

    mapped.add( segmentToA )
    segmentMapping[ segmentToA ] = "a"

    # Parse g segment
    nine = ""

    for code in inputs:

        n = len( code )
        if n == 6:
            nine = set( code )
            diff = four.symmetric_difference( nine ).symmetric_difference( mapped )

            if len( diff ) == 1 and list(diff)[0] not in mapped:
                break

    segmentToG = "".join( diff )

    mapped.add( segmentToG )
    segmentMapping[ segmentToG ] = "g"

    # Parse d segment
    three = ""

    for code in inputs:

        n = len( code )
        if n == 5:
            three = set( code )
            diff = one.symmetric_difference( three ).symmetric_difference( mapped )

            if len( diff ) == 1 and list(diff)[0] not in mapped:
                break
    
    segmentToD = "".join( diff )

    mapped.add( segmentToD )
    segmentMapping[ segmentToD ] = "d"

    # Parse e segment
    diff = eight.symmetric_difference( nine )
    segmentToE = "".join( diff )

    mapped.add( segmentToE )
    segmentMapping[ segmentToE ] = "e"

    # Parse b
    threeED = three
    threeED.add( segmentToE )
    threeED.remove( segmentToD )

    for code in inputs:

        n = len( code )
        if n == 6:

            zero = set( code )
            diff = threeED.symmetric_difference( zero )

            if len( diff ) == 1 and list(diff)[0] not in mapped:
                break
    
    segmentToB = "".join( diff )

    mapped.add( segmentToB )
    segmentMapping[ segmentToB ] = "b"

    # Parse f segment
    eightB = eight
    eightB.remove( segmentToB )

    for code in inputs:

        n = len( code )
        if n == 5:
            two = set( code )
            diff = eightB.symmetric_difference( two )

            if len( diff ) == 1 and list(diff)[0] not in mapped:
                break

    segmentToF = "".join( diff )

    mapped.add( segmentToF )
    segmentMapping[ segmentToF ] = "f"

    # Parse C segment
    eightE = eight
    eightE.add( segmentToB )
    eightE.remove( segmentToE )

    for code in inputs:

        n = len( code )
        if n == 5:
            five = set( code )
            diff = eightE.symmetric_difference( five )

            if len( diff ) == 1 and list(diff)[0] not in mapped:
                break
    
    segmentToC = "".join( diff )

    mapped.add( segmentToC )
    segmentMapping[ segmentToC ] = "c"

    return segmentMapping


def parseOutputLine( output, mapping):

    output = output.replace("\n", "")
    codes = output.split(" ")
    codes.pop(0)

    displayNumber = 0
    
    counter = 3
    for code in codes:

        segments = ""
        for letter in code:
            
            segmentOn = mapping[letter]
            segments = segments + segmentOn
        
        segments = sorted( segments )
        segments = "".join( segments )

        number = display[segments]
        displayNumber = displayNumber + number * 10 ** counter
        counter = counter - 1

    return displayNumber
    