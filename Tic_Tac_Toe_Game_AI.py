# Tic-Tac-Toe Game for User vs Computer
# Offer "X" (first move) or "O" (second move)
# Play against the User with the other symbol

########## FUNCTIONS ###############
def printInfo():
    print("Welcome to TicTacToe 2.0!!!")
    print("You will be playing against Computer (AI) in this game!")
    print("Please enjoy the game.\n")
    print('Here are the coordinates to be chosen when playing game.')
    print('(0,0) | (0,1) | (0,2)')
    print('(1,0) | (1,1) | (1,2)')
    print('(2,0) | (2,1) | (2,2)')
    print("\nEnd of Info. Let's begin the game!\n")
    print("The following shows an empty board.")

def createBoard():
    '''
        Creates board with spaces in the beginning
    '''
    b = []
    for i in range(3):
        a = []
        for j in range(3):
            a.append(" ")
        b.append(a)
    return b

def printBoard(board):
    '''
        Print board
    '''
    for i in range(3):
        for j in range(3):
            if j==1:
                print("|"+board[i][j]+"|", end="")
            else:
                print(board[i][j], end="")
        print("\n")

def getPlayer(player_spec,x):
    '''
        Gets player name from symbol used
    '''
    name = ""
    for p in player_spec.keys():
        if player_spec[p][0] == x:
            name = p
            break
    return name

def updateBoard(board,symbol,position):
    '''
        Updates board for every player's move
    '''
    row,col = position[0],position[1]
    board[row][col] = symbol
    return board

def choosePlayerNum():
    '''
        Asks user to choose X(1st player) or O(2nd player)
    '''
    # Ask user to choose X as first player or O as second player
    while 1:
        uip = input("Please select X as first player or O as second player.")
        uip = uip[0].upper()
        if uip == 'X':
            print("You have selected X as first player.")
            symy = uip
            symc = 'O'
            x_turny = 1 # first player
            x_turnc = 2 # second player
            player_list = ["You","Computer"]
            break
        elif uip == 'O':
            print("You have selected O as second player.")
            symy = uip
            symc = 'X'
            x_turny = 2
            x_turnc = 1
            player_list = ["Computer","You"]
            break
        else:
            print("Please enter correct input: X or O.")
            continue
    
    # {player : [symbol,turn]} Here turn means first or second player
    player_spec = {"You" : [symy,x_turny] , "Computer" : [symc,x_turnc]}
    
    return player_spec,player_list

def checkPositionValidity(board,position):
    '''
        Check if the position in board is empty
    '''
    if board[position[0]][position[1]] == " ":
        boolres = True
    else:
        boolres = False
    return boolres

def checkHorizontalWin(player_spec,board,winPlayer):
    '''
        Check for horizontal win
    '''
    flag = False
    for i in range(3):
        if ( (board[i][0] == board[i][1] ) and (board[i][2] == board[i][1]) and (board[i][0] != " ") ):
            flag = True
            winPlayer = getPlayer(player_spec,board[i][0])
            break   
    return flag,winPlayer

def checkVerticalWin(player_spec,board,winPlayer):
    '''
        Check for vertical win
    '''
    flag = False
    for i in range(3):
        if ( (board[0][i] == board[1][i]) and (board[1][i] == board[2][i]) and (board[2][i] != " ") ):
            flag = True
            winPlayer = getPlayer(player_spec,board[0][i])
            break   
    return flag,winPlayer

def checkDiagonalWin(player_spec,board,winPlayer):
    '''
        Check for diagonal win
    '''
    flag = False
    if ( (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]) and (board[2][2] != " ") ):
        flag = True
        winPlayer = getPlayer(player_spec,board[1][1])
    elif ( (board[0][2] == board[1][1]) and (board[1][1] == board[2][0]) and (board[2][0] != " ") ):  
        flag = True
        winPlayer = getPlayer(player_spec,board[1][1])        
    
    return flag,winPlayer

def checkPlayerWin(player_spec,board):
    '''
        Check for all types of win
    '''
    win_flag = False
    winPlayer = ""
    
    H,winPlayer = checkHorizontalWin(player_spec,board,winPlayer)
    V,winPlayer = checkVerticalWin(player_spec,board,winPlayer)
    D,winPlayer = checkDiagonalWin(player_spec,board,winPlayer)
    
    win_flag = H | V | D
    return win_flag , winPlayer

def checkEndGame(turn_count,MAX_TURNS,winGame):
    '''
        Check if game ended
        Game only ends when a player has won or all board positions have been filled up
    '''
    # End of every loop, check if game ended
    noMoreTurns = False        
    if turn_count == MAX_TURNS:
        noMoreTurns = True
        
    endGame = winGame | noMoreTurns
    return endGame,noMoreTurns
        
