class MIDIBoard():
    def __init__(self):
        self._board = [[['00', '00', '00'] for i in range(8)] for i in range(8)]

    def set(self, coords, value):
        self._board[coords[0]][coords[1]] = value

    def get(self, coords):
        return self._board[coords[0]][coords[1]]
