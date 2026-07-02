from pieces import piece_moves
from helpers import chess_board
from helpers import get_piece
from helpers import empty_square
from helpers import is_white
from helpers import is_black
from helpers import is_opp


class Board:
    def __init__(self):
        self.board = chess_board
        self.game_notation = []     # table
        self.turn_count = 0
        self.color = True           # True as White and False as Black

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def register_move(self, move, take_bool):
        origin_square = move[0]
        destination_square = move[1]
        origin_piece = get_piece(self.board, origin_square)

        piece = {
            "p": "",
            "n": "N",
            "r": "R",
            "k": "K",
            "b": "B",
            "q": "Q"
        }
        column = {
            0: "a",
            1: "b",
            2: "c",
            3: "d",
            4: "e",
            5: "f",
            6: "g",
            7: "h"
        }

        if origin_piece.lower() == "p":
            if take_bool:
                ini_str = column[origin_square[0]]
            else:
                ini_str = ""
        else:
            ini_str = piece[origin_piece[0]]
        
        take_str = "x" if take_bool else ""

        # faltan enroques, checks, checkmate y
            # comprobar si varias piezas iguales pueden moverse a la misma casilla

        move_str = ini_str + take_str + column[destination_square[0]] + str(destination_square[1])

        # move register "matrix"
        if self.color:
            self.turn_count += 1
            self.game_notation.append([])
        self.game_notation[(self.turn_count) - 1].append(move_str)
        self.color = not self.color

        return

    def move_piece(self, move):
        origin_piece = get_piece(move[0])
        destination_piece = get_piece(move[1])

        # for the register of the move in the game
        is_taking = True if is_opp(origin_piece, destination_piece) else False
        self.register_move(self, move, is_taking)
        
        destination_piece = origin_piece
        origin_piece = "."

        return

    def get_all_moves(self):
        moves = []

        for row in range(len(chess_board)):
            for col in range(len(chess_board[0])):
                moves = []
                square = (row, col)
                piece = get_piece(self.board, square)

                if empty_square(self.board, square):
                    continue

                # only white can move their own pieces, and same for black
                if (self.color == True and is_white(self.board, square)) or (self.color == False and is_black(self.board, square)):
                    get_moves = piece_moves[piece.lower()]
                    for move in get_moves(self.board, row, col):
                        moves.append((square, move))    # origin + end squares

        return moves