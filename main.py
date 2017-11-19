import chess
import time
import threading
from chessengine import ChessEngine
# from controller.midifighterio import MidiFighterIO

class Game(threading.Thread):
    def __init__(self, board=chess.Board()):
        threading.Thread.__init__(self)
        self.board = board
        self.engine = ChessEngine()
    def run(self):
        while not self.board.is_game_over():
           time.sleep(0.1)

    def get_board(self):
        return self.board

    def get_moves(self, source):
        moves = []
        for move in self.board.legal_moves:
            # move = chess.Move()
            if move.from_square == source:
                moves.append(move.to_square)
        return moves
    
    def print_update(self):
        print(self.board)

    def get_engine_update(self):
        move = self.engine.get_best_move(self.board.fen())
        self.board.push_uci(move)
        print(move)
        self.print_update()

    def play_move(self, move):
        self.board.push(move)
        self.print_update()
        self.get_engine_update()
        

    def move(self, source, dest):
        for move in self.board.legal_moves:
            if move.from_square == source and move.to_square == dest:
                return move

    def press_query(self, file_index, rank_index):
        square = chess.square(file_index, rank_index)
        # color = board.piece_at(square).color
        board_piece = self.board.piece_at(square)
        if board_piece.color == self.board.turn:
            # possible_attacks = find_attacks(board_piece)
            # for i in get_moves(board, square):
            possible_attacks = get_moves(self.board, square)
            return [(chess.square_file(s), chess.square_rank(s)) for s in possible_attacks ]

    def press_confirm(self, from_file, from_rank, to_file, to_rank):
        square = chess.square(from_file, from_rank)
        next_attack = chess.square(to_file, to_rank)
        if next_attack in self.get_moves(square):
            self.play_move(chess.Move(square, next_attack))
    
        

def get_state():
    pass

def update():
    pass

def find_attacks(board, filei, ranki):
    return board.attacks(chess.square(filei, ranki))

def get_moves(board, source):
    moves = []
    for move in board.legal_moves:
        # move = chess.Move()
        if move.from_square == source:
            moves.append(move.to_square)
    return moves

def play_move(board, move):
    board.push(move)
    return

def move(board, source, dest):
    for move in board.legal_moves:
        if move.from_square == source and move.to_square == dest:
            return move
def main():
    game = Game()
    game.start()
    game.print_update()
    print(game.press_query(1,1))
    game.press_confirm(1,1,1,2)


if __name__ == '__main__':
    main()
# board = chess.Board()
# mf_io = MidiFighterIO()

# while not board.is_game_over():
#     # This is our main game loop
#     print(board)
#     mf_io.send_board_state(board)

#     # next_square = mf_io.get_square()
#     file_index, rank_index = mf_io.get_square()
#     square = chess.square(file_index, rank_index)
#     # color = board.piece_at(square).color
#     board_piece = board.piece_at(square)
#     if board_piece.color == board.turn:
#         # possible_attacks = find_attacks(board_piece)
#         # for i in get_moves(board, square):
#         possible_attacks = get_moves(board, square)
            
#         mf_io.send_piece_selected(next_piece['coords'], possible_attacks)

#         next_file, next_rank = mf_io.get_square()
#         next_attack = chess.square(next_file,next_rank)
#         if next_attack in possible_attacks:
#             play_move(board, move(board, square, next_attack))
