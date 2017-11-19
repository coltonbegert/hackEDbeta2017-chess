import mido
from queue import Queue

from .midiboard import MIDIBoard
from .constants import *

class MidiFighterIO():
    def __init__(self):
        self.board = MIDIBoard()
        self.input = mido.open_input('Midi Fighter 64')
        self.output = mido.open_output('Midi Fighter 64')
        # self.draw_queue = Queue()

    def square_to_coords(self, coord):
        if isinstance(coord, list) or isinstance(coord, tuple):
            return coord
        return (7-(coord//8), coord%8)

    def get_button_press(self):
        # flush
        list(self.input.iter_pending())

        button_data = self.input.receive()
        while not button_data.hex().startswith(MIDI_NOTE_OFF):
            button_data = self.input.receive()
        return button_data.hex().split()[1]

    def get_square(self):
        button_byte = self.get_button_press()
        return self.square_to_coords(BOARD_BYTE_TO_COORDS[button_byte])

    def build_msg_block(self, lines, half='01'):
        # lines is 8 lines long, please
        # half is '01' or '02', please
        dup_lines = lines * 2
        rows = []
        for j in range(16):
            row_num = hex(j+1).split('x')[1].zfill(2)
            rows.append(MIDI_COLOUR_HEADER + half + row_num + MIDI_COLOUR_DELIM + dup_lines[j] + TERMINATOR)
        return rows

    def get_midi(self):
        lines = []
        for i in range(8):
            data = ''.join([''.join(self.board.get(BOARD_COORDS[i][j])) for j in range(8)])
            lines.append(data)

        block = self.build_msg_block(lines, '01') + self.build_msg_block(lines, '02')
        block.insert(0, DEFAULT_SETTINGS)
        return block

    def send_board_state(self, board):
        # where board is a chess.Board
        bad = set()
        for piece in board.piece_map().items():
            bad.add(piece[0])
            if piece[1].color: # white
                self.board.set(self.square_to_coords(piece[0]), ['7f', '7f', '7f'])
            else:
                self.board.set(self.square_to_coords(piece[0]), ['2f', '00', '17'])
        for i in range(64):
            if i not in bad:
                # print(i)
                self.board.set(self.square_to_coords(i), ['00', '00', '00'])


        self.push()

    def send_piece_selected(self, attacks):
        for x,y in attacks:
            self.board.set((7-y, x), ['7f', '00', '00'])

        self.push()

    def push(self):
        for midi_line in self.get_midi():
            msg = mido.Message.from_bytes(bytearray.fromhex(midi_line))
            self.output.send(msg)
