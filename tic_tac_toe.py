import random

PLAYER = 'X'
COMPUTER = 'O'
EMPTY = ' '


def print_board(board):
    for row in board:
        print('|'.join(row))
    print()


def check_winner(board, player):
    lines = []
    lines.extend(board)  # rows
    lines.extend([[board[r][c] for r in range(3)] for c in range(3)])  # cols
    lines.append([board[i][i] for i in range(3)])  # diag
    lines.append([board[i][2 - i] for i in range(3)])  # anti diag
    return any(all(cell == player for cell in line) for line in lines)


def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == EMPTY]


def minimax(board, player, depth=0):
    if check_winner(board, PLAYER):
        return -10 + depth, None
    if check_winner(board, COMPUTER):
        return 10 - depth, None
    moves = get_available_moves(board)
    if not moves:
        return 0, None

    if player == COMPUTER:
        best_score = float('-inf')
        best_move = None
        for move in moves:
            r, c = move
            board[r][c] = COMPUTER
            score, _ = minimax(board, PLAYER, depth + 1)
            board[r][c] = EMPTY
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for move in moves:
            r, c = move
            board[r][c] = PLAYER
            score, _ = minimax(board, COMPUTER, depth + 1)
            board[r][c] = EMPTY
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move


def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    current = PLAYER

    while True:
        print_board(board)
        if current == PLAYER:
            try:
                move = input('Enter move as row,col (0-2): ')
                r, c = map(int, move.split(','))
            except Exception:
                print('Invalid input')
                continue
            if (r not in range(3)) or (c not in range(3)) or board[r][c] != EMPTY:
                print('Invalid move')
                continue
        else:
            _, move = minimax(board, COMPUTER)
            r, c = move
            print(f'Computer chooses {r},{c}')

        board[r][c] = current

        if check_winner(board, current):
            print_board(board)
            print(f'{current} wins!')
            return
        if not get_available_moves(board):
            print_board(board)
            print('It\'s a tie!')
            return
        current = COMPUTER if current == PLAYER else PLAYER


if __name__ == '__main__':
    play_game()
