from pystockfish import *

class ChessEngine:

    def __init__(self):
        self.Engine = Engine(depth = 19)

    def get_best_move(self, fen):
        self.Engine.setfenposition(fen)
        return self.Engine.bestmove()["move"]
