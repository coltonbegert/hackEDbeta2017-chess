import chess
import numpy
class AttackDefendMap:

    
    def __init__(self, turn):
        self.turn = turn
        self.attack_map = []
        self.defend_map = []
        self.values = dict([(chess.PAWN, 1), 
            (chess.KNIGHT, 3), 
            (chess.BISHOP, 3),
            (chess.ROOK, 6),
            (chess.QUEEN, 9),
            (chess.KING, 200)])

    def push(self, white, black):
        min_white = min(white, key= lambda x: self.values[x[0]]) if len(white) else (None, -1)
        min_black = min(black, key= lambda x: self.values[x[0]]) if len(black) else (None, -1)

        if self.turn:
            self.attack_map.append(min_white[1])
            self.defend_map.append(min_black[1])
        else:
            self.attack_map.append(min_black[1])
            self.defend_map.append(min_white[1])

