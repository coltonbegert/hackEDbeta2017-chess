import chess
from controller.midifighterio import MidiFighterIO

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

board = chess.Board()
mf_io = MidiFighterIO()

while not board.is_game_over():
    # This is our main game loop
    print(board)
    mf_io.send_board_state(board)

    # next_square = mf_io.get_square()
    file_index, rank_index = mf_io.get_square()
    square = chess.square(file_index, rank_index)
    # color = board.piece_at(square).color
    board_piece = board.piece_at(square)
    if board_piece.color == board.turn:
        # possible_attacks = find_attacks(board_piece)
        # for i in get_moves(board, square):
        possible_attacks = get_moves(board, square)
            
        mf_io.send_piece_selected(next_piece['coords'], possible_attacks)

        next_file, next_rank = mf_io.get_square()
        next_attack = chess.square(next_file,next_rank)
        if next_attack in possible_attacks:
            play_move(board, move(board, square, next_attack))
