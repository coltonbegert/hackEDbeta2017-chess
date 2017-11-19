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
        if game is None:
            raise ValueError("End of file")
        board = game.board()

        if len(list(game.main_line())) <= 1:
            return None

        stop = randint(1, len(list(game.main_line())))
        node = game
        while stop != 0:
            stop -= 1
            next_node = node.variations[0]

            if next_node.comment.find("eval") == -1:
                return None
            board.push(next_node.move)
            node = next_node

        state_evaluation = float(node.comment.split(']')[0].replace('[%eval ', '').replace("#", ""))

        return BoardState(board, state_evaluation)

