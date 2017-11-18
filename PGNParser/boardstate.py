import chess
class BoardState:

    def __init__(self, board):

        self.side_to_move = board.turn
        #Castling Rights
        self.white_long_castle = board.has_queenside_castling_rights(chess.WHITE)
        self.white_short_castle = board.has_kingside_castling_rights(chess.WHITE)
        self.black_long_castle = board.has_queenside_castling_rights(chess.BLACK)
        self.black_short_castle = board.has_kingside_castling_rights(chess.BLACK)

        #Material Counts
        self.white_queens = board.queens
