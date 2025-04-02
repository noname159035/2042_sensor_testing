from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('UI/untitled.ui', self)  # Загрузка UI

        # Работа с элементами
        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        print("Прямая загрузка UI!")


if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()