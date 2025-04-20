# main.py
import sys
from PyQt5 import QtCore, QtWidgets
from components.ui_mainwindow import Ui_MainWindow
from components.test_bar import TestBar
# Импорт компонента прогресс-бара, если требуется
from components.progress_bar_component import MyProgressBar
from components.modal_info import ModalDialog
import os

class MainWindow(QtWidgets.QMainWindow):
    def showModalDialog(self, title, img_url, text):
        # Пример вызова модального окна с данными
        modal = ModalDialog(
            title=title,
            url=img_url,
            text=text,
            parent=self
        )
        modal.exec_()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Создаем интерфейс из .ui файла

        # Убираем статичные блоки, добавленные в Designer
        self.ui.verticalLayout_2.removeWidget(self.ui.test_bar_6)
        self.ui.test_bar_6.setParent(None)
        self.ui.verticalLayout_2.removeWidget(self.ui.test_bar_7)
        self.ui.test_bar_7.setParent(None)

        # Динамически создаем несколько экземпляров TestBar
        # for i in range(3):
        #     test_bar = TestBar(
        #         title=f"Тест {i+1}",
        #         left_button="Подробнее",
        #         right_button="Результат",
        #         status="Fail"
        #     )
        #     self.ui.verticalLayout_2.addWidget(test_bar)

        test_bar = TestBar(
            title=f"Тест 3",
            left_button="Подробнее",
            right_button="Результат",
            status="In Progress"
        )
        self.ui.verticalLayout_2.addWidget(test_bar)

        test_bar = TestBar(
            title=f"Тест 3",
            left_button="Подробнее",
            right_button="Результат",
            status="Success"
        )
        self.ui.verticalLayout_2.addWidget(test_bar)

        test_bar = TestBar(
            title=f"Тест 3",
            left_button="Подробнее",
            right_button="Результат",
            status="Fail"
        )
        self.ui.verticalLayout_2.addWidget(test_bar)

        self.ui.more_info.clicked.connect(
            lambda: self.showModalDialog(
                title="Информация",
                img_url="../img/image_1.jpg",
                text="Это текст модального окна."
            )
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
