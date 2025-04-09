import sys
import math

from Board import Board

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Connect4(QWidget):
    SCREEN_HEIGHT = 2100
    SCREEN_WIDTH = 1500

    ROWS = 6
    COLUMNS = 7
    WINNING_CHAIN = 4
    BOARD_WIDTH = 1204
    BOARD_HEIGHT = 1038

    SLOT_SCALE = 1.5

    def __init__(self):
        super(Connect4, self).__init__()

        # General Parameter Setup
        self.slot_diameter = (self.BOARD_WIDTH // self.COLUMNS) - (8 * self.SLOT_SCALE)
        self.slot_padding = (7 * self.SLOT_SCALE)
        self.center_X = self.SCREEN_WIDTH // 2
        self.center_Y = self.SCREEN_HEIGHT // 2
        self.current_player = 1

        # Board Class Setup
        self.game_board = Board(self.ROWS, self.COLUMNS, self.WINNING_CHAIN)

        # PyQT Layout Setup
        self.initialize_UI()

        self.show()

    def initialize_UI(self):
        self.title = "Connect 4"
        self.setWindowTitle(self.title)
        self.resize(self.SCREEN_HEIGHT, self.SCREEN_WIDTH)
        self.board_ui = [[Slot(self.slot_diameter) for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]

        main_layout = QVBoxLayout()
        action_layout = QHBoxLayout()
        display_layout = QGridLayout()




    def start_game(self):
        pass

    def end_game(self):
        pass


class Slot(QWidget):
    def __init__(self, slotSize):
        super().__init__()
        self.state = 0
        self.slotSize = slotSize

if __name__ == "__main__":
    app = QApplication([])

    connect4 = Connect4()

    sys.exit(app.exec_())



