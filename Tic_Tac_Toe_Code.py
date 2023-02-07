
def getWinCondition():
    winConditions = []

    #vertical
    winConditions.append([0,8,6])
    winConditions.append([1,4,7])
    winConditions.append([2,5,8])

    #across
    winConditions.append([0,1,2])
    winConditions.append([3,4,5])
    winConditions.append([6,7,8])

    #diagonol
    winConditions.append([0,4,8])
    winConditions.append([6,4,2])

    return winConditions

#set up board
def setupBoard():
    emptyBoard = []
    for i in range(9):
        emptyBoard.append(str(i))
    return emptyBoard   

def displayBoard(copyBoard):
    strBoard =  (copyBoard[0]) + '|' + (copyBoard[1]) + '|' + (copyBoard[2]) +'\n'
    strBoard += '-----' + '\n'
    strBoard += (copyBoard[3]) + '|' + (copyBoard[4]) + '|' + (copyBoard[5]) +'\n'
    strBoard += '-----' + '\n'
    strBoard += (copyBoard[6]) + '|' + (copyBoard[7]) + '|' + (copyBoard[8]) +'\n'
    print(strBoard)

def userChoice(copyBoard, copyPlayer):
    wrongInput = True
    
    while wrongInput:
        
                
        userInput = input("Please select a square (0-8): ")
        if userInput in copyBoard:
            wrongInput = False
            copyBoard[int(userInput)] = copyPlayer

        else:
            print("Please enter a numeric value from 0-8")
        
    return copyBoard

def compChoice(copyBoard, copyPlayer):
    '''search the array for missing numbers to base the next move off of'''
    #might need a while loop to make sure there are no duplicate choices
    #think of a way to make sure the choices are tracked
    #maybe a list that contains the choices made by the user and the computer.
    
    print("------Computer Choice------")
    if 'X' in copyBoard[4]:
        copyBoard[8] = copyPlayer
    elif 'X' in copyBoard[8]:
        copyBoard[0] = copyPlayer

    return copyBoard

def checkWinner(board):
    winCheck = False
    winConditions = getWinCondition()

    for winCond in winConditions:
        first = board[winCond[0]]
        if first == board[winCond[1]] and first == board[winCond[2]]:
            winCheck = True
    return winCheck
    

#intialize variables
board = setupBoard()
count = 0
player = ''
turnTracker = 1
winner = ''

while (winner == ''):
    displayBoard(board)
    if turnTracker > 0:
        player = 'X'
    else:
        player = 'O'
    #in while user input as number, check for acceptable input
    if player == 'X':
        board = userChoice(board, player)
    else:
        board = compChoice(board, player)
    count += 1
    #check win condition
    winCheck = checkWinner(board)
    if winCheck == True:
        winner = player
    elif count > 8:
        winner = "Tie"

    turnTracker *= -1
displayBoard(board)

if winner == "Tie":
    print("It was a tie!")
else:
    print("Winner is ", player)



