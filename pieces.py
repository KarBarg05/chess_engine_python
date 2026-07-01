from helpers import inbounds
from helpers import square_to_piece
from helpers import empty_square
from helpers import is_opp
from helpers import is_ours
from helpers import straight_dirs
from helpers import diagonal_dirs
from helpers import sliding_sum


def get_pawn_moves(board, row, col): 
    moves = []
    current_square = (row, col)
    current_piece = square_to_piece(board, current_square)
    
    if current_piece == "P": # white pawn
        adv_square = sliding_sum(current_square, straight_dirs["up"])

        if inbounds(adv_square) and empty_square(board, adv_square):
            moves.append(adv_square)

            if row == 6 and empty_square(board, (row - 2, col)): # initial "double move"
                moves.append((row - 2, col))
        
        # capturable pieces
        capture_dirs = [diagonal_dirs["upright"], diagonal_dirs["upleft"]]

        for dir in capture_dirs:
            capture_square = sliding_sum(current_square, dir)
            if not inbounds(capture_square):
                continue

            capture_piece = square_to_piece(board, capture_square)
            if capture_piece == "k":
                continue

            if is_opp(current_piece, capture_piece):
                moves.append(capture_square)


    elif current_piece == "p": # black pawn
        adv_square = sliding_sum(current_square, straight_dirs["down"])
        
        if inbounds(adv_square) and empty_square(board, adv_square):
            moves.append(adv_square)

            if row == 1 and empty_square(board, (row + 2, col)): # initial "double move"
                moves.append((row + 2, col))
        
        # capturable pieces
        capture_dirs = [diagonal_dirs["downright"], diagonal_dirs["downleft"]]

        for dir in capture_dirs:
            capture_square = sliding_sum(current_square, dir)
            if not inbounds(capture_square):
                continue

            capture_piece = square_to_piece(board, capture_square)
            if capture_piece == "K":
                continue

            if is_opp(current_piece, capture_piece):
                moves.append(capture_square)


    return moves
    
def get_knight_moves(board, row, col): 
    moves = []
    square = (row, col)
    piece = square_to_piece(board, square)
    
    possible_moves = ((row - 2, col - 1),
                      (row - 2, col + 1),
                      (row - 1, col + 2),
                      (row + 1, col + 2),
                      (row + 2, col + 1),
                      (row + 2, col - 1),
                      (row + 1, col - 2),
                      (row - 1, col - 2))
    
    for move in possible_moves:    # if move's legal
        capture_square = sliding_sum(square, move)
        if not inbounds(capture_square):
            continue

        capture_piece = square_to_piece(board, capture_square)
        if capture_piece.lower() == "k":
            continue
        
        if not is_ours(piece, capture_piece):
            moves.append(move)

    return moves

def get_sliding_moves(board, row, col, dirs):
    moves = []
    current_piece = square_to_piece(board, (row, col))
  
    for dir in dirs:
        current_square = (row, col)

        next_square = sliding_sum(current_square, dir)
        next_piece = square_to_piece(board, next_square)
        if next_piece.lower() == "k":
            break

        while inbounds(next_square) and (is_opp(current_piece, next_piece) or empty_square(board, next_square)):
            moves.append(next_square)

            if empty_square(board, next_square):
                current_square = next_square
                next_square = sliding_sum(current_square, dir)
            else:   # captura de pieza
                break

    return moves

def get_rook_moves(board, row, col):
    return get_sliding_moves(board, row, col, list(straight_dirs.values))

def get_bishop_moves(board, row, col):
    return get_sliding_moves(board, row, col, list(diagonal_dirs.values))

def get_queen_moves(board, row, col):
    return get_sliding_moves(board, row, col, list(straight_dirs.values) + list(diagonal_dirs.values))

def get_king_moves(board, row, col):
    moves = []
    current_square = (row, col)
    current_piece = square_to_piece(board, current_square)
    dirs = list(straight_dirs.values) + list(diagonal_dirs.values)

    # normal moves
    for dir in dirs:
        next_square = sliding_sum(current_square, dir)
        next_piece = square_to_piece(board, next_square)
        if next_piece.lower() == "k":
            continue
        
        if inbounds(next_square) and (is_opp(current_piece, next_piece) or empty_square(board, next_square)):
            moves.append(next_square)
        
    # enroque???

    return moves

piece_moves = {
    "p": get_pawn_moves,
    "n": get_knight_moves,
    "r": get_rook_moves,
    "k": get_king_moves,
    "b": get_bishop_moves,
    "q": get_queen_moves
}