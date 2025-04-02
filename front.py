import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QGroupBox, QRadioButton, QPushButton, QCheckBox,
    QLabel, QComboBox, QScrollArea
)


class SensorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Основной layout
        main_layout = QHBoxLayout()

        # Левая панель (30% ширины)
        left_panel = QVBoxLayout()

        # Группа "Тип датчика"
        type_group = QGroupBox("Тип датчика")
        type_layout = QVBoxLayout()
        for i in range(1, 5):
            type_layout.addWidget(QRadioButton(f"Тип {i}"))
        type_group.setLayout(type_layout)
        type_layout.setContentsMargins(10, 20, 10, 10)  # Отступы

        # Группа "Выбор датчика"
        sensor_group = QGroupBox("Выбор датчика")
        sensor_layout = QVBoxLayout()
        sensors = ["Датчик 1", "Датчик 2", "Датчик 3", "Загрузить"]
        self.sensor_combo = QComboBox()
        self.sensor_combo.addItems(sensors)
        sensor_layout.addWidget(self.sensor_combo)
        sensor_group.setLayout(sensor_layout)
        sensor_layout.setSpacing(15)

        # Кнопки
        details_btn = QPushButton("Подробнее")
        start_btn = QPushButton("Start test")

        left_panel.addWidget(type_group)
        left_panel.addWidget(sensor_group)
        left_panel.addWidget(details_btn)
        left_panel.addWidget(start_btn)
        left_panel.addStretch()

        # Правая панель (70% ширины)
        right_panel = QVBoxLayout()
        scroll = QScrollArea()
        content = QWidget()
        self.test_layout = QVBoxLayout(content)

        # Генерация тестов
        for i in range(4):
            test_group = QGroupBox(f"Тест {i + 1}")
            test_inner = QVBoxLayout()

            details = QPushButton("подробнее")
            success = QCheckBox("Success")

            test_inner.addWidget(details)
            test_inner.addWidget(success)
            test_group.setLayout(test_inner)
            self.test_layout.addWidget(test_group)

        scroll.setWidget(content)
        scroll.setWidgetResizable(True)
        right_panel.addWidget(scroll)

        # Стилизация
        self.setStyleSheet("""
            QWidget {
                font-family: "Arial";
                background: #FFFFFF;
            }
            QGroupBox {
                font-size: 16px;
                color: #333333;
                border: 1px solid #CCCCCC;
                border-radius: 5px;
                margin-top: 15px;
                padding-top: 15px;
            }
            QPushButton {
                background: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                min-width: 100px;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background: #45A049;
            }
            QComboBox {
                padding: 5px;
                border: 1px solid #CCCCCC;
            }
            QCheckBox {
                spacing: 8px;
                font-size: 14px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 1px solid #CCCCCC;
            }
            QCheckBox::indicator:checked {
                background: #4CAF50;
                border: 1px solid #40923F;
            }
        """)

        # Сборка интерфейса
        main_layout.addLayout(left_panel, 30)
        main_layout.addLayout(right_panel, 70)
        self.setLayout(main_layout)

        # Настройки окна
        self.setWindowTitle('Sensor Testing App')
        self.setGeometry(300, 300, 800, 500)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SensorApp()
    sys.exit(app.exec_())
    print("test")
