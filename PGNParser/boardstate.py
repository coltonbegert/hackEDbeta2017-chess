import chess
from attdefmap import AttackDefendMap
from fenparser import FenParser

class BoardState:

    def __init__(self, board, state_evaluation):

        self.stockfish_evaluation = state_evaluation
        self.side_to_move = board.turn
        #Castling Rights
        self.white_long_castle = board.has_queenside_castling_rights(chess.WHITE)
        self.white_short_castle = board.has_kingside_castling_rights(chess.WHITE)
        self.black_long_castle = board.has_queenside_castling_rights(chess.BLACK)
        self.black_short_castle = board.has_kingside_castling_rights(chess.BLACK)

        #Material Counts
        self.set_material_values(board)

        self.set_attack_defend_maps(board)


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
        self.white_king_count = len(white_king)
        self.white_queen_count = len(white_queen)
        self.white_rook_count = len(white_rooks)
        self.white_bishops_count = len(white_bishops)
        self.white_knight_count = len(white_knights)
        self.white_pawn_count = len(white_pawns)

        self.black_king_count = len(black_king)
        self.black_queen_count = len(black_queen)
        self.black_rook_count = len(black_rooks)
        self.black_bishops_count = len(black_bishops)
        self.black_knight_count = len(black_knights)
        self.black_pawn_count = len(black_pawns)

        #Material locations
        self.white_pawns = list(map(lambda x: x, white_pawns))
        while(len(self.white_pawns) < 8):
            self.white_pawns.append(0)

        self.white_rooks = list(map(lambda x: x, white_rooks))
        while(len(self.white_rooks) < 2):
            self.white_rooks.append(0)

        self.white_bishops = list(map(lambda x: x, white_bishops))
        while(len(self.white_bishops) < 2):
            self.white_bishops.append(0)

        self.white_knights = list(map(lambda x: x, white_knights))
        while(len(self.white_knights) < 2):
            self.white_knights.append(0)

        self.white_queen = list(map(lambda x: x, white_queen))
        while(len(self.white_queen) < 1):
            self.white_queen.append(0)

        self.white_king = list(map(lambda x: x, white_king))
        while(len(self.white_king) < 1):
            self.white_king.append(0)


        self.black_pawns = list(map(lambda x: x, black_pawns))
        while(len(self.black_pawns) < 8):
            self.black_pawns.append(0)

        self.black_rooks = list(map(lambda x: x, black_rooks))
        while(len(self.black_rooks) < 2):
            self.black_rooks.append(0)

        self.black_bishops = list(map(lambda x: x, black_bishops))
        while(len(self.black_bishops) < 2):
            self.black_bishops.append(0)

        self.black_knights = list(map(lambda x: x, black_knights))
        while(len(self.black_knights) < 2):
            self.black_knights.append(0)

        self.black_queen = list(map(lambda x: x, black_queen))
        while(len(self.black_queen) < 1):
            self.black_queen.append(0)

        self.black_king = list(map(lambda x: x, black_king))
        while(len(self.black_king) < 1):
            self.black_king.append(0)


    def set_attack_defend_maps(self, board):
        self.attack_defend_map = AttackDefendMap(board.turn)

        for x in range(0, 63):
            white_positions = board.attackers(chess.WHITE, x)
            black_positions = board.attackers(chess.BLACK, x)
            fen_parser = FenParser(board.fen())
            white_pieces = [(fen_parser.get_piece_at_square(i), i) for i in white_positions]
            black_pieces = [(fen_parser.get_piece_at_square(i), i) for i in black_positions]

            self.attack_defend_map.push(white_pieces, black_pieces)

    def __repr__(self):
        item_list = []
        item_list.append(self.side_to_move)
        item_list.append(self.white_long_castle) 
        item_list.append(self.white_short_castle)
        item_list.append(self.black_long_castle) 
        item_list.append(self.black_short_castle)
        item_list.append(self.white_king_count) 
        item_list.append(self.white_queen_count)
        item_list.append(self.white_bishops_count)
        item_list.append(self.white_knight_count) 
        item_list.append(self.white_pawn_count) 
        item_list.append(self.black_king_count) 
        item_list.append(self.black_queen_count) 
        item_list.append(self.black_bishops_count)
        item_list.append(self.black_knight_count) 
        item_list.append(self.black_pawn_count) 
        item_list += self.white_pawns
        item_list += self.white_rooks
        item_list += self.white_bishops
        item_list += self.white_knights
        item_list += self.white_queen
        item_list += self.white_king
        item_list += self.black_pawns
        item_list += self.black_rooks
        item_list += self.black_bishops
        item_list += self.black_knights
        item_list += self.black_queen
        item_list += self.black_king
        item_list += self.attack_defend_map.toList()
        return ','.join(str(x) for x in item_list) 

