#!/usr/bin/env python3
# main.py

from sensor_library import get_sensor_types, get_sensors_by_type, add_sensor, get_sensor
from test_runner import run_test
import subprocess
import os
import time

def print_menu():
    print("\nВыберите опцию:")
    print("1. Показать типы датчиков")
    print("2. Выбрать тип датчика и показать доступные датчики")
    print("3. Добавить свой датчик")
    print("4. Запустить тест для выбранного датчика и захватить изображение")
    print("5. Выход")


def list_sensor_types():
    types = get_sensor_types()
    print("Доступные типы датчиков:")
    for t in types:
        print(f"- {t}")


def list_sensors_by_type():
    sensor_type = input("Введите тип датчика: ")
    sensors = get_sensors_by_type(sensor_type)
    if not sensors:
        print("Датчики не найдены для данного типа.")
    else:
        print(f"Датчики типа '{sensor_type}':")
        for sensor in sensors:
            print(f"- {sensor['name']} (ROS-лаунч: {sensor['ros_launch']}, Тестовая сцена: {sensor['test_scene']})")


def add_custom_sensor():
    sensor_type = input("Введите тип датчика, к которому хотите добавить свой: ")
    sensor_name = input("Введите имя вашего датчика: ")
    ros_launch = input("Введите путь к ROS-лаунч файлу: ")
    test_scene = input("Введите название тестовой сцены: ")
    new_sensor = {
        "name": sensor_name,
        "ros_launch": ros_launch,
        "test_scene": test_scene
    }
    add_sensor(sensor_type, new_sensor)
    print(f"Датчик '{sensor_name}' успешно добавлен в тип '{sensor_type}'.")


def capture_image():
    try:
        import rospy
        from sensor_msgs.msg import Image
        from cv_bridge import CvBridge
        import cv2
    except ImportError as e:
        print("Нужно установить ROS-модули:", e)
        return None

    if not rospy.core.is_initialized():
        rospy.init_node("image_capture_node", anonymous=True)

    try:
        print("Ожидаем изображение с /test_camera/image_raw...")
        msg = rospy.wait_for_message("/depth_camera/image_raw", Image, timeout=30)
        image = CvBridge().imgmsg_to_cv2(msg, "bgr8")
        filename = "captured_image.png"
        cv2.imwrite(filename, image)
        return filename
    except Exception as e:
        print("Ошибка при захвате:", e)
        return None


def run_sensor_test():
    sensor_type = input("Введите тип датчика для теста: ")
    sensor_name = input("Введите имя датчика для теста: ")
    sensor = get_sensor(sensor_type, sensor_name)
    if not sensor:
        print("Ошибка: датчик не найден для указанного типа.")
        return
    # Запускаем тест (roslaunch команда) через функцию run_test
    result = run_test(sensor_type, sensor_name)
    print(result)

    # Ждем, чтобы тестовая сцена успела запуститься и камера начала публиковать данные
    print("Ожидание запуска тестовой сцены и публикации данных камеры...")
    time.sleep(5)

    # Захватываем изображение
    filename = capture_image()
    if filename:
        print("Изображение успешно захвачено и сохранено как", filename)
    else:
        print("Не удалось захватить изображение.")

'''
def main():
    while True:
        print_menu()
        choice = input("Введите номер опции: ")
        if choice == "1":
            list_sensor_types()
        elif choice == "2":
            list_sensors_by_type()
        elif choice == "3":
            add_custom_sensor()
        elif choice == "4":
            run_sensor_test()
        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте еще раз.")



main()
'''

def menu():
    while True:
        print("\n1. Типы датчиков\n2. Список датчиков\n3. Добавить датчик\n4. Запуск теста с захватом\n5. Выход")
        choice = input("Выберите опцию: ")
        if choice == "1":
            for t in get_sensor_types(): print("-", t)
        elif choice == "2":
            t = input("Тип датчика: ")
            for s in get_sensors_by_type(t): print("-", s["name"])
        elif choice == "3":
            t = input("Тип: ")
            n = input("Имя: ")
            p = input("Пакет: ")
            f = input("Файл launch: ")
            sc = input("Сцена: ")
            add_sensor(t, {"name": n, "ros_pkg": p, "launch_file": f, "test_scene": sc})
        elif choice == "4":
            t = input("Тип: ")
            n = input("Имя: ")
            print(run_test(t, n))
            print("Ожидаем запуск...")
            time.sleep(5)
            image = capture_image()
            if image:
                print("Снимок сохранен:", image)
            else:
                print("Снимок не удалось получить.")
        elif choice == "5":
            break

menu()
