# test_runner.py
# Возможно необходимо будет добавить команду catkin_make для обновления кэше при запуске на новых устройствах
# Команда catkin_make так же нужна при добавлении нового датчика
import subprocess
from sensor_library import get_sensor
import os
import subprocess


def run_test(sensor_type: str, sensor_name: str):
    sensor = get_sensor(sensor_type, sensor_name)
    if not sensor:
        return f"Датчик {sensor_name} не найден для типа {sensor_type}"

    # Получаем путь к catkin_ws из переменной окружения или вычисляем относительно текущей директории.
    catkin_ws = os.environ.get("CATKIN_WS", os.path.join(os.path.abspath(os.path.dirname(__file__)), "catkin_ws"))
    catkin_setup = os.path.join(catkin_ws, "devel", "setup.bash")

    try:
        cmd = f"source {catkin_setup} && roslaunch {sensor['ros_pkg']} {sensor['launch_file']}"
        subprocess.Popen(["bash", "-c", cmd])
        return (f"Запущен тест для датчика '{sensor_name}' с тестовой сценой "
                f"'{sensor['test_scene']}'. (ROS-лаунч: {sensor['ros_pkg']} {sensor['launch_file']})")
    except Exception as e:
        return f"Ошибка при запуске теста: {e}"