import random

print("Welcome to Tic Tac Toe")
print("----------------------")

possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3

def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameBoard[x][y], end=" |")
    print("\n+---+---+---+")

def modifyArray(num, turn):
    num -= 1
    row, col = divmod(num, 3)
    gameBoard[row][col] = turn

def checkForWinner(gameBoard):
    def check_line(line):
        if all(cell == 'X' for cell in line):
            print("X has won!")
            return 'X'
        elif all(cell == 'O' for cell in line):
            print("O has won!")
            return 'O'
        return 'N'

    # Check rows
    for row in gameBoard:
        result = check_line(row)
        if result != 'N':
            return result

    # Check columns
    for col in range(3):
        result = check_line([gameBoard[row][col] for row in range(3)])
        if result != 'N':
            return result

    # Check diagonals
    result = check_line([gameBoard[i][i] for i in range(3)])
    if result != 'N':
        return result

    result = check_line([gameBoard[i][2 - i] for i in range(3)])
    if result != 'N':
        return result

    return 'N'


def IA():
    ## Logique pour l'IA
    for i in range(3):
        # Vérification des lignes

        if gameBoard[i][0] == "O" and gameBoard[i][1] == "O" and gameBoard[i][2] != "O" and gameBoard[i][2] != "X":
            gameBoard[i][2] = "O"
            return
        elif gameBoard[i][0] == "O" and gameBoard[i][2] == "O" and gameBoard[i][1] != "O" and gameBoard[i][2] != "X":
            gameBoard[i][1] = "O"
            return
        elif gameBoard[i][1] == "O" and gameBoard[i][2] == "O" and gameBoard[i][0] != "O" and gameBoard[i][2] != "X":
            gameBoard[i][0] = "O"
            return
        
        if gameBoard[i][0] == "X" and gameBoard[i][1] == "X" and gameBoard[i][2] != "O":
            gameBoard[i][2] = "O"
            return
        elif gameBoard[i][0] == "X" and gameBoard[i][2] == "X" and gameBoard[i][1] != "O":
            gameBoard[i][1] = "O"
            return
        elif gameBoard[i][1] == "X" and gameBoard[i][2] == "X" and gameBoard[i][0] != "O":
            gameBoard[i][0] = "O"
            return

        # Vérification des colonnes
        elif gameBoard[0][i] == "O" and gameBoard[1][i] == "O" and gameBoard[2][i] != "O" and gameBoard[i][2] != "X":
            gameBoard[2][i] = "O"
            return
        elif gameBoard[0][i] == "O" and gameBoard[2][i] == "O" and gameBoard[1][i] != "O" and gameBoard[i][2] != "X":
            gameBoard[1][i] = "O"
            return
        elif gameBoard[1][i] == "O" and gameBoard[2][i] == "O" and gameBoard[0][i] != "O" and gameBoard[i][2] != "X":
            gameBoard[0][i] = "O"
            return
        
        elif gameBoard[0][i] == "X" and gameBoard[1][i] == "X" and gameBoard[2][i] != "O":
            gameBoard[2][i] = "O"
            return
        elif gameBoard[0][i] == "X" and gameBoard[2][i] == "X" and gameBoard[1][i] != "O":
            gameBoard[1][i] = "O"
            return
        elif gameBoard[1][i] == "X" and gameBoard[2][i] == "X" and gameBoard[0][i] != "O":
            gameBoard[0][i] = "O"
            return
        

    # Vérification des diagonales

    if gameBoard[0][0] == "O" and gameBoard[1][1] == "O" and gameBoard[2][2] != "O" and gameBoard[i][2] != "X":
        gameBoard[2][2] = "O"
        return
    elif gameBoard[0][0] == "O" and gameBoard[2][2] == "O" and gameBoard[1][1] != "O" and gameBoard[i][2] != "X":
        gameBoard[1][1] = "O"
        return
    elif gameBoard[1][1] == "O" and gameBoard[2][2] == "O" and gameBoard[0][0] != "O" and gameBoard[i][2] != "X":
        gameBoard[0][0] = "O"
        return

    elif gameBoard[0][2] == "O" and gameBoard[1][1] == "O" and gameBoard[2][0] != "O" and gameBoard[i][2] != "X":
        gameBoard[2][0] = "O"
        return
    elif gameBoard[0][2] == "O" and gameBoard[2][0] == "O" and gameBoard[1][1] != "O" and gameBoard[i][2] != "X":
        gameBoard[1][1] = "O"
        return
    elif gameBoard[1][1] == "O" and gameBoard[2][0] == "O" and gameBoard[0][2] != "O" and gameBoard[i][2] != "X":
        gameBoard[0][2] = "O"
        return

    if gameBoard[0][0] == "X" and gameBoard[1][1] == "X" and gameBoard[2][2] != "O":
        gameBoard[2][2] = "O"
        return
    elif gameBoard[0][0] == "X" and gameBoard[2][2] == "X" and gameBoard[1][1] != "O":
        gameBoard[1][1] = "O"
        return
    elif gameBoard[1][1] == "X" and gameBoard[2][2] == "X" and gameBoard[0][0] != "O":
        gameBoard[0][0] = "O"
        return

    elif gameBoard[0][2] == "X" and gameBoard[1][1] == "X" and gameBoard[2][0] != "O":
        gameBoard[2][0] = "O"
        return
    elif gameBoard[0][2] == "X" and gameBoard[2][0] == "X" and gameBoard[1][1] != "O":
        gameBoard[1][1] = "O"
        return
    elif gameBoard[1][1] == "X" and gameBoard[2][0] == "X" and gameBoard[0][2] != "O":
        gameBoard[0][2] = "O"
        return
    
    
    
    
    
    

    # Si aucune condition n'est remplie, choisissez une case aléatoire
    cpuChoice = random.choice(possibleNumbers)
    print("\nCpu choice: ", cpuChoice)
    if cpuChoice in possibleNumbers:
        modifyArray(cpuChoice, 'O')
        possibleNumbers.remove(cpuChoice)

leaveLoop = False
turnCounter = 0
while not leaveLoop:
    printGameBoard()
    if turnCounter % 2 == 0:
        numberPicked = int(input("\nChoose a number [1-9]: "))
        if 1 <= numberPicked <= 9 and numberPicked in possibleNumbers:
            modifyArray(numberPicked, 'X')
            possibleNumbers.remove(numberPicked)
            turnCounter += 1
        else:
          print("Enter a valid number")
    else:
        IA()
        turnCounter += 1

    winner = checkForWinner(gameBoard)
    if winner != "N":
        print("\nGame over! Thank you for playing :)")
        leaveLoop = True  # Ajout de cette ligne pour terminer la boucle
