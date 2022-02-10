

from PyQt5 import QtWidgets
import sys

from window import Window


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
