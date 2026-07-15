def print_board(board):
    print("  0   1   2")
    for i in range(0,3):
        print(i, board[i][0], "|", board[i][1], "|", board[i][2])
        if (i < 2):
            print("  --+---+--")
    print("\n")

def check_winner(board):
    for i in range(0,3):
        if(board[i][0]!=' ' and board[i][0]==board[i][1] and board[i][1]==board[i][2]):
            if(board[i][0]=='X'):
                return 1
            else:
                return -1
        if(board[0][i]!=' 'and board[0][i]==board[1][i]and board[1][i]==board[2][i]):
            if(board[0][i]=='X'):
                return 1
            else:
                return -1
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' '):
        if (board[0][0] == 'X'):
            return 1
        else:
            return -1
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' '):
        if (board[0][2] == 'X'):
            return 1
        else:
            return -1
    return 0

def is_full(board):
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j]==' '):
                return False
    return True

def minimax(board, depth, isMaximizing):
    winner = check_winner(board)
    if (winner == 1):
        return 1
    if (winner == -1):
        return -1
    if (is_full(board)):
        return 0
    if (isMaximizing):
        best_score = -1000
        for i in range(0,3):
            for j in range(0,3):
                if (board[i][j] == ' '):
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    if (score > best_score):
                        best_score = score
        return best_score
    else:
        best_score = 1000
        for i in range(0,3):
            for j in range(0,3):
                if (board[i][j] == ' '):
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    if (score < best_score):
                        best_score = score
        return best_score

def best_move_minimax(board):
    best_score = 1000
    move = (-1, -1)
    for i in range(0,3):
        for j in range(0,3):
            if (board[i][j] == ' '):
                board[i][j] = 'O'
                score = minimax(board, 0, True)
                board[i][j] = ' '
                if (score < best_score):
                    best_score = score
                    move = (i, j)
    return move

prune_count = 0
def alphabeta(board, alpha, beta, is_maximizing):
    global prune_count
    winner = check_winner(board)
    if(winner != 0):
        return winner
    if(is_full(board)):
        return 0
    if(is_maximizing):  
        best_score = -1000
        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j] == ' '):
                    board[i][j] = 'X'
                    temp = alphabeta(board, alpha, beta, False)
                    board[i][j] = ' '
                    best_score = max(best_score, temp)
                    alpha = max(alpha, best_score)
                    if(beta <= alpha):
                        prune_count += 1
                        return best_score
        return best_score
    else: 
        best_score = 1000
        for i in range(0,3):
            for j in range(0,3):
                if(board[i][j] == ' '):
                    board[i][j] = 'O'
                    temp = alphabeta(board, alpha, beta, True)
                    board[i][j] = ' '
                    best_score = min(best_score, temp)
                    beta = min(beta, best_score)
                    if(beta <= alpha):
                        prune_count += 1
                        return best_score
        return best_score

def best_move_alphaBeta(board):
    global prune_count
    best_score = 1000
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if(board[i][j] == ' '):
                board[i][j] = 'O'
                score = alphabeta(board, -1000, 1000, True)
                board[i][j] = ' '
                if(score < best_score):
                    best_score = score
                    best_move = (i, j)
    return best_move

def simulate_game():
    global prune_count
    choice=0
    count_tmp=-1
    while(not(choice==1) and not(choice==2)):
        count_tmp+=1
        choice=int(input("1. Minimax\n2. Alpha-Beta\nEnter your choice: "))
        if(count_tmp>=1):
            print("Invalid Choice please enter valid choice\n")
    
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print_board(board)
    
    if(choice==1):
        while (check_winner(board) == 0 and not is_full(board)):
            x = int(input("Enter row (0-2): "))
            y = int(input("Enter column (0-2): "))
            if (x < 0 or x > 2 or y < 0 or y > 2 or board[x][y] != ' '):
                print("Invalid move. Try again.\n")
            else:
                board[x][y] = 'X'
                print("Board after your move:")
                print_board(board)
                if (check_winner(board) != 0 or is_full(board)):
                    break
                move = best_move_minimax(board)
                if (move != (-1, -1)):
                    board[move[0]][move[1]] = 'O'
                    print("Computer's move: Row", move[0], "Column", move[1])
                    print_board(board)
    elif(choice==2):
        prune_count = 0
        while (check_winner(board) == 0 and not is_full(board)):
            x = int(input("Enter row (0-2): "))
            y = int(input("Enter column (0-2): "))
            if (x < 0 or x > 2 or y < 0 or y > 2 or board[x][y] != ' '):
                print("Invalid move. Try again.\n")
            else:
                board[x][y] = 'X'
                print("Board after your move:")
                print_board(board)
                if (check_winner(board) != 0 or is_full(board)):
                    break
                move = best_move_alphaBeta(board)
                if (move != (-1, -1)):
                    board[move[0]][move[1]] = 'O'
                    print("Computer's move: Row", move[0], "Column", move[1])
                    print_board(board)

    result = check_winner(board)
    print_board(board)
    if (result == 1):
        print("You win!")
    elif (result == -1):
        print("Computer wins!")
    else:
        print("Draw!")

simulate_game()