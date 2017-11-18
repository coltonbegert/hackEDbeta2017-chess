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
        self.set_material_values(board)


    def set_material_values(self, board):
        white_queen = board.pieces(chess.QUEEN, chess.WHITE)
        white_king = board.pieces(chess.KING, chess.WHITE)
        white_rooks = board.pieces(chess.ROOK, chess.WHITE)
        white_bishops = board.pieces(chess.BISHOP, chess.WHITE)
        white_knights = board.pieces(chess.KNIGHT, chess.WHITE)
        white_pawns = board.pieces(chess.PAWN, chess.WHITE)

        black_queen = board.pieces(chess.QUEEN, chess.BLACK)
        black_king = board.pieces(chess.KING, chess.BLACK)
        black_rooks = board.pieces(chess.ROOK, chess.BLACK)
        black_bishops = board.pieces(chess.BISHOP, chess.BLACK)
        black_knights = board.pieces(chess.KNIGHT, chess.BLACK)
        black_pawns = board.pieces(chess.PAWN, chess.BLACK)
        
        #Material Counts
        self.white_queen_count = len(white_queen)
        self.white_rook_count = len(white_rooks)
        self.white_bishops_count = len(white_bishops)
        self.white_knight_count = len(white_knights)
        self.white_pawn_count = len(white_pawns)

        self.black_queen_count = len(black_queen)
        self.black_rook_count = len(black_rooks)
        self.black_bishops_count = len(black_bishops)
        self.black_knight_count = len(black_knights)
        self.black_pawn_count = len(black_pawns)

