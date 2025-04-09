import math

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Canvas(QWidget):
    screenHeight = 2100
    screenWidth = 1500

    slotScale = 1.5

    def __init__(self):
        super(Canvas, self).__init__()
        self.title = "Connect 4"

        self.initializeUI()

    def initializeUI(self):
        self.canvasSettings()

        self.show()

    def canvasSettings(self):
        self.setWindowTitle(self.title)
        self.resize(self.screenHeight, self.screenWidth)

    def paintEvent(self, event):
        qp = QPainter(self)

        # Connect 4 Board
        qp.setBrush(QColor(0, 0, 255))
        qp.setPen(Qt.NoPen)

        centerX = self.width() // 2
        centerY = self.height() // 2

        boardWidth = 1204 # multiple of 7
        boardHeight = 1038 # multiple of 6
        boardX = centerX - boardWidth // 2
        boardY = math.floor(centerY - boardHeight / 1.75)

        qp.drawRect(boardX, boardY, boardWidth, boardHeight)

        # Connect 4 Slots
        cols = 7
        rows = 6
        slotDiameter = (boardWidth // 7) - (8 * self.slotScale)
        slotPadding = (7 * self.slotScale)
        qp.setBrush(Qt.white)
        for row in range(rows):
            for col in range(cols):
                x = boardX + slotPadding + col * (slotDiameter + slotPadding)
                y = boardY + slotPadding + row * (slotDiameter + slotPadding)
                qp.drawEllipse(x, y, slotDiameter, slotDiameter)