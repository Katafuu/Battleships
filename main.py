import Board
import os


def checkHit(coord):
    col = ord(coord[0])-65
    row = int(coord[1])-1
    if realBoard[row][col] == "S":
        fakeBoard[row][col] = "H"
        return True
    fakeBoard[row][col] = "X"
    return False





print("-----Main Menu-----")
ch = input("1) Play\n2) Quit\n")
if ch == ('1' or 'play'):
    dimensions = input('Select the dimensions of the board format: (RowsxColumns): ')
    rows = int(dimensions[0])
    col = int(dimensions[-1])
    shipnum = int(input("Select the number of ships you would like to have: "))
    os.system('cls')
    print('')
    realBoard = Board.generateBoard(rows, col, shipnum)
    fakeBoard = Board.generateBoard(rows, col, 0)
    visited = []
    while shipnum != 0:
        Board.printboard(fakeBoard)
        sel = input("Enter coords (0 to quit): ")
        os.system('cls')
        print('')
        try:
            if sel in visited:
                raise Exception("Incorrect or already visited co-ordinates, please try again")
            elif sel == 0:
                quit()
            elif checkHit(sel):
                print("HIT!")
                shipnum -= 1
            visited.append(sel)
            # print(Board.seperator())
        except:
            print("Incorrect or already visited co-ordinates, please try again")
    print('GAME END, YOU WIN!')
    Board.printboard(realBoard)
    print("ship locations ^")
    input("Enter to exit\n")
else:
    print("Goodbye! Enter to exit")
    input()
    quit





# https://www.geeksforgeeks.org/python-program-convert-string-list/
# https://itsmycode.com/convert-letters-to-numbers-in-python/#:~:text=We%20can%20convert%20letters%20to%20numbers%20in%20Python%20using%20the,convert%20each%20letter%20into%20number.
# https://stackoverflow.com/questions/45027681/pythonic-way-to-print-2d-list-python
# https://stackoverflow.com/questions/29351492/how-to-make-a-continuous-alphabetic-list-python-from-a-z-then-from-aa-ab-ac-e
# https://www.geeksforgeeks.org/python-itertools-product/
# https://www.simplilearn.com/tutorials/python-tutorial/yield-in-python#:~:text=The%20Yield%20keyword%20in%20Python%20is%20similar%20to%20a%20return,of%20simply%20returning%20a%20value.
# https://stackoverflow.com/questions/400739/what-does-asterisk-mean-in-python#:~:text=A%20single%20star%20means%20that,that%20were%20supplied%20with%20keywords.
