import numpy as np

class BingoGame():
    def __init__( self, board):

        self.nRows = board.shape[0]
        self.nCols = board.shape[1]
        self.won = False

        self.board = board
        self.played = np.zeros([ self.nRows, self.nCols])

    def play( self, number):

        ind = self.board == number
        self.played[ind] = 1

        return self.checkWinCondition()

    def checkWinCondition( self ):

        rowSums = self.played.sum( axis = 0)
        colSums = self.played.sum( axis = 1)

        rowWin = np.any( rowSums == self.nRows )
        colWin = np.any( colSums == self.nCols )

        self.won = rowWin | colWin
    
    def computeBoardScore( self ):

        inds = self.played == 0.0
        unplayed = self.board[ inds ]

        boardScore = unplayed.sum()
        return boardScore