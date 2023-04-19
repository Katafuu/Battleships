import random as rand
import string
import itertools


def generateBoard(rows,columns,numOfShips):
    board = []
    for i in range(rows):
        board.append(["W"] * columns)
    for x in range(numOfShips):
        randnum2 = rand.randint(0,columns-1)
        randnum = rand.randint(0,rows-1)
        board[randnum][randnum2] = "S"
    return board

def CartesianLetterGen():
    size = 1
    while True:
        for s in itertools.product(string.ascii_uppercase, repeat=size):
            yield "".join(s)
        size += 1
gen = CartesianLetterGen()
def LetterGenerator():
    for s in gen:
        return s

def printLetters(columns):
    letters = []
    for place in range(columns):
        letters.append(LetterGenerator())
    return letters

realBoard = []


# def seperator():
#     row = len(realBoard)
#     multiplier = (31 // 7 )**2
#     multi2 = int(31 % 7)
#     print('-' * multiplier, end='')
#     print('-' * multi2)
# def seperator():
#     row = len(realBoard)
#     multiplier = (31 // 7 )**2
#     multi2 = int(31 % 7)
#     print('-' *5*row)
#dont know if i want any seperators



def printboard(board):
    row = len(board)
    col = len(board[0])
    letters = printLetters(col)
    global gen
    gen = CartesianLetterGen()  # this resets the generator object
    num = []
    for x in range(1,row+1):
        num.append(f'{x} ')


    print("  ", end=" ")
    print(*letters,sep=" | ", end='')
    print('')
    # seperator()
    for counter,val in enumerate(board):
        print(num[counter], end=" ")
        print(*val, sep=" | ")
        # seperator()
