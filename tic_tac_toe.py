# https://github.com/visheshdvivedi/Top-10-Easy-Python-Project-Ideas-For-Beginners/blob/main/tic_tac_toe.py

board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
X = 'X'
O = 'O'

def display_board():
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(f"-----------")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(f"-----------")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]}")


def update_board(character, position):
    row = (position - 1) // 3
    column = (position - 1) % 3
    board[row][column] = character


def check_win():
    for i in range(3):
        # Horizontal check
        if board[i][0] == board[i][1] == board[i][2]:
            return True
        elif board[0][i] == board[1][i] == board[2][i]:
            return True
    # Cross check
    if board[0][2] == board[1][1] == board[2][0]:
        return True
    elif board[0][0] == board[1][1] == board[2][2]:
        return True
    # Nothing found
    return False


def check_position(position):
    row = (position - 1) // 3
    column = (position - 1) % 3
    if board[row][column] == X or board[row][column] == O:
        return False
    return True


print(f"==== Welcome to Tic Tac Toe Game ====")
counter = 0
while True:
    if counter % 2 == 0:
        display_board()
        while True:
            choice = int(input(f"Player {(counter % 2) + 1}, enter your position ('{X}'): "))
            if choice not in range(1, 10):
                print(f"Invalid input... Please try again!")
                continue
            if check_position(choice):
                update_board(X, choice)
                if check_win():
                    print(f"Congratulations!!! Player {(counter % 2) + 1} won!!!")
                    exit(0)
                else:
                    counter += 1
                    break
            else:
                print(f"Position {choice} is already occupied. Choose another position")
        if counter == 9:
            print(f"The match ended with a draw!!! Better luck next time")
            exit(0)
    else:
        display_board()
        while True:
            choice = int(input(f"Player {(counter % 2) + 1}, enter your position ('{O}'): "))
            if choice not in range(1, 10):
                print(f"Invalid input... Please try again!")
                continue
            if check_position(choice):
                update_board(O, choice)
                if check_win():
                    print(f"Congratulations!!! Player {(counter % 2) + 1} won!!!")
                    exit(0)
                else:
                    counter += 1
                    break
            else:
                print(f"Position {choice} is already occupied. Choose another position.")
    print()

