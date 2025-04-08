import math

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Canvas(QWidget):
    def __init__(self):
        super(Canvas, self).__init__()
        self.title = "Connect 4"

        self.initializeUI()

    def initializeUI(self):
        self.canvasSettings()

        self.show()

    def canvasSettings(self):
        self.setWindowTitle(self.title)
        self.resize(2100, 1500)

    def paintEvent(self, event):
        qp = QPainter(self)

        # Connect 4 Board
        qp.setBrush(QColor(0, 0, 255))
        qp.setPen(Qt.NoPen)

        centerX = self.width() // 2
        centerY = self.height() // 2

        boardWidth = 1200
        boardHeight = 800
        boardX = centerX - boardWidth // 2
        boardY = math.floor(centerY - boardHeight / 1.5)

        qp.drawRect(boardX, boardY, boardWidth, boardHeight)

        # Connect 4 Slots
        cols = 7
        rows = 6
        slotDiameter = 80
        slotPadding = 10
        qp.setBrush(Qt.white)
        for row in range(rows):
            for col in range(cols):
                x = boardX + slotPadding + col * (slotDiameter + slotPadding)
                y = boardY + slotPadding + row * (slotDiameter + slotPadding)
                qp.drawEllipse(x, y, slotDiameter, slotDiameter)
