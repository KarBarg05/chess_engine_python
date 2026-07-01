from main import get_all_moves 
from main import chess_board
from main import print_board

board = chess_board
turn = "white"

while True:
    print("\n------------------")
    print_board(board)
    print("------------------\n")
    
    moves = get_all_moves(board, turn)

    if not moves:
        print("No hay movimientos")
        break

    move = moves[0]  # always chooses first move

    # apply move
    (r1, c1), (r2, c2) = move
    board[r2][c2] = board[r1][c1]
    board[r1][c1] = "."

    turn = "black" if turn == "white" else "white" # pass turn