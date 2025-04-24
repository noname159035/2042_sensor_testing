from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
import time
from functools import partial
from components.ui_mainwindow import Ui_MainWindow
from components.test_bar import TestBar
from components.modal_info import ModalDialog
from components.modal_result import TestResultDialog
from sensor_library import *


# Поток для функции `wait_tests`
class WaitTestsThread(QThread):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

    def run(self):
        # print(self.main_window.active_tests)
        while True:
            time.sleep(1)

            for test_entry in self.main_window.active_tests:
                if test_entry["status"] == "In Progress":
                    title = test_entry["test"].labelTitle.text()
                    test_entry["test_name"], test_entry["status"], test_entry["result"] = get_test_results(title)
                    # print("Обновили состояние:", test_entry)

                    if test_entry["status"] in ["Success", "Fail"]:
                        test_bar = test_entry["test"]
                        test_bar.change_status(
                            status=test_entry["status"],
                        )

            all_ready = all(test_entry["status"] != "In Progress" for test_entry in self.main_window.active_tests)
            if all_ready:
                # print("Все готовы!")
                break


class MainWindow(QtWidgets.QMainWindow):
    active_tests = []
    datch_name = ''
    type_name = ''

    def showModalDialog(self):

        modal = ModalDialog(
            title="Заголовок",
            url="../img/type/type.jpg",
            text="текст",
            parent=self
        )

        modal.exec_()

    def showModalResultDialog(self, result, etalon):
        dialog = TestResultDialog(result, etalon, self)
        dialog.exec()

    def handleTestButtonClicked(self, test_name):
        # print(f"Кнопка нажата в тесте с названием: {test_name}")
        # print(self.active_tests)

        matching_test = next((test for test in self.active_tests if test['test_name'] == test_name), None)

        if matching_test:
            etalon = matching_test['etalon']
            result = matching_test['result']
            # print(f"Нашли тест: etalon={etalon}, result={result}")
            self.showModalResultDialog(result=result, etalon=etalon)
        else:
            pass
            # print(f"Тест с названием '{test_name}' не найден!")

    def start_test(self):
        self.update_tests()
        self.datch_name = self.ui.datch_menu.currentText()
        self.type_name = self.ui.type_menu.currentText()

        if self.datch_name != "Выбор датчика" and self.type_name != "Тип датчика":
            for test in get_tests_by_sensor(self.type_name, self.datch_name):
                test_bar = TestBar(
                    title=f"{test[0]}",
                    status="In Progress"
                )
                self.ui.verticalLayout_2.addWidget(test_bar)
                self.active_tests.append({
                    "test": test_bar,
                    "test_name": test[0],
                    "status": "In Progress",
                    "etalon": test[1],
                    "result": 0
                })

                test_bar.rightButton.clicked.connect(
                    partial(self.handleTestButtonClicked, test[0])
                )

            self.wait_thread = WaitTestsThread(self)
            self.wait_thread.start()

    def update_tests(self):
        while self.active_tests:
            test_entry = self.active_tests.pop()
            test_bar = test_entry["test"]
            self.ui.verticalLayout_2.removeWidget(test_bar)
            test_bar.hide()
            test_bar.deleteLater()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.verticalLayout_2.removeWidget(self.ui.test_bar_6)
        self.ui.test_bar_6.setParent(None)
        self.ui.verticalLayout_2.removeWidget(self.ui.test_bar_7)
        self.ui.test_bar_7.setParent(None)

        self.ui.more_info.clicked.connect(self.showModalDialog)

        self.ui.start_test.clicked.connect(self.start_test)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
