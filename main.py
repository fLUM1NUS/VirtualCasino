import sys
import time

import pygame
import sys

from PyQt5 import uic, QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QTextStream, QFile
from PyQt5.QtWidgets import QApplication, QMainWindow

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/start_ui.ui', self)  # Загружаем дизайн
        self.setWindowIcon(QtGui.QIcon('res/icon.png'))
        self.setWindowTitle('Виртуальное казино')
        self.quitBtn.clicked.connect(self.go_quit)
        self.shopBtn.clicked.connect(self.go_shop)
        # self.quitBtn.clicked.connect(self.go_pygame)

    def go_shop(self):
        self.window = ShopWindow()
        self.window.showFullScreen()
        self.hide()

    def go_quit(self):
        sys.exit()

    def go_pygame(self):
        self.hide()

        pygame.init()
        pygame.display.set_caption("Виртуальное казино")  # Название приложения
        #    size = width, height = 1600, 900  # размеры окна
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        programIcon = pygame.image.load('res/icon.png')  # Иконка приложения
        pygame.display.set_icon(programIcon)
        pygame.display.flip()
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()


class ShopWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/shop_ui.ui', self)  # Загружаем дизайн
        self.setWindowIcon(QtGui.QIcon('res/icon.png'))
        self.setWindowTitle('Виртуальное казино')
        self.goBackBtn.clicked.connect(self.go_back)


    def go_back(self):
        self.window = MenuWindow()
        self.window.showFullScreen()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    file = QFile("res/darkstyle.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())
    ex = MenuWindow()
    ex.showFullScreen()
    sys.excepthook = except_hook
    sys.exit(app.exec_())



# commit1
