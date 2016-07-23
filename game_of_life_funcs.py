
"""
Functions used for the Game of Life
"""

import random

def count_neighbours(board, NUM_ROWS):

    """
    Return an array where each cell tells us how
    many neighbours that cell has in the current
    board.
    """

    neighbours_board = [[0 for _ in xrange(NUM_ROWS)] for _ in xrange(NUM_ROWS)]

    for i in range(0, NUM_ROWS):
        for j in range(0, NUM_ROWS):

            neighbours = 0

            if i >= 1:
                if j >= 1:
                    if board[i-1][j-1] == 1:
                        neighbours += 1
                if j <= NUM_ROWS-2:
                    if board[i-1][j+1] == 1:
                        neighbours += 1
                if board[i-1][j] == 1:
                    neighbours += 1

            if i <= NUM_ROWS-2:
                if j >= 1:
                    if board[i+1][j-1] == 1:
                        neighbours += 1
                if j <= NUM_ROWS-2:
                    if board[i+1][j+1] == 1:
                        neighbours += 1
                if board[i+1][j] == 1:
                    neighbours += 1

            if j >= 1:
                if board[i][j-1] == 1:
                    neighbours += 1

            if j <= NUM_ROWS-2:
                if board[i][j+1] == 1:
                    neighbours += 1

            neighbours_board[i][j] = neighbours

    return neighbours_board


def generate_next_board(board, NUM_ROWS):

    """Generate the next board with updated conditions for each square"""

    neighbours_board = count_neighbours(board, NUM_ROWS)
    new_board = [[0 for _ in xrange(NUM_ROWS)] for _ in xrange(NUM_ROWS)]

    for i in xrange(NUM_ROWS):
        for j in xrange(NUM_ROWS):

            neighbours = neighbours_board[i][j]

            if (neighbours < 2 or neighbours > 3) and board[i][j] == 1:
                new_board[i][j] = 0

            elif neighbours == 3 and board[i][j] == 0:
                new_board[i][j] = 1

            else:
                new_board[i][j] = board[i][j]

    return new_board


def initialiseBoard(NUM_ROWS):

    """Create the board and set the middle set of squares to random states"""

    board = [[0 for _ in xrange(NUM_ROWS)] for _ in xrange(NUM_ROWS)]

    # Probability that a cell in the centre of the grid is alive at the start
    alive_probability = 0.2

    for i in range((NUM_ROWS/2)-5, (NUM_ROWS/2)+5):
        for j in range((NUM_ROWS/2)-5, (NUM_ROWS/2)+5):
            board[i][j] = int(random.random() <= alive_probability)

    return board


def printBoard(NUM_ROWS):

    """Prints the board in the console window"""

    for i in range(0, NUM_ROWS):
        storeStr = ""
        for j in range(0, NUM_ROWS):
            if board[i][j] == 1:
                storeStr += '@'
            else:
                storeStr += '  '
        print storeStr


def makeGlider(board, NUM_ROWS):

    """Create a glider in the top left hand corner of board"""

    for i in range(0, NUM_ROWS):
        for j in range(0, NUM_ROWS):

            board[i][j] = 0

    board[3][3] = 1
    board[4][3] = 1
    board[5][3] = 1
    board[5][2] = 1
    board[4][1] = 1

    return board

