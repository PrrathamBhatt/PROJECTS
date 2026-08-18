import math

board = [" " for _ in range(9)]


def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def board_full():
    return " " not in board


def minimax(is_maximizing):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(False)

                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(True)

                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def computer_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


def player_move():
    while True:
        try:
            position = int(input("Choose a position (1-9): "))

            if position < 1 or position > 9:
                print("Choose a number from 1 to 9.")
                continue

            position -= 1

            if board[position] != " ":
                print("That position is already taken.")
                continue

            board[position] = "X"
            break

        except ValueError:
            print("Please enter a number.")


print("===== TIC-TAC-TOE =====")
print("You are X")
print("Computer is O")

while True:

    print_board()

    player_move()

    if check_winner("X"):
        print_board()
        print("🎉 You win!")
        break

    if board_full():
        print_board()
        print("It's a draw!")
        break

    computer_move()

    if check_winner("O"):
        print_board()
        print("🤖 Computer wins!")
        break
