# components/progress_bar_component.py
from PyQt5 import QtWidgets


class MyProgressBar(QtWidgets.QProgressBar):
    def __init__(self, parent=None):
        super(MyProgressBar, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setMinimum(0)
        self.setMaximum(100)
        self.setValue(0)
        self.setStyleSheet("""
            QProgressBar {
                border: 2px solid #545659;
                border-radius: 10px;
                background: #ecf0f1;
                text-align: center;
                color: #2c3e50;
                font: bold 14px;
            }
            QProgressBar::chunk {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 #F0D000, stop:1 #F0D000
                );
                border-radius: 8px;
                margin: 1px;
            }
        """)
