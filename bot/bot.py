import chess
import numpy as np
import profile

board = chess.Board()


class State():
    def __init__(self, board=None, move=None, depth=0):
        self.board = board
        self.score = None
        self.move = move
        self.child_moves = []
        self.depth = depth
        self.best_child = None

        
    def is_game_over(self):
        if self.board is not None:
            return self.board.is_game_over()
        return False

    '''
    use NN to get state score
    '''
    def update_score(self):
        # TODO implement network for state evaluation
        self.score = -1
        # f = self.board.fen().split()[0]
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
        new_board.push(move)
        # print(new_board)
        new_state = State(new_board, move, self.depth - 1)
        new_state.update_score()
        self.child_moves.append(new_state)

    '''
    use python-chess to generate all legal moves and branch the search tree for these new states
    '''
    def gen_children(self):
        # for i in self.board.pseudo_legal_moves:
        self.children = []
        if len(self.child_moves) == 0:
            for i in self.board.legal_moves:
                self.make_move(i)


    def order_children(self):
        # TODO order the children by the predicted best score
        pass

    def get_best_move(self):
        max_score = 0
        max_move = 1
        self.gen_children()
        for i in range(len(self.child_moves)):
            if self.child_moves[i].get_score() > max_score:
                max_score = self.child_moves[i].get_score()
                max_move = i
        return self.child_moves[max_move]
global c
c = 0
def alpha_beta(state, depth, alpha, beta):
    global c
    c += 1
    # print("hello", depth)
    if depth == 0 or state.is_game_over():
        return float(state.get_score())
    state.gen_children()
    state.order_children()
    best_score = -np.inf
    for s in state.child_moves:
        value = -alpha_beta(s, depth - 1, -beta, -alpha)
        s.score = value
        best_score = np.maximum(value, best_score)
        alpha = np.maximum(alpha, value)
        if alpha >= beta:
            # print("here")
            break
    state.best_child = best_score
    return best_score

    


def play():
    
    root = State(board=chess.Board(), depth=4)
    while not root.is_game_over():
        # print()
        score = alpha_beta(root, 4, -np.inf, np.inf)
        # print(root.board.fen(), root)
        for i in root.child_moves:
            # print("hello")
            if i.score == score:
                # print(root.board)

                root = State(board=i.board.copy())
                # print(i.board)
                # print(root.board)
                # print("score: ", score, root.board.fen())
                break
        # print(len(root.child_moves))
        print(root.board, "\n")

    print(score)



def bad_evaluation(fen):
    w_pieces = "RNBQPK"
    b_pieces = "rnbqpk"
    vals = [5, 3, 3, 9, 1,200]
    score = 0
    for i in range(6):
        score += fen.count(w_pieces[i]) * vals[i]
        score -= fen.count(b_pieces[i]) * vals[i]
    return score

# profile.run('play()')
play()
print (c)
# c = 0
# while not board.is_game_over():
#     c += 1
#     # print(c)
#     for i in board.legal_moves:
#         move = i
#     # print(move)
#     board.push(move)
#     f = board.fen().split()[0]

#     # print(f.count('r'), f.count('n'), f.count('b'), f.count('q'), f.count('k'), f.count('p'), f.count('R'), f.count('N'), f.count('B'), f.count('Q'), f.count('K'), f.count('P'))
#     print(board)
#     print(bad_evaluation(f))

#     # print(board.is_game_over())

# print("moves: ",c)


