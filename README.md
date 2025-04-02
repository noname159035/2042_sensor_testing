# 2042_sensor_testing

Чтоб посмотреть структуру откройте файл во вкладке Code вместо Preview

backend/
├── main.py                  # Точка входа: консольное меню
├── sensor_library.py        # "Библиотека" датчиков с привязками к ROS-лаунч файлам и тестовым сценам
├── test_runner.py           # Модуль для запуска тестов (заглушка)
└── test_scripts/            # Папка с тестовыми скриптами (заглушки)
    ├── launch_stereo.sh
    ├── launch_mono.sh
    ├── launch_depth.sh
    ├── launch_touch.sh
    ├── launch_multi_touch.sh
    ├── launch_rfid.sh
    └── launch_rfid_long.sh
