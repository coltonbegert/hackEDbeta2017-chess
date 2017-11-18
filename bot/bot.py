import chess

board = chess.Board()


class State():
    def __init__(self, board=None, move=None):
        self.board = board
        self.score = None
        self.move = move
        self.child_moves = []

        
    def is_game_over(self):
        if self.board is not None:
            return self.board.is_game_over()
        return False

    '''
    use NN to get state score
    '''
    def update_score(self):
        # TODO implement network for state evaluation
        # self.score = -1
        self.score=bad_evaluation(self.board.fen().split()[0])
        return False

    '''
    returns the games score if calculated and if not calculates the score for the surrent state
    '''
    def get_score(self):
        if self.score is not None:
            return self.score
        self.update_score()
        return self.score

    '''
    Copy the current board, apply the next move and create a new state which contains this.
    '''
    def make_move(self, move):
        new_board = self.board.copy()
        new_board.move(move)
        new_state = State(new_board, move)
        self.child_moves.append(new_state)

    '''
    use python-chess to generate all legal moves and branch the search tree for these new states
    '''
    def gen_children(self):
        for i in self.board.legal_moves:
            self.make_move(i)

    def get_best_move(self):
        max_score = 0
        max_move = None
        for i in self.child_moves:
            if self.child_moves[i].get_score() > max_score:
                max_score = self.child_moves[i].get_score()
                max_move = i
        return self.child_moves[max_move]

def play():
    root = State(board=chess.Board())
    print(root.get_best_move())



def bad_evaluation(fen):
    b_pieces = "rnbqp"
    w_pieces = "RNBQP"
    vals = [5, 3, 3, 9, 1]
    score = 0
    for i in range(5):
        score += fen.count(b_pieces[i]) * vals[i]
        score -= fen.count(w_pieces[i]) * vals[i]
    return score

c = 0
while not board.is_game_over():
    c += 1
    # print(c)
    for i in board.legal_moves:
        move = i
    # print(move)
    board.push(move)
    f = board.fen().split()[0]

    # print(f.count('r'), f.count('n'), f.count('b'), f.count('q'), f.count('k'), f.count('p'), f.count('R'), f.count('N'), f.count('B'), f.count('Q'), f.count('K'), f.count('P'))
    print(board)
    print(bad_evaluation(f))


    # print(board.is_game_over())

print("moves: ",c)


