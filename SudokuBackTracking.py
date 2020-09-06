'''
Python grid solver using backtracking algorithm.
Author: Sunny Mangat
Date: July 17, 2019

'''

# Board is a 2D list that stores our sudoku board
# 0 represent empty spots.
board = [
    [8,7,0,0,0,0,0,2,0],
    [0,0,9,8,0,6,7,1,0],
    [0,0,1,2,0,9,0,0,5],
    [0,0,5,0,0,8,0,7,0],
    [4,0,0,5,0,1,0,0,8],
    [0,6,0,7,0,0,1,0,0],
    [7,0,0,6,0,2,3,0,0],
    [0,8,6,1,0,4,2,0,0],
    [0,9,0,0,0,0,0,4,6]
]


######
#
# Function: findEmpty
# Parameter: board (2D list)
# Return: tuple (i, j) which is the empty spot on the board represented by 0
#
######
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    
    return None

###########
#
# Function: validMove
# Parameters: board (2D list), number (int), position (tuple (int, int))
# Return: bool
#
###########
def validMove(board, number, position):
    for i in range(0, len(board)):
        if (board[position[0]][i]) == number and position[1] != i:
            return False

    for i in range(len(board)):
        if board[i][position[1]] == number and position[1] != i:
            return False

    XBox = position[1]//3
    YBox = position[0]//3

    for i in range(YBox*3, YBox*3 + 3):
        for j in range(XBox*3, XBox*3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    return True



##############
#
# Function: solveBoard
# Parameters: board (2D List)
# Return: bool
#
##############

def solveBoard(board):
    find_empty = findEmpty(board)

    if find_empty:
        row, column = find_empty
    else:
        return True


    for i in range(1, 10):
        if validMove(board, i, (row, column)):
            board[row][column] = i

            if solveBoard(board):
                return True

            board[row][column] = 0

    return False    
    



#################
#
# Function: printBoard
# Parameter: board (2D List)
# return: none
#
#################

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print(board[i][j], end = "\n")
            else:
                print(str(board[i][j]) + " ", end = "")


def main():
    print("")
    print("")
    print("Original board")
    print("")

    printBoard(board)
    
    print("")
    print("")
    print("Solving the board...")
    print("")
    
    solveBoard(board)
    
    printBoard(board)


main()