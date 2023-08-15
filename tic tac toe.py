def print_board(board):
    print('-------------')
    for row in board:
        print('|', end='')
        for val in row:
            print(' ' + val + ' |', end='')
        print('\n-------------')

def is_valid_move(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row][col] != ' ':
        return False
    return True

def has_won(board, player):
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def play():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input(f"{current_player}, enter row (0-2): "))
        col = int(input(f"{current_player}, enter col (0-2): "))

        if not is_valid_move(board, row, col):
            print("Invalid move, try again!")
            continue

        board[row][col] = current_player

        if has_won(board, current_player):
            print_board(board)
            print(f"{current_player} has won!")
            return

        if all([val != ' ' for row in board for val in row]):
            print_board(board)
            print("It's a tie!")
            return

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    play()