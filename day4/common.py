import numpy as np
from bingoGame import BingoGame

def parseGames( lines ):

    board = []
    games = []

    resetBoard = False

    counter = 0
    for line in lines:

        if counter == 0:
            numbers = np.fromstring( line, sep = ",")
            counter = counter + 1
            continue

        if line == "\n":

            resetBoard = True
            counter = counter + 1
            
            if counter > 2:
                game = BingoGame( board )
                games.append( game )

            continue

        boardRow = np.fromstring( line, sep = " ")

        if resetBoard:
            board = boardRow
            resetBoard = False
        else:
            board = np.vstack([ board, boardRow])

    game = BingoGame( board )
    games.append( game )
    return ( numbers, games)