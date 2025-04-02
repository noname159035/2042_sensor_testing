# test_runner.py

import subprocess
from sensor_library import get_sensor

def run_test(sensor_type: str, sensor_name: str):
    sensor = get_sensor(sensor_type, sensor_name)
    if not sensor:
        return f"Датчик {sensor_name} не найден для типа {sensor_type}"

    # Здесь в будущем можно использовать subprocess для запуска ROS/Gazebo.
    # Пока возвращаем сообщение о запуске теста.
    # Например, можно вызвать: subprocess.Popen(["bash", sensor['ros_launch']])
    return (f"Запущен тест для датчика '{sensor_name}' с тестовой сценой '{sensor['test_scene']}'. "
            f"(ROS-лаунч: {sensor['ros_launch']})")