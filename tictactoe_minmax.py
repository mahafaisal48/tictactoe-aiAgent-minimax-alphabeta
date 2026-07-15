def check_winner(board):
    for i in range(0,3):
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != ' '):
            if (board[i][0] == 'X'):
                return 1
            else:
                return -1
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != ' '):
            if (board[0][i] == 'X'):
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
            if (board[i][j] == ' '):
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

def best_move(board):
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

def print_board(board):
    print("  0   1   2")
    for i in range(0,3):
        print(i, board[i][0], "|", board[i][1], "|", board[i][2])
        if (i < 2):
            print("  --+---+--")
    print()

def simulate_game():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print_board(board)
    while (check_winner(board) == 0 and not is_full(board)):
        x = int(input("Enter row (0-2): "))
        y = int(input("Enter column (0-2): "))
        
        if (x < 0 or x > 2 or y < 0 or y > 2 or board[x][y] != ' '):
            print("Invalid move. Try again.\n")
        else:
            board[x][y] = 'X'
            print("\nBoard after your move:")
            print_board(board)
            
            if (check_winner(board) != 0 or is_full(board)):
                break
            
            move = best_move(board)
            if (move != (-1, -1)):
                board[move[0]][move[1]] = 'O'
                print("Computer's move: Row", move[0], "Column", move[1])
                print_board(board)
    
    result = check_winner(board)
    if (result == 1):
        print("You win!")
    elif (result == -1):
        print("Computer wins!")
    else:
        print("Draw!")

simulate_game()