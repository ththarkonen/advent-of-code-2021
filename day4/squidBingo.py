import numpy as np
import common
from bingoGame import BingoGame

file = open("./day4/data.txt")
lines = file.readlines()

(numbers, games) = common.parseGames( lines )

nNumbers = len( numbers )
nGames = len( games )

winner = np.zeros([ nGames, 1], dtype = bool)

def playGames( numbers, games):
    for number in numbers:
        for game in games:

            game.play( number )
            if game.won: return ( number, game)


def findLastWinner( numbers, games):

    nGames = len( games )
    wins = 0

    for number in numbers:
        for game in games:
            
            if game.won: continue

            game.play( number )

            if game.won: wins = wins + 1
            if wins == nGames - 1: return ( number, game)

( number, game) = playGames( numbers, games)
( lastWinnerNumber, lastWinnerGame) = findLastWinner( numbers, games)

finalScore = number * game.computeBoardScore()
finalScore = int( finalScore )

losingScore = lastWinnerNumber * lastWinnerGame.computeBoardScore()
losingScore = int( losingScore )

print( finalScore )
print( losingScore )
            

    


