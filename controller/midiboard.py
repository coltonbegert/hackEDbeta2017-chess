class MIDIBoard():
    def __init__(self):
        self._board = [[['00', '00', '00'] for i in range(8)] for i in range(8)]

    def _get_coords(self, coord):
        if isinstance(coord, list) or isinstance(coord, tuple):
            return coord
        return (coord//8, coord%8)

    def set(self, pos, value):
        coords = self._get_coords(pos)
        self._board[coords[0]][coords[1]] = value

    def get(self, pos):
        coords = self._get_coords(pos)
        return self._board[coords[0]][coords[1]]