def minimax(board,player,player_spec,MAX_TURNS,scoreDict,turn_count):
    '''
        Minmax algorithm for AI:
            User - minimizer --> tries to get minimum of negative score
            Computer - maximizer --> tries to get maximum of positive score
            
        This is a simple algorithm without any concern on the depth of the decision tree
    '''
    winGame,p = checkPlayerWin(player_spec,board)
    endGame,_ = checkEndGame(turn_count,MAX_TURNS,winGame)
    if endGame:
        if winGame:
            score = scoreDict[p]
        else:
            score = scoreDict['Tie']
        # game ended when predicting so return score
        return score 
    #----------------------------------------------------------
    else:
        if player == "Computer": # maximizing
        
            bestScore = -np.inf
            for i in range(3):
                for j in range(3):
                    if checkPositionValidity(board,[i,j]):
                        board[i][j] = player_spec[player][0]
                        score = minimax(board,"You",player_spec,MAX_TURNS,scoreDict,turn_count+1)
                        board[i][j] = ' '
                        bestScore = max(score,bestScore)

    
        else: # player = "You" --> minimizing
        
            bestScore = np.inf
            for i in range(3):
                for j in range(3):
                    if checkPositionValidity(board,[i,j]):
                        board[i][j] = player_spec[player][0]
                        score = minimax(board,"Computer",player_spec,MAX_TURNS,scoreDict,turn_count+1)
                        board[i][j] = ' '
                        bestScore = min(score,bestScore)
                        
        return bestScore


def aiMove(board,player,player_spec,MAX_TURNS,scoreDict,turn_count):
    '''
        Move implemnented by AI--> starter of minimax
    '''
    bestScore = -np.inf
    bestPos = [3,3]

    for i in range(3):
        for j in range(3):
            if checkPositionValidity(board,[i,j]):
                board[i][j] = player_spec[player][0]
                # Best move of AI is to block the winning spot 
                # for the user which means it needs to predict what
                # user's best move will be. Therefore, the minimax
                # function will invovle the user to know user's move.
                score = minimax(board,"You",player_spec,MAX_TURNS,scoreDict,turn_count)
                board[i][j] = ' '
                if (score > bestScore):
                    bestScore = score
                    bestPos = [i,j]
    return bestPos


def playTicTacToe():
    '''
        Play entire game
    '''  
    # Initiate Variables/Flags
    MAX_TURNS = 9
    turn_count = 0
    # game completed when a player wins or all 9 spaces filled up
    winA = winB = winGame = endGame = noMoreTurns = False 
    
    
    # Initiate Game
    printInfo()
    board = createBoard()
    printBoard(board)
    
    # Create score points
    scoreDict = {"You":-1 , "Computer":1, "Tie":0 }
    
    # Ask user to choose X as first player or O as second player
    player_spec,player_list = choosePlayerNum()
    # Get 1st player to start game
    val = 0
    next_player = player_list[val]
    
    # Start Game using while loop
    while(not endGame):
        
        # Increment turn count
        turn_count += 1
        
        # Get current player
        player = next_player
        # Get symbol for current player
        symbol = player_spec[player][0]
        
        if player == "You":
            # Your move
            # Input for positon to be in this format: row,col where 0<=row<=2 and 0<=col<=2
            while 1:
                try:
                    print("############################################################################")
                    uip = input("Enter {}r position, please (format: row,col where 0<=row<=2 and 0<=col<=2) : ".format(player))
                    uip=uip.split(",")
                    position = [int(uip[0]),int(uip[1])]
                    if checkPositionValidity(board,position):
                        print("Turn count: {}".format(turn_count), end = "\t")
                        print("{} chose row {} and col {} \n".format(player,uip[0],uip[1]))
                        break
                    else:
                        print("This position is already occupied. Please choose a correct position.")
                except:
                    print("Please enter a valid input. (format: row,col where 0<=row<=2 and 0<=col<=2)")

        else:
            # Computer's move (AI)
            print("############################################################################")
            print("Computer is thinking...")
            position = aiMove(board,player,player_spec,MAX_TURNS,scoreDict,turn_count)
            print("Turn count: {}".format(turn_count), end = "---")
            print("{} chose row {} and col {} \n".format(player,position[0],position[1]))
           
        
        # Update board
        board = updateBoard(board,symbol,position)
        printBoard(board)
        
        # Prepare to call next player for next turn
        val = 1-val # 1-val toggles 0 and 1
        next_player = player_list[val]
        
             # Check for win
        winGame , _ = checkPlayerWin(player_spec,board)
        endGame,noMoreTurns = checkEndGame(turn_count,MAX_TURNS,winGame)
                
        if endGame == False:
            print("No winner found! Game continues...\n")
            print("############################################################################")
            
    
   #-------------------------------------------------- 
    # After game ended
    if noMoreTurns:
        print("Game ended as all 9 spaces on board are filled. So, its a draw!")
    elif winGame:
        print("Game ended as {} won!".format(player))


############ MAIN ###############
playTicTacToe()