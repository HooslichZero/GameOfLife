import random


n=20 # Number of cells in grid (i.e. grid will be nxn cells)


def nextBoard(board):

    """Generate the next board with updated conditions for each square"""

    for i in range(0,n):
        for j in range(0,n):    
            neighbours = 0
            
            if i >= 1:
                if j >= 1:
                    if board[i-1][j-1] == 1:
                        neighbours += 1
                if j <= n-2:
                    if board[i-1][j+1] == 1:
                        neighbours += 1
                if board[i-1][j] == 1:
                    neighbours += 1

            if i <= n-2:
                if j >= 1:
                    if board[i+1][j-1] == 1:
                        neighbours += 1
                if j <= n-2:
                    if board[i+1][j+1] == 1:
                        neighbours += 1
                if board[i+1][j] == 1:
                    neighbours += 1

            if j >= 1:
                if board[i][j-1] == 1:
                        neighbours += 1

            if j <= n-2:
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

    board = [['  ' for x in xrange(n)] for x in xrange(n)]

    for i in range((n/2)-5,(n/2)+5):
        for j in range((n/2)-5,(n/2)+5):
            x = random.randint(0,6) 
            if x == 1:
                board[i][j] = 1
            else:
                board[i][j] = 0

    return board


def printBoard():

    """Prints the board in the console window"""

    for i in range(0,n):
        storeStr = ""
        for j in range(0,n):
            if board[i][j] == 1:
                storeStr += '@'
            else:
                storeStr +=  '  '
        print storeStr


def updatePos(board):

    """Sets the array of current states equal to the values stored in the array of next states"""

    for i in range(0,n):
        for j in range(0,n):
            newBoard = nextBoard(board)

    for i in range(0,n):
        for j in range(0,n):
            board[i][j] = newBoard[i][j]


    return board


newBoard = [['  ' for x in xrange(n)] for x in xrange(n)]


def makeGlider(board):

    """Create a glider in the top left hand corner of board"""

    for i in range(0,n):
        for j in range(0,n):
        
            board[i][j] = 0

    board[3][3] = 1
    board[4][3] = 1
    board[5][3] = 1
    board[5][2] = 1
    board[4][1] = 1

    return board

