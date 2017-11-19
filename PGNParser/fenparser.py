import chess

class FenParser:

    NORTH = 0
    NORTHWEST = 1
    WEST = 2
    SOUTHWEST = 3
    SOUTH = 4
    SOUTHEAST = 5
    EAST = 6
    NORTHEAST = 7

    pieces = {'p': chess.PAWN, 'r': chess.ROOK, 'b': chess.BISHOP, 'n': chess.KNIGHT, 'q': chess.QUEEN, 'k': chess.KING}
    def __init__(self, fen):
        self.fen = fen

    def get_piece_at_square(self, square):
        row_index = square // 8
        col_index = square - 8 * row_index

        #part[0] is the board representation
        row = self.fen.split()[0].split("/")[7 - row_index]
        piece = ""
        for c in row:
            if col_index <= 0:
                piece = c.lower()
                break
            if c.isdigit():
                col_index -= int(c)
            else:
                col_index -= 1

        return FenParser.pieces[piece]

        
            



