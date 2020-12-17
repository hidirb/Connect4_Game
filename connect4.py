field = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],
[" "," "," "," "," "," "],[" "," "," "," "," "," "],
[" "," "," "," "," "," "],[" "," "," "," "," "," "],
[" "," "," "," "," "," "]]

def drawField(f):
        for row in range(11):
                if row%2 == 0:
                        practRow = int(row/2)
                        for column in range(13):
                                if column%2 == 0:
                                        practColumn = int(column/2)
                                        if column != 12:
                                                print (f[practColumn][practRow], end = "")
                                        else:
                                                print(f[practColumn][practRow])
                                else:
                                        print("|", end = "")
                else:
                        print("- - - - - - -")
                                        
                                     
def updateField(n,p):
        column = field[n]
        index = ""
        columnReverse = column[::-1]
        for row in columnReverse:
                if row == " ":
                        index = columnReverse.index(row)
                        columnReverse[index] = "X" if p == 1 else "O"
                        break
        if index == "":
                return False
        column = columnReverse[::-1]
        field[n] = column
        drawField(field)
        return True

def CreateTempField():  
        TempField = [[" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],
        [" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],
        [" "," ", " "," "," "," "," "],[" "," ", " "," "," "," "," "],
        [" "," ", " "," "," "," "," "]]   
        for i in range(7):
                for c in range(len(field[i])):
                        TempField[c][i] = field[i][c]
                        return TempField        

def columnCheck(TempField):
        winner = False
        for column in TempField:
                counter = 0
                length = len(column)
                for i in range(1, length):
                    if column[i - 1] != " " and column[i] != " " and column[i -1 ] == column[i]:
                         counter += 1
                    else:
                        counter = 0
                    if counter == 3:
                        winner = column[i - 1]
                        return winner
        return winner

def rowCheck():
        winner = False
        for column in field:
                counter = 0
                length = len(column)
                for i in range(1, length):
                    if column[i - 1] != " " and column[i] != " " and column[i - 1 ] == column[i]:
                        counter += 1
                    else:
                        counter = 0
                    if counter == 3:
                        winner = column[i - 1]
                        return winner    
        return winner

def fDiagonalCheck(TempField,player):
        for i in range(0, len(TempField)):
                for j in range(0, len(TempField[i])):
                    try:
                        if TempField[i][j] == player and TempField[i + 1][j - 1] == player and TempField[i + 2][j - 2] == player and TempField[i + 3][j - 3] == player:
                            return True
                    except IndexError:
                        next

        return False

def bDiagonalCheck(TempField,player):
        for i in range(0, len(TempField)):
                for j in range(0, len(TempField[i])):
                    try:
                        if TempField[i][j] == player and TempField[i + 1][j + 1] == player and TempField[i + 2][j + 2] == player and TempField[i + 3][j + 3] == player:
                            return True
                    except IndexError:
                        next
        return False


def validMove(userInput1):
        if userInput1 >=1 and userInput1 <=7:
                return True
        else:
                return False


def start():
        playing = True
        player = 1
        winner = ""
        while(playing):
                userInput1 = int(input("Please Enter Column number here: "))
                if userInput1:
                        if validMove(userInput1) == False:
                                print("Please Try Again! ")
                        else:
                                if updateField(userInput1 -1, player):
                                        print("")
                                        cplayer = player
                                        move = "X" if player == 1 else "O"
                                        player = 2 if player == 1 else 1
                                        winner = rowCheck()
                                        if winner:
                                                playing = False
                                        else:
                                                TempField = CreateTempField()
                                                winner = columnCheck(TempField)
                                                if winner:
                                                        playing = False
                                                elif bDiagonalCheck(TempField, move):
                                                        winner = cplayer
                                                        playing = False
                                                elif fDiagonalCheck(TempField, move):
                                                        winner = cplayer
                                                        no_win = False
                                else:
                                        print("Please Try again.\n")
                else:
                        print("Please Try again.\n")

        if winner == "X":
            winner = "1"
            print("CONGRATULATIONS!!!! PLAYER "+ str(winner))
        else:
            winner = "2"
            print("CONGRATULATIONS!!!! PLAYER "+ str(winner))

                 
drawField(field)
start()

        

                                        
