# ----------- global variable ----------------

current_player = 'X'

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-', ]


# ------ end global variable section ---------

def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def handle_turn():
    global current_player
    pos = input('choose position from 1 to 9 : ')
    pos = int(pos) - 1
    if board[pos] != '-':
        current_player = 'O' if (current_player == 'X') else 'X'
    elif (board[pos] == '-'):
        board[pos] = current_player
    display_board()


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def check_row():
    # print("in row")
    if ((board[0] == board[1] == board[2]) and board[0] != '-'):
        return True
    elif ((board[3] == board[4] == board[5]) and board[3] != '-'):
        return True
    elif ((board[6] == board[7] == board[8]) and board[6] != '-'):
        return True
    else:
        return False


def check_col():
    # print("in col")
    if ((board[0] == board[3] == board[6]) and board[0] != '-'):
        return True
    elif ((board[1] == board[4] == board[7]) and board[1] != '-'):
        return True
    elif ((board[2] == board[5] == board[8]) and board[2] != '-'):
        return True
    else:
        return False


def check_diagonal():
    # print("in dia")
    if ((board[0] == board[4] == board[8]) and board[0] != '-'):
        return True
    elif ((board[2] == board[4] == board[6]) and board[2] != '-'):
        return True
    else:
        return False


def check_if_win():
    # check_row()
    # check_col()
    # check_diagonal()

    if (check_row() or check_col() or check_diagonal()):
        return True
    else:
        return False


def check_if_tie():
    cnt = board.count('-')
    if (cnt == 0):
        return True
    else:
        return False


def check_if_game_over():
    # check if any winner
    # check if game is tie

    if (check_if_win()):
        print('winner is : ' + current_player)
        return True
    elif (check_if_tie()):
        print('game is tie')
        return True
    else:
        return False


def play_game():
    display_board()

    game_still_going = True

    while game_still_going:
        handle_turn()

        if (check_if_game_over()):
            game_still_going = False

        flip_player()


play_game()