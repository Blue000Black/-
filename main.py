from random import randint
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
import sys
from PyQt6 import uic


class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle("Жёлтые круги")
        self.circle = [0, 0 ,0]
        self.btn.clicked.connect(self.act)

    def act(self):
        self.circle[2] = randint(20, 300)
        self.circle[0] = randint(0, self.width() - self.circle[2])
        self.circle[1] = randint(0, self.height() - self.circle[2])

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        painter.drawEllipse(self.circle[0], self.circle[1], self.circle[2], self.circle[2])
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())
