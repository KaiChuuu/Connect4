import sys

from Board import Board

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Connect4(QWidget):
    game_map = ["start", "in-game", "end"]

    SCREEN_HEIGHT = 2100
    SCREEN_WIDTH = 1500

    ROWS = 6
    COLUMNS = 7
    WINNING_CHAIN = 4

    BOARD_WIDTH = 1204
    BOARD_HEIGHT = 1038

    SLOT_SCALE = 2

    def __init__(self):
        super(Connect4, self).__init__()

        # General Parameter Setup
        self.slot_diameter = (self.BOARD_WIDTH // self.COLUMNS) - (8 * self.SLOT_SCALE)
        self.slot_padding = (7 * self.SLOT_SCALE)
        self.center_X = self.SCREEN_WIDTH // 2
        self.center_Y = self.SCREEN_HEIGHT // 2
        self.current_player = 1
        self.game_status = "neutral"

        # Board Class Setup
        self.game_board = Board(self.ROWS, self.COLUMNS, self.WINNING_CHAIN)

        # PyQT Layout Setup
        self.initialize_UI()

        self.show()

    def initialize_UI(self):
        self.title = "Connect 4"
        self.setWindowTitle(self.title)
        self.setFixedSize(self.SCREEN_HEIGHT, self.SCREEN_WIDTH)
        self.board_ui = [[Slot(self.slot_diameter) for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]

        action_layout = QHBoxLayout()
        self.action_buttons = []
        self.display_layout = QGridLayout()

        # Title
        title_label = QLabel("CONNECT 4")
        title_label.setStyleSheet("font-size: 50px; color: blue; font-weight: bold; letter-spacing: 10px;")

        # Turn Display
        self.turn_label = QLabel("Player 1 turn!")
        self.turn_label.setStyleSheet("font-size: 30px; color: black;")

        # Title Container
        title_layout = QHBoxLayout()
        title_layout.addStretch()
        title_layout.addWidget(title_label)
        title_layout.addStretch()

        # Turn Container
        turn_layout = QHBoxLayout()
        turn_layout.addStretch()
        turn_layout.addWidget(self.turn_label)
        turn_layout.addStretch()

        # Top Container Vertical
        top_container = QVBoxLayout()
        top_container.addLayout(title_layout)
        top_container.addLayout(turn_layout)

        # Text Container Widget
        text_container = QWidget()
        text_container.setFixedSize(self.BOARD_WIDTH, 180)
        text_container.setLayout(top_container)

        # Final Text Container
        text_layout = QHBoxLayout()
        text_layout.addWidget(text_container)

        # Action Buttons
        for col in range(self.COLUMNS):
            btn = QPushButton(f"↓")
            btn.setStyleSheet("background-color: grey")
            btn.setDisabled(True)
            btn.clicked.connect(lambda _, c=col: self.drop_piece(c))
            self.action_buttons.append(btn)
            action_layout.addWidget(btn)

        # Connect 4 Board
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                self.display_layout.addWidget(self.board_ui[row][col], row, col)

        # Board Container
        board_layout = QVBoxLayout()
        board_layout.addLayout(action_layout)
        board_layout.addLayout(self.display_layout)

        # Create Board Widget
        container = QWidget()
        container.setFixedSize(self.BOARD_WIDTH, self.BOARD_HEIGHT)
        container.setStyleSheet("background-color: blue")
        container.setLayout(board_layout)

        # Final Board Layer
        hora_layout = QHBoxLayout()
        hora_layout.addStretch()
        hora_layout.addWidget(container)
        hora_layout.addStretch()

        # Start / Restart Buttons
        self.start_btn = QPushButton("START GAME")
        self.start_btn.setStyleSheet("font-size: 30px")
        self.start_btn.clicked.connect(self.start_game)

        self.restart_btn = QPushButton("RESTART GAME")
        self.restart_btn.setStyleSheet("font-size: 30px")
        self.restart_btn.clicked.connect(lambda _, r=True: self.end_game(r))
        self.restart_btn.setDisabled(True)

        # Start / End Widget
        menu_layout = QHBoxLayout()
        menu_layout.addWidget(self.start_btn)
        menu_layout.setSpacing(100)
        menu_layout.addWidget(self.restart_btn)

        menu_container = QWidget()
        menu_container.setFixedSize(self.BOARD_WIDTH, 100)
        menu_container.setLayout(menu_layout)

        menu_section = QHBoxLayout()
        menu_section.addStretch()
        menu_section.addWidget(menu_container)
        menu_section.addStretch()

        # Global Outer Vertical Layer
        vert_layout = QVBoxLayout()
        vert_layout.addLayout(text_layout)
        vert_layout.addLayout(hora_layout)
        vert_layout.addLayout(menu_section)

        self.setLayout(vert_layout)

    def drop_piece(self, column):
        for row in reversed(range(self.ROWS)):
            if self.board_ui[row][column].state == 0:
                self.board_ui[row][column].set_state(self.current_player)
                self.game_board.update_board(row, column, self.current_player)

                self.game_board.print_board()

                if row == 0:
                    self.action_buttons[column].setStyleSheet("background-color: grey")
                    self.action_buttons[column].setDisabled(True)

                if self.game_board.is_winning_move(row, column, self.current_player):
                    self.end_game(False)
                    return

                self.switch_turn()
                return

    def switch_turn(self):
        if self.current_player == 2:
            self.current_player = 1
            self.turn_label.setText("Player 1 turn!")
        else:
            self.current_player = 2
            self.turn_label.setText("Player 2 turn!")

    def start_game(self):
        self.game_status = 1
        self.game_board.reset_board()

        # Reset game board UI
        for row in range(self.ROWS):
            for col in range(self.COLUMNS):
                self.board_ui[row][col].set_state(0)

        self.game_board.reset_board()

        self.current_player = 1
        self.turn_label.setText("Player 1 turn!")

        self.start_btn.setDisabled(True)
        self.restart_btn.setDisabled(False)

        for btn in self.action_buttons:
            btn.setStyleSheet("background-color: white")
            btn.setDisabled(False)

        self.game_status = 2

    def end_game(self, isRestart):
        self.game_status = 2

        self.start_btn.setDisabled(False)
        self.restart_btn.setDisabled(True)

        for btn in self.action_buttons:
            btn.setStyleSheet("background-color: grey")
            btn.setDisabled(True)

        if not isRestart:
            self.turn_label.setText(f"PLAYER {self.current_player} WINS!")
            print(f"game end. {self.current_player} wins")
        else:
            self.turn_label.setText(f"GAME OVER")
            print(f"game end.")

class Slot(QWidget):
    color_map = {0 : Qt.white, 1 : Qt.red, 2 : Qt.yellow}

    def __init__(self, slotSize):
        super().__init__()
        self.state = 0 # 0 : white, 1 : red, 2: yellow
        self.slotSize = slotSize
        self.setMinimumSize(slotSize, slotSize)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(self.color_map[self.state], Qt.SolidPattern))
        rect = self.rect().adjusted(10, 10, -10, -10)
        painter.drawEllipse(rect)

    def set_state(self, state):
        self.state = state
        self.update()

if __name__ == "__main__":
    app = QApplication([])

    connect4 = Connect4()

    sys.exit(app.exec_())