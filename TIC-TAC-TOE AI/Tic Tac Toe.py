import math

def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]): return True
        if all([board[j][i] == player for j in range(3)]): return True
    if all([board[i][i] == player for i in range(3)]): return True
    if all([board[i][2-i] == player for i in range(3)]): return True
    return False

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if not get_empty_cells(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (i,j) in get_empty_cells(board):
            board[i][j] = "O"
            score = minimax(board, depth + 1, False)
            board[i][j] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (i,j) in get_empty_cells(board):
            board[i][j] = "X"
            score = minimax(board, depth + 1, True)
            board[i][j] = " "
            best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -math.inf
    move = None
    for (i,j) in get_empty_cells(board):
        board[i][j] = "O"
        score = minimax(board, 0, False)
        board[i][j] = " "
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def play_game():
    board = [[" "]*3 for _ in range(3)]
    print("Player is X. AI is O.")
    print_board(board)

    while True:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] != " ":
            print("Cell occupied. Try again.")
            continue
        board[row][col] = "X"
        print_board(board)

        if check_win(board, "X"):
            print("You win!")
            break
        if not get_empty_cells(board):
            print("It's a draw!")
            break

        print("AI thinking...")
        i, j = get_best_move(board)
        board[i][j] = "O"
        print_board(board)

        if check_win(board, "O"):
            print("AI wins!")
            break
        if not get_empty_cells(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
