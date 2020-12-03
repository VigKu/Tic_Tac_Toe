# Tic-Tac-Toe Game for 2 Players
# Write your code in this cell

########## FUNCTIONS ###############

def createBoard():
    b = []
    for i in range(3):
        a = []
        for j in range(3):
            a.append(" ")
        b.append(a)
    return b

def printBoard(board):
     for i in range(3):
        for j in range(3):
            if j==1:
                print("|"+board[i][j]+"|", end="")
            else:
                print(board[i][j], end="")
        print("\n")

#def getPlayer(player_spec,x):
#    name = ""
#    for p in player_spec.keys():
#        if player_spec[p][0] == x:
#            name = p
#            break
#    return name

def updateBoard(board,symbol,position):
    row,col = position[0],position[1]
    board[row][col] = symbol
    return board

def checkHorizontalWin(player_spec,board,symbol):
    flag = False
    for i in range(3):
        if ( (board[i][0] == symbol) and (board[i][1] == symbol) and (board[i][2] == symbol) ):
            flag = True
            #winPlayer = getPlayer(player_spec,board[i][0])
            break   
    return flag

def checkVerticalWin(player_spec,board,symbol):
    flag = False
    for i in range(3):
        if ( (board[0][i] == symbol) and (board[1][i] == symbol) and (board[2][i] == symbol) ):
            flag = True
            #winPlayer = getPlayer(player_spec,board[0][i])
            break   
    return flag

def checkDiagonalWin(player_spec,board,symbol):
    flag = False
    if ( (board[0][0] == symbol) and (board[1][1] == symbol) and (board[2][2] == symbol) ):
        flag = True
        #winPlayer = getPlayer(player_spec,board[1][1])
    elif ( (board[0][2] == symbol) and (board[1][1] == symbol) and (board[2][0] == symbol) ):  
        flag = True
        #winPlayer = getPlayer(player_spec,board[1][1])        
    
    return flag

def checkPlayerWin(player_spec,board,symbol):
    win_flag = False
    
    H = checkHorizontalWin(player_spec,board,symbol)
    V = checkVerticalWin(player_spec,board,symbol)
    D = checkDiagonalWin(player_spec,board,symbol)
    
    win_flag = H | V | D
    return win_flag , player_spec


def playTicTacToe():
    
    # Initiate Variables/Flags
    MAX_TURNS = 9
    turn_count = 0
    # game completed when a player wins or all 9 spaces filled up
    winA = winB = winGame = endGame = noMoreTurns = False 
    #winPlayer = ""
    player_list = ["UserA","UserB"]
    
    # Randomly decides if UserA or UserB will start game first
    val = random.randint(0, 1)
    next_player = player_list[val]
    
    
    # Initiate Game
    player_spec = {"UserA" : ["X",winA] , "UserB" : ["O",winB]} # {player : [sumbol,win flag]}
    board = createBoard()
    printBoard(board)
    
    
    # Start Game using while loop
    while(not endGame):
        
        # Input position
        turn_count += 1 # increment turn count
        player = next_player
        
        # Input for positon to be in this format: row,col where 0<=row<=2 and 0<=col<=2
        input_flag = True
        while input_flag:
            uip = input("Enter {}'s position, please : ".format(player))
            uip=uip.split(",")
            position = [int(uip[0]),int(uip[1])]
            if board[position[0]][position[1]] == " ":
                print(turn_count, end = "\t")
                print("{} chose row {} and col {} \n".format(player,uip[0],uip[1]))
                input_flag = False
            else:
                print("This position is already occupied. Please choose a correct position.")
            
        # Prepare to call next player for next turn
        val = 1-val # 1-val toggles 0 and 1
        next_player = player_list[val]
        
        # Get symbol for player
        symbol = player_spec[player][0]
        
        # Update board
        board = updateBoard(board,symbol,position)
        printBoard(board)
        
        # Check for win
        winGame , player_spec = checkPlayerWin(player_spec,board,symbol)
        
        # End of every loop
        if turn_count == MAX_TURNS:
            noMoreTurns = True
        
        endGame = winGame | noMoreTurns
        
        if endGame == False:
            print("No winner found! Game continues...\n")
            print("----------------------------------\n")
            
    
   #-------------------------------------------------- 
    # After game ended
    if noMoreTurns:
        print("Game ended as all 9 spaces on board are filled. So, its a draw!")
    elif winGame:
        print("Game ended as player: {} won!".format(player))
    
############ MAIN ###############

import random
playTicTacToe()