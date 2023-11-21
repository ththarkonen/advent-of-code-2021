import common

file = open("./day8/data.txt")
lines = file.readlines()

uniqueLengths = [ 2, 3, 4, 7]

nUniqueLetters = 0

for line in lines:

    output_ii = line.split("|")
    output_ii = output_ii[1]
    
    individualOutput_ii = output_ii.split(" ")
    
    for letter in individualOutput_ii:

        letter = letter.replace("\n", "")
        sortedLetter = ''.join( sorted( letter ) )

        nLetters = len( letter )

        if nLetters in uniqueLengths:
            print( letter, nLetters)
            nUniqueLetters = nUniqueLetters + 1

print( nUniqueLetters )

result = 0
for line in lines:

    line_ii = line.split("|")

    input_ii = line_ii[0]
    output_ii = line_ii[1]

    mapping = common.parseInputLine( input_ii )
    displayNumber = common.parseOutputLine( output_ii, mapping)

    result = result + displayNumber
    print( displayNumber )
    #break

print( result )




