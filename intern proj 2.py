def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    win_conditions = (
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    )
    return [player, player, player] in win_conditions

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_move(player):
    while True:
        try:
            row = int(input(f"{player}, enter the row (1, 2, 3): ")) - 1
            col = int(input(f"{player}, enter the column (1, 2, 3): ")) - 1
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def play_game():
    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"
        game_over = False
        
        while not game_over:
            print_board(board)
            row, col = get_move(current_player)
            
            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    game_over = True
                elif is_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    game_over = True
                else:
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("This position is already taken. Try again.")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
