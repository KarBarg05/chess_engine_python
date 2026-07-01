'''
                                                TESTEO I
                                           (06/05/2026 01:16)

                                    Just finished "get_pawn_moves()"
                                Pawns can move forward, move 2 squares from
                               the start, and take pieces on their diagonals.
                                              No En Passant
                                              No Promoting
                             "get_pawn_moves" only shows possible next squares,
                                            no initial square.
'''

from main import get_pawn_moves

# INITIAL MOVEMENT
board = [["." for _ in range(8)] for _ in range(8)]
board[6][3] = "P"  # white pawn

assert set(get_pawn_moves(board, 6, 3)) == set([(5, 3), (4, 3)])


# BLOCKING PIECE
board[5][3] = "p"

assert get_pawn_moves(board, 5, 3) == [] # testing black pawn too


# CAPTURE
board = [["." for _ in range(8)] for _ in range(8)]
board[6][3] = "P"
board[5][2] = "p"
board[5][4] = "p"

assert set(get_pawn_moves(board, 6, 3)) == set([(5, 3), (4, 3), (5, 2), (5, 4)])


# BORDERS
board = [["." for _ in range(8)] for _ in range(8)]
board[6][0] = "P"
board[0][0] = "P"

assert set(get_pawn_moves(board, 6, 0)) == set([(5, 0), (4, 0)])
assert get_pawn_moves(board, 0, 0) == []


print("\nTEST I: ALL GOOD")


'''
                                                TESTEO II
                                            (07/05/2026 10:14)

                                     Just finished "get_knight_moves()"
                                        Knights have full movility
                                Helper functions "inbounds()" and "empty_board()"
                           "get_all_moves()" used in playtesting, now includes knights
'''

from main import get_knight_moves
from helpers import empty_board

# FULL MOVEMENT
board = empty_board()
board[4][4] = "N"  # white knight

assert set(get_knight_moves(board, 4, 4)) == set([(2, 3), (2, 5), (3, 6), (5, 6), (6, 5), (6, 3), (5, 2), (3, 2)])


# MOVEMENT FROM CORNERS
board = empty_board()
board[0][0] = "n"  # testing black knight too

assert set(get_knight_moves(board, 0, 0)) == set([(1, 2), (2, 1)])


# CAPTURE
board = empty_board()
board[3][3] = "N"
board[5][2] = "p"
board[5][4] = "P"
board[4][1] = "P"
board[2][5] = "p"

assert set(get_knight_moves(board, 3, 3)) == set([(1, 2), (1, 4), (2, 5), (4, 5), (5, 2), (2, 1)])


print("\nTEST II: ALL GOOD")