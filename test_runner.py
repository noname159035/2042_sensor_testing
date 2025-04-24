# test_runner.py
# Возможно необходимо будет добавить команду catkin_make для обновления кэше при запуске на новых устройствах
# Команда catkin_make так же нужна при добавлении нового датчика
import subprocess
from sensor_library import get_sensor
import os
import subprocess
import time

def run_test(sensor_type: str, sensor_name: str):
    sensor = get_sensor(sensor_type, sensor_name)
    if not sensor:
        return f"Датчик {sensor_name} не найден для типа {sensor_type}"

    # Пути
    catkin_ws = os.environ.get("CATKIN_WS", os.path.join(os.path.abspath(os.path.dirname(__file__)), "catkin_ws"))
    catkin_setup = os.path.join(catkin_ws, "devel", "setup.bash")
    sensor_pkg = sensor["ros_pkg"]
    launch_file = sensor.get("launch_file", "scene_17.launch")
    test_scene = sensor.get("test_scene", "scene_17")

    # Команда запуска ROS-сцены
    roslaunch_cmd = f"source {catkin_setup} && roslaunch {sensor_pkg} {launch_file}"

    try:
        # Запуск Gazebo сцены с ROS-датчиком
        print(f"Запуск сцены {test_scene} для датчика {sensor_name}...")
        subprocess.Popen(["bash", "-c", roslaunch_cmd])

        # Подождем, чтобы сцена загрузилась
        time.sleep(5)

        # Определение пути к тест-скрипту
        test_script_name = f"test_{sensor_type.lower()}_{sensor_name.lower()}.py"
        test_script_path = os.path.join(catkin_ws, "src", sensor_pkg, "scripts", test_script_name)

        if os.path.exists(test_script_path):
            print(f"Запуск теста: {test_script_name}")
            subprocess.Popen(["python3", test_script_path])
        else:
            print(f"[!] Тест-скрипт не найден: {test_script_path}")

        return f"Тест '{test_script_name}' запущен (если существует). Сцена: {test_scene}."

    except Exception as e:
        return f"Ошибка при запуске теста: {e}"



def kill_gazebo():
    try:
        subprocess.run(["pkill", "-f", "gzserver"], check=False)
        subprocess.run(["pkill", "-f", "gzclient"], check=False)
        print("🔁 Gazebo был завершён принудительно.")
    except Exception as e:
        print("⚠️ Ошибка при завершении Gazebo:", e)
