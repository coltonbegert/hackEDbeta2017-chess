import pystockfish
from pystockfish import Engine

class ChessEngine:

    def __init__(self):
        self.Engine = Engine(depth = 19)



    def get_best_move(self, fen):
        self.Engine.setfenposition(fen)
        return self.Engine.bestmove()["move"]

def best_move(self):
    last_line = ""
    self.go()
    while True:
        text = self.stdout.readline().strip()
        split_text = text.split(' ')
        if split_text[0] == 'bestmove':
            return {'move': split_text[1],
                    'ponder': None,
                    'info': last_line
            }
        last_line = text

pystockfish.Engine.bestmove = best_move
