from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(1000, 300, 300, 300)
        self.setWindowTitle("hello qt5")
        self.init_ui()

    def init_ui(self):
        self.lable = QtWidgets.QLabel(self)
        self.lable.setText('lable1')
        self.lable.move(10, 10)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        self.b1.move(40, 40)
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.lable.setText("press the button")
        self.update()

    def update(self):
        self.lable.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
