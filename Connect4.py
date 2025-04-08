import sys
from PyQt5.QtWidgets import QApplication, QWidget
from Board import Board
from Canvas import Canvas

class Connect4:
    def __init__(self):
        self.gameBoard = Board()

    def startGame(self):
        self.gameBoard.resetBoard()


    def endGame(self):
        pass


if __name__ == "__main__":
    app = QApplication([])

    canvas = Canvas()
    sys.exit(app.exec_())


    # game = Connect4()
    # game.startGame()


