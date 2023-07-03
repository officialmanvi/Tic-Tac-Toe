# Creating the board
board = [' ' for _ in range(9)]

# Define the winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]


def print_board():
    # Print the current board
    print("-------------")
    for i in range(3):
        print("|", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2], "|")
        print("-------------")


def check_winner(player):
    # Check if the player has won
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False


def is_board_full():
    # Check if the board is full
    return all(cell != ' ' for cell in board)


def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()
        print("Player", current_player, "turn.")

        position = int(input("Enter a position (1-9): ")) - 1

        if board[position] == ' ':
            board[position] = current_player

            if check_winner(current_player):
                print_board()
                print("Player", current_player, "wins!")
                game_over = True
            elif is_board_full():
                print_board()
                print("It's a tie!")
                game_over = True
            else:
                # Switch players
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")


play_game()