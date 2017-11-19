import chess
from controller.midifighterio import MidiFighterIO

def get_state():
    pass

def update():
    pass

def find_attacks(piece):
    pass

def play_move():
    pass

board = chess.Board()
mf_io = MidiFighterIO()

while not board.is_game_over():
    # This is our main game loop
    print(board)
    mf_io.send_board_state(board)

    next_square = mf_io.get_square()
    board_piece = board.piece_at(chess.square(next_square))
    if board_piece.color == board.turn:
        possible_attacks = find_attacks(board_piece)
        mf_io.send_piece_selected(next_piece['coords'], possible_attacks)

        next_attack = mf_io.get_square()
        if next_attack in possible_attacks:
            play_move(next_attack)
