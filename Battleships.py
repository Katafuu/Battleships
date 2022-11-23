with open("ships.txt","r") as f:
  line1,line2,line3,line4,line5,line6,line7,line8  = f.read().split("\n")

#I First began by loading the file, each line in the txt file will be a list, I made the seperate variables a list by using the .split function
game = []
def refreshgame():
  global game
  for lists in [line1,line2,line3,line4,line5,line6,line7,line8]:
    newli = convert(lists)
    game.append(newli)
    #This is so that the game can  be updated with 
def printgame():
  refreshgame()
  num = ["1)","2)","3)","4)","5)","6)","7)","8)"]
  letters = ["A","B","C","D","E","F","G"]
  i = -1
  print(" ",end=" ")
  for x in letters:
    print(*x,end=" ")
  print("")
  for x in game:
    i = i+1
    print(num[i],end="")
    print(*x,sep=" ")
def convert(string):
    li = list(string.split(","))
    return li
    #This was to convert the lines that I extracted from the txt to make each letter it's own list element, by splitting everything that was seperated by a "," into a list
def checkships():
  shipnums = 0
  for n in range(8):
    shipnums += game[n].count("S")
  return shipnums
  #this checks the num of ships left on the table by counting the number of "S" appearances in each row, then adding that number to a variable called shipnums
printgame()
#print("Num of ships:",checkships())

shipnums = checkships()
while shipnums > 0:
  shipnums = checkships()
  print("There are",shipnums,"ships left\n")
  gridselec = input("Enter a grid location:\n")
  row = ord(gridselec.upper()[0])-65
  column = int(gridselec[1])-1
  #This determines the place values of the row and  columns in the list, i used the ord() function to find the ASCII value of a letter then translated that into the list index, and similarly with the column number (COLUMN AND ROW ARE ACCIDENTALLY SWITCHED)
  if game[column][row] == "S":
    game[column][row] = "H"
    print("SCORE\n\n")
    #checks if the location of the guess on the 2d list was correct or not, and switches it's value
    try:
      printgame()
    except:
      pass
  elif shipnums == 0:
    print("YOU GOT THEM ALL!")
    #once the number of ships is 0, the game ends and you  get this message
  elif game[column][row] == "W":
    game[column][row] = "X"
    print("MISS")
    try:
      printgame()
    except:
      pass
#sources: 
#https://www.geeksforgeeks.org/python-program-convert-string-list/
#https://itsmycode.com/convert-letters-to-numbers-in-python/#:~:text=We%20can%20convert%20letters%20to%20numbers%20in%20Python%20using%20the,convert%20each%20letter%20into%20number.
#https://stackoverflow.com/questions/45027681/pythonic-way-to-print-2d-list-python
