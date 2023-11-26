
file = open("./day10/data.txt", "r")
lines = file.readlines()

leftBrackets = ["<", "[", f"{{", "("]
rightSymbols = [">", "]", f"}}", ")"]
alignedBrackets = ["<>","[]", f"{{}}", "()"]

incompleteLines = []
errors = []

for line in lines:

    lineOrig = line
    lineErrors = []

    while True:

        nPrev = len( line )

        for brackets in alignedBrackets:
            line = line.replace( brackets, "")

        nNext = len( line )

        if nPrev == nNext:  break

    for leftBracket in leftBrackets:
        for rightSymbol in rightSymbols:
            
            combination = leftBracket + rightSymbol
            
            if combination in alignedBrackets: continue

            if combination in line:

                ind = line.index( combination )
                lineErrors.append( ( ind, rightSymbol) )

    nErrors = len( lineErrors )

    if nErrors == 0:
        incompleteLines.append( line )
        continue

    lineErrors = sorted( lineErrors )
    firstError = lineErrors[0]

    errors.append( firstError )

totalSyntaxError = 0
totalScores = []

for error in errors:
    if error[1] == ")": totalSyntaxError = totalSyntaxError + 3
    elif error[1] == "]": totalSyntaxError = totalSyntaxError + 57
    elif error[1] == f"}}": totalSyntaxError = totalSyntaxError + 1197
    elif error[1] == ">": totalSyntaxError = totalSyntaxError + 25137

for line in incompleteLines:

    line = line.replace("\n", "")
    totalScore = 0

    for bracket in reversed( line ):

        totalScore = 5 * totalScore

        if bracket == "(": totalScore = totalScore + 1
        elif bracket == "[": totalScore = totalScore + 2
        elif bracket == f"{{": totalScore = totalScore + 3
        elif bracket == "<": totalScore = totalScore + 4

    totalScores.append( totalScore )

nIncompleteLines = len( incompleteLines )
middleScoreIndex = int( 0.5 * nIncompleteLines )
totalScores = sorted( totalScores )

print( totalSyntaxError )
print( totalScores[middleScoreIndex] )
