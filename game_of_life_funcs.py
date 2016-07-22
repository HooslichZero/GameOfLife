
"""
Functions used for the Game of Life
"""

import random

import game_of_life_globals as gol_globals

NUM_CELLS = gol_globals.NUM_CELLS


def generate_next_board(board):

    """Generate the next board with updated conditions for each square"""

    for i in range(0,NUM_CELLS):
        for j in range(0,NUM_CELLS):
            neighbours = 0
            
            if i >= 1:
                if j >= 1:
                    if board[i-1][j-1] == 1:
                        neighbours += 1
                if j <= NUM_CELLS-2:
                    if board[i-1][j+1] == 1:
                        neighbours += 1
                if board[i-1][j] == 1:
                    neighbours += 1

            if i <= NUM_CELLS-2:
                if j >= 1:
                    if board[i+1][j-1] == 1:
                        neighbours += 1
                if j <= NUM_CELLS-2:
                    if board[i+1][j+1] == 1:
                        neighbours += 1
                if board[i+1][j] == 1:
                    neighbours += 1

            if j >= 1:
                if board[i][j-1] == 1:
                        neighbours += 1

            if j <= NUM_CELLS-2:
                if board[i][j+1] == 1:
                        neighbours += 1

            if (neighbours < 2 or neighbours >3) and board[i][j]==1:
                newBoard[i][j] = 0

            elif neighbours == 3 and board[i][j]==0:
                newBoard[i][j] = 1

            else:
                newBoard[i][j] = board[i][j]

    return newBoard


def initialiseBoard():

    """Create the board and set the middle set of squares to random states"""

    board = [['  ' for x in xrange(NUM_CELLS)] for x in xrange(NUM_CELLS)]

    for i in range((NUM_CELLS/2)-5,(NUM_CELLS/2)+5):
        for j in range((NUM_CELLS/2)-5,(NUM_CELLS/2)+5):
            x = random.randint(0,6) 
            if x == 1:
                board[i][j] = 1
            else:
                board[i][j] = 0

    return board


def printBoard():

    """Prints the board in the console window"""

    for i in range(0,NUM_CELLS):
        storeStr = ""
        for j in range(0,NUM_CELLS):
            if board[i][j] == 1:
                storeStr += '@'
            else:
                storeStr +=  '  '
        print storeStr


def updatePos(board):

    """Sets the array of current states equal to the values stored in the array of next states"""

    for i in range(0,NUM_CELLS):
        for j in range(0,NUM_CELLS):
            newBoard = generate_next_board(board)

    for i in range(0,NUM_CELLS):
        for j in range(0,NUM_CELLS):
            board[i][j] = newBoard[i][j]


    return board


newBoard = [['  ' for x in xrange(NUM_CELLS)] for x in xrange(NUM_CELLS)]


def makeGlider(board):

    """Create a glider in the top left hand corner of board"""

    for i in range(0,NUM_CELLS):
        for j in range(0,NUM_CELLS):
        
            board[i][j] = 0

    board[3][3] = 1
    board[4][3] = 1
    board[5][3] = 1
    board[5][2] = 1
    board[4][1] = 1

    return board

