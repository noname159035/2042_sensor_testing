# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(718, 488)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("/* Кружочек */\n"
"QScrollArea QFrame QFrame QFrame {\n"
"    min-width: 22px;\n"
"    max-width: 22px;\n"
"    min-height: 22px;\n"
"    max-height: 22px;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    border: none;\n"
"    background: #25BB57;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"/* Статус */\n"
"QScrollArea QFrame QFrame QLabel {\n"
"    min-width: 80px;\n"
"    max-width: 80px;\n"
"    min-height: 40px;\n"
"    max-height: 40px;\n"
"    background: none;\n"
"    qproperty-alignment: \'AlignRight | AlignVCenter\';\n"
"    color: #545659;\n"
"    font-size: 16px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"}\n"
"\n"
"QScrollArea QFrame QFrame {\n"
"    border: 1px solid #545659;\n"
"    border-radius: 12px;\n"
"    padding: 0;\n"
"    background: #EEEEEE;\n"
"    min-width: 130px;\n"
"    max-width: 130px;\n"
"    min-height: 40px;\n"
"    max-height: 40px;\n"
"}\n"
"\n"
"QScrollArea QFrame QLabel {\n"
"    border: none;\n"
"    min-width: 100px;\n"
"    min-height: 25px;\n"
"    border-radius: 5px;\n"
"    padding: 0;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"}\n"
"\n"
"QScrollArea QFrame QPushButton {\n"
"    border: 1px solid #545659;\n"
"    min-width: 100px;\n"
"    min-height: 25px;\n"
"    border-radius: 5px;\n"
"    padding: 0;\n"
"    background: #D9D9D9;\n"
"}\n"
"\n"
"QScrollArea QFrame QPushButton:hover {\n"
"    background: #CACACA;\n"
"}\n"
"\n"
"QScrollArea QFrame QPushButton:pressed {\n"
"    background: #B8B8B8;\n"
"}\n"
"\n"
"QMainWindow {\n"
"    background: #D9D9D9;\n"
"}\n"
"\n"
"QScrollArea QFrame {\n"
"    background: #EEEEEE;\n"
"    border-radius: 15px;\n"
"    border: 1px solid #545659;\n"
"    padding: 8px 12px;\n"
"    min-width: 450px;\n"
"    max-width: 450px;\n"
"    min-height: 100px;\n"
"    max-height: 100px;\n"
"}\n"
"\n"
"\n"
"QScrollArea {\n"
"    background: #D9D9D9;\n"
"    border: none;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents {\n"
"    background: #D9D9D9;\n"
"    border: none;\n"
"}\n"
"\n"
"/* Стили для самого прогресс-бара */\n"
"QProgressBar {\n"
"    border: 2px solid #545659;         /* Рамка */\n"
"    border-radius: 10px;               /* Закругление углов */\n"
"    background: #ecf0f1;               /* Фон всего прогресс-бара */\n"
"    text-align: center;                /* Выравнивание текста по центру */\n"
"    color: #2c3e50;                    /* Цвет текста */\n"
"    font: bold 14px;                   /* Шрифт текста */\n"
"}\n"
"\n"
"/* Стили для части, обозначающей прогресс (chunk) */\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #F0D000, stop:1 #F0D000\n"
"    );                                /* Градиент заполнения */\n"
"    border-radius: 8px;                /* Закругление углов для чанка */\n"
"    margin: 1px;                      /* Небольшой отступ, чтобы рамка прогресс-бара была видна */\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.left_nav = QtWidgets.QFrame(self.centralwidget)
        self.left_nav.setGeometry(QtCore.QRect(10, 10, 211, 471))
        self.left_nav.setStyleSheet("#left_nav {\n"
"    background: #EEEEEE;\n"
"    border-radius: 15px;\n"
"    border: 1px solid #545659;\n"
"    padding: 8px 12px;\n"
"    min-width: 100px;   \n"
"    min-height: 30px;  \n"
"}")
        self.left_nav.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_nav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_nav.setObjectName("left_nav")
        self.type_menu = QtWidgets.QComboBox(self.left_nav)
        self.type_menu.setGeometry(QtCore.QRect(10, 20, 191, 19))
        self.type_menu.setStyleSheet("#type_menu {\n"
"    border: none;\n"
"    padding-right: 5px;\n"
"    color: #545659;\n"
"    text-align: center;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"background: #EEEEEE;\n"
"}\n"
"#type_menu::drop-down {\n"
"\n"
"}\n"
"")
        self.type_menu.setObjectName("type_menu")
        self.type_menu.addItem("")
        self.type_menu.addItem("")
        self.type_menu.addItem("")
        self.type_menu.addItem("")
        self.type_menu.addItem("")
        self.type_menu.addItem("")
        self.datch_menu = QtWidgets.QComboBox(self.left_nav)
        self.datch_menu.setGeometry(QtCore.QRect(10, 190, 191, 19))
        self.datch_menu.setStyleSheet("#datch_menu {\n"
"    border: none;\n"
"    padding-right: 5px;\n"
"    color: #545659;\n"
"    text-align: center;\n"
"font-size: 16px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"background: #EEEEEE;\n"
"}\n"
"#datch_menu::drop-down {\n"
"\n"
"}\n"
"")
        self.datch_menu.setObjectName("datch_menu")
        self.datch_menu.addItem("")
        self.datch_menu.addItem("")
        self.datch_menu.addItem("")
        self.datch_menu.addItem("")
        self.datch_menu.addItem("")
        self.datch_menu.addItem("")
        self.more_info = QtWidgets.QPushButton(self.left_nav)
        self.more_info.setGeometry(QtCore.QRect(10, 350, 184, 54))
        self.more_info.setStyleSheet("#more_info {\n"
"    width: 180px;\n"
"    height: 50px;\n"
"    border-radius: 15px;\n"
"    border: 2px solid #545659;\n"
"    background: #EEEEEE;\n"
"    color: #545659;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"    padding: 0;\n"
"}\n"
"\n"
"#more_info:hover {\n"
"    background: #D8D8D8;\n"
"}\n"
"\n"
"#more_info:pressed {  \n"
"    background: #C4C4C4;\n"
"}")
        self.more_info.setObjectName("more_info")
        self.start_test = QtWidgets.QPushButton(self.left_nav)
        self.start_test.setGeometry(QtCore.QRect(10, 410, 184, 54))
        self.start_test.setStyleSheet("#start_test {\n"
"    width: 180px;\n"
"    height: 50px;\n"
"    border-radius: 15px;\n"
"    border: 2px solid #545659;\n"
"    background: #EEEEEE;\n"
"    color: #545659;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"    padding: 0; \n"
"}\n"
"\n"
"#start_test:hover {\n"
"    background: #D8D8D8;\n"
"}\n"
"\n"
"#start_test:pressed {\n"
"    background: #C4C4C4;\n"
"}")
        self.start_test.setObjectName("start_test")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(230, 10, 481, 471))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 481, 471))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.test_bar_6 = QtWidgets.QFrame(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_bar_6.sizePolicy().hasHeightForWidth())
        self.test_bar_6.setSizePolicy(sizePolicy)
        self.test_bar_6.setMinimumSize(QtCore.QSize(476, 118))
        self.test_bar_6.setMaximumSize(QtCore.QSize(476, 118))
        self.test_bar_6.setStyleSheet("")
        self.test_bar_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test_bar_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.test_bar_6.setObjectName("test_bar_6")
        self.label_19 = QtWidgets.QLabel(self.test_bar_6)
        self.label_19.setGeometry(QtCore.QRect(20, 10, 100, 40))
        self.label_19.setStyleSheet("color: #545659;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"background: #EEEEEE;")
        self.label_19.setObjectName("label_19")
        self.pushButton_19 = QtWidgets.QPushButton(self.test_bar_6)
        self.pushButton_19.setGeometry(QtCore.QRect(20, 70, 201, 31))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.test_bar_6)
        self.pushButton_20.setGeometry(QtCore.QRect(260, 70, 201, 31))
        self.pushButton_20.setObjectName("pushButton_20")
        self.frame_19 = QtWidgets.QFrame(self.test_bar_6)
        self.frame_19.setGeometry(QtCore.QRect(330, 10, 132, 42))
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.frame_20 = QtWidgets.QFrame(self.frame_19)
        self.frame_20.setGeometry(QtCore.QRect(10, 10, 22, 22))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.label_20 = QtWidgets.QLabel(self.frame_19)
        self.label_20.setGeometry(QtCore.QRect(40, 0, 80, 40))
        self.label_20.setMinimumSize(QtCore.QSize(80, 40))
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.test_bar_6)
        self.test_bar_7 = QtWidgets.QFrame(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_bar_7.sizePolicy().hasHeightForWidth())
        self.test_bar_7.setSizePolicy(sizePolicy)
        self.test_bar_7.setMinimumSize(QtCore.QSize(476, 118))
        self.test_bar_7.setMaximumSize(QtCore.QSize(476, 118))
        self.test_bar_7.setStyleSheet("")
        self.test_bar_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.test_bar_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.test_bar_7.setObjectName("test_bar_7")
        self.label_21 = QtWidgets.QLabel(self.test_bar_7)
        self.label_21.setGeometry(QtCore.QRect(20, 10, 100, 40))
        self.label_21.setStyleSheet("color: #545659;\n"
"    text-align: center;\n"
"    font-size: 16px;\n"
"    font-style: normal;\n"
"    font-weight: 400;\n"
"    line-height: normal;\n"
"background: #EEEEEE;")
        self.label_21.setObjectName("label_21")
        self.frame_21 = QtWidgets.QFrame(self.test_bar_7)
        self.frame_21.setGeometry(QtCore.QRect(330, 10, 132, 42))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.frame_22 = QtWidgets.QFrame(self.frame_21)
        self.frame_22.setGeometry(QtCore.QRect(10, 10, 22, 22))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.label_22 = QtWidgets.QLabel(self.frame_21)
        self.label_22.setGeometry(QtCore.QRect(40, 0, 80, 40))
        self.label_22.setMinimumSize(QtCore.QSize(80, 40))
        self.label_22.setObjectName("label_22")
        self.progressBar = QtWidgets.QProgressBar(self.test_bar_7)
        self.progressBar.setGeometry(QtCore.QRect(20, 80, 441, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.test_bar_7)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.type_menu.setItemText(0, _translate("MainWindow", "Тип датчика"))
        self.type_menu.setItemText(1, _translate("MainWindow", "Тип 1"))
        self.type_menu.setItemText(2, _translate("MainWindow", "Тип 2"))
        self.type_menu.setItemText(3, _translate("MainWindow", "Тип 3"))
        self.type_menu.setItemText(4, _translate("MainWindow", "Тип 4"))
        self.type_menu.setItemText(5, _translate("MainWindow", "Тип 5"))
        self.datch_menu.setItemText(0, _translate("MainWindow", "Выбор датчика"))
        self.datch_menu.setItemText(1, _translate("MainWindow", "Датчик 1"))
        self.datch_menu.setItemText(2, _translate("MainWindow", "Датчик 2"))
        self.datch_menu.setItemText(3, _translate("MainWindow", "Датчик 3"))
        self.datch_menu.setItemText(4, _translate("MainWindow", "Датчик 4"))
        self.datch_menu.setItemText(5, _translate("MainWindow", "Датчик 5"))
        self.more_info.setText(_translate("MainWindow", "Подробнее"))
        self.start_test.setText(_translate("MainWindow", "Начать тестирование"))
        self.label_19.setText(_translate("MainWindow", "Тест 1"))
        self.pushButton_19.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_20.setText(_translate("MainWindow", "PushButton"))
        self.label_20.setText(_translate("MainWindow", "Success"))
        self.label_21.setText(_translate("MainWindow", "Тест 1"))
        self.label_22.setText(_translate("MainWindow", "In Progress"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
