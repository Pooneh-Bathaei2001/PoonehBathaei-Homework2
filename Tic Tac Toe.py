gameboard = [["-","-","-"],["-","-","-"],["-","-","-"]]
row = 3
col = 3
def show():
    for x in range(row):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range (col): 
            print("", gameboard[x][y], end =" |")
    print("\n+---+---+---+")

show()

def winnercheck():
    if gameboard[0][0] == 'x' and gameboard [0][1] == 'x' and gameboard[0][2] == 'x':
        print("player one is the winner")
    if gameboard[0][0] == 'O' and gameboard [0][1] == 'O' and gameboard[0][2] == 'O':
        print("player two is the winner")
    if gameboard[1][0] == 'x' and gameboard[1][1] == 'x' and gameboard[1][2] == 'x':
        print("player one is the winner")
    if gameboard[1][0] == 'O' and gameboard [1][1] == 'O' and gameboard[1][2] == 'O':
        print("player two is the winner")
    if gameboard[2][0] == 'x' and gameboard[2][1] == 'x' and gameboard[2][2] == 'x':
        print("player one is the winner")
    if gameboard[2][0] == 'O' and gameboard [2][1] == 'O' and gameboard[2][2] == 'O':
        print("player two is the winner")
    if gameboard[0][0] == 'x' and gameboard[1][1] == 'x' and gameboard[2][2] == 'x':
        print("player one is the winner")
    if gameboard[0][0] == 'O' and gameboard [1][1] == 'O' and gameboard[2][2] == 'O':
        print("player two is the winner")
    if gameboard[0][2] == 'x' and gameboard[1][1] == 'x' and gameboard[2][0] == 'x':
        print("player one is the winner")
    if gameboard[0][2] == 'O' and gameboard [1][1] == 'O' and gameboard[2][0] == 'O':
        print("player two is the winner")
    if gameboard[0][0] == 'x' and gameboard[1][0] == 'x' and gameboard[2][0] == 'x':
        print("player one is the winner")
    if gameboard[0][0] == 'O' and gameboard [1][0] == 'O' and gameboard[2][0] == 'O':
        print("player two is the winner")
    if gameboard[0][1] == 'x' and gameboard[1][1] == 'x' and gameboard[2][1] == 'x':
        print("player one is the winner")
    if gameboard[0][1] == 'O' and gameboard [1][1] == 'O' and gameboard[2][1] == 'O':
        print("player two is the winner")
    if gameboard[0][2] == 'x' and gameboard[1][2] == 'x' and gameboard[2][2] == 'x':
        print("player one is the winner")
    if gameboard[0][2] == 'O' and gameboard [1][2] == 'O' and gameboard[2][2] == 'O':
        print("player two is the winner")

while True:
    print("Player one (x) turn:") 
    while True:
            row = int(input("Enter your desired row: "))
            col = int(input("Enter your desired col: "))
            if 0<= row <=2 and 0<= col <=2:
                if gameboard[row][col] == "-":
                    gameboard[row][col] = "X" 
                    show()
                    winnercheck()
                    break 
                else:
                    print("This one is already taken!!!")
            else:
                print("choose between 0-2")
    if gameboard[0][0] != "-" and gameboard[0][1] != "-" and gameboard[0][2] != "-" and gameboard[1][0] != "-" and gameboard[1][1] != "-" and gameboard[1][2] != "-" and gameboard[2][0] != "-" and gameboard[2][1] != "-" and gameboard[2][2] != "-" and winnercheck() != True:
                    print("equal")
                    break
    
    print("Player two (O) turn") 
    while True:
            row = int(input("Enter your desired row: "))
            col = int(input("Enter your desired col: "))
            if 0<= row <=2 and 0<= col <=2:
                if gameboard[row][col] == "-":
                    gameboard[row][col] = "O"
                    show()
                    winnercheck()
                    break
                else:
                    print("This one is already taken!!!")
            else:
                print("choose between 0-2")
    if gameboard[0][0] != "-" and gameboard[0][1] != "-" and gameboard[0][2] != "-" and gameboard[1][0] != "-" and gameboard[1][1] != "-" and gameboard[1][2] != "-" and gameboard[2][0] != "-" and gameboard[2][1] != "-" and gameboard[2][2] != "-" and winnercheck() != True:
         print("equal")
         break