import mido
from queue import Queue

from midiboard import MIDIBoard
from constants import *

class MidiFighterIO():
    def __init__(self):
        self.board = MIDIBoard()
        self.input = mido.open_input('Midi Fighter 64')
        self.output = mido.open_output('Midi Fighter 64')
        # self.draw_queue = Queue()

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

    def push(self):
        for midi_line in self.get_midi():
            msg = mido.Message.from_bytes(bytearray.fromhex(midi_line))
            self.output.send(msg)