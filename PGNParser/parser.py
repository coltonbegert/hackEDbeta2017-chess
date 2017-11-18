import chess.pgn
from random import randint
from boardstate import BoardState

class PGNParser:

    def __init__(self, file):
        self.pgn = open(file)

    def parse_next_game(self):
        """
        IT'S A DOCSTRING NOW
        """
        game = chess.pgn.read_game(self.pgn)
        board = game.board()
    
        #Select a random game state
        stop = randint(1, len(list(game.main_line())))
        for idx, move in enumerate(game.main_line()):
            if(idx == stop):
                break
            board.push(move)

        return BoardState(board)

