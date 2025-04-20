# components/test_bar.py
from PyQt5 import QtWidgets, QtCore
from components.progress_bar_component import MyProgressBar
from components.modal_result import TestResultDialog

class TestBar(QtWidgets.QFrame):
    def showModalResultDialog(self, result, etalon):
        dialog = TestResultDialog(result, etalon, self)
        dialog.exec()

    def __init__(self, parent=None, title="Тест", left_button="Action1", right_button="Action2", status="Success"):
        super(TestBar, self).__init__(parent)
        self.setupUi(title, left_button, right_button, status)

    def setupUi(self, title, left_button, right_button, status):
        self.setObjectName("TestBarFrame")
        self.setMinimumSize(QtCore.QSize(476, 118))
        self.setMaximumSize(QtCore.QSize(476, 118))
        self.setStyleSheet("""
            QFrame#TestBarFrame {
                background: #EEEEEE;
                border: 1px solid #545659;
                border-radius: 15px;
                padding: 8px 12px;
            }
            QLabel {
                color: #545659;
                font-size: 16px;
                background: #EEEEEE;
            }
            QPushButton {
                border: 1px solid #545659;
                background: #D9D9D9;
                font-size: 14px;
            }
            QPushButton:hover {
                background: #CACACA;
            }
            QPushButton:pressed {
                background: #B8B8B8;
            }  
        """)
        # Заголовок
        self.labelTitle = QtWidgets.QLabel(self)
        self.labelTitle.setGeometry(QtCore.QRect(20, 10, 100, 40))
        self.labelTitle.setText(title)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")

        if (status != "In Progress"):
            # Левая кнопка
            self.leftButton = QtWidgets.QPushButton(self)
            self.leftButton.setGeometry(QtCore.QRect(20, 70, 201, 31))
            self.leftButton.setText(left_button)
            self.leftButton.setObjectName("leftButton")
            self.leftButton.setStyleSheet("""border-radius: 7px;""")
            # Правая кнопка
            self.rightButton = QtWidgets.QPushButton(self)
            self.rightButton.setGeometry(QtCore.QRect(260, 70, 201, 31))
            self.rightButton.setText(right_button)
            self.rightButton.setObjectName("rightButton")
            self.rightButton.setStyleSheet("""border-radius: 7px;""")
            self.rightButton.clicked.connect(lambda: self.showModalResultDialog(result=123, etalon=12)
)
        else:
            #Прогресс-бар
            self.progressBar = MyProgressBar(self)
            self.progressBar.setGeometry(QtCore.QRect(20, 70, 441, 31))
            self.progressBar.setValue(50)

        # Область статуса
        self.frameStatus = QtWidgets.QFrame(self)
        self.frameStatus.setGeometry(QtCore.QRect(330, 10, 132, 42))
        self.frameStatus.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameStatus.setObjectName("frameStatus")
        self.frameStatus.setStyleSheet("""
                    background-color: #FFFFFF;
                    border: 1px solid #545659;
                    border-radius: 10px;
                """)
        # Кружок статуса
        self.circle = QtWidgets.QFrame(self.frameStatus)
        self.circle.setGeometry(QtCore.QRect(10, 10, 22, 22))
        self.circle.setStyleSheet("border-radius: 20px; border: none;")
        if status == "Success":
            self.circle.setStyleSheet("background: #25BB57;")
        elif status == "In Progress":
            self.circle.setStyleSheet("background: #F0D000;")
        elif status == "Fail":
            self.circle.setStyleSheet("background: #BB2525;")
        self.circle.setObjectName("circle")

        # Текст статуса
        self.labelStatus = QtWidgets.QLabel(self.frameStatus)
        self.labelStatus.setGeometry(QtCore.QRect(40, 1, 80, 40))
        self.labelStatus.setText(status)
        self.labelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatus.setObjectName("labelStatus")
        self.labelStatus.setStyleSheet("""border: none;""")
