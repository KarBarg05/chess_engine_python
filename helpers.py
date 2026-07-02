chess_board = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"]
]


def empty_board():
    return [["." for _ in range(8)] for _ in range(8)]

# square[row][col]
def inbounds(square):
    return ((0 <= square[0] <= 7) and (0 <= square[1] <= 7))

def get_piece(board, square):
    return board[square[0]][square[1]]

def empty_square(board, square):
    return get_piece(board, square) == "."

def is_white(board, square):
    return get_piece(board, square).isupper()

def is_black(board, square):
    return get_piece(board, square).islower()

def is_opp(board, s1, s2): 
    p1 = get_piece(board, s1)
    p2 = get_piece(board, s2)

    return (is_white(p1) and is_black(p2)) or (is_black(p1) and is_white(p2))

def is_ours(board, s1, s2):
    p1 = get_piece(board, s1)
    p2 = get_piece(board, s2)
    
    return (is_white(p1) and is_white(p2)) or (is_black(p1) and is_black(p2))

straight_dirs = {
    "up":      (-1, 0),
    "right":    (0, 1),
    "down":     (1, 0),
    "left":     (0, -1)
}

diagonal_dirs = {
    "upright":     (-1, 1),
    "downright":    (1, 1),
    "downleft":    (1, -1),
    "upleft":      (-1, -1)
}

# sums position with direction tuple
def sliding_sum(square, dir):
    combined = zip(square, dir)
    new_square = tuple(map(sum, combined))

    return new_square

# función para comprobar jaques
        # y/o movimientos ilegales