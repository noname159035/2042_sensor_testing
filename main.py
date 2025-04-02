# main.py

from sensor_library import get_sensor_types, get_sensors_by_type, add_sensor, get_sensor
from test_runner import run_test

def print_menu():
    print("\nВыберите опцию:")
    print("1. Показать типы датчиков")
    print("2. Выбрать тип датчика и показать доступные датчики")
    print("3. Добавить свой датчик")
    print("4. Запустить тест для выбранного датчика")
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

def run_sensor_test():
    sensor_type = input("Введите тип датчика для теста: ")
    sensor_name = input("Введите имя датчика для теста: ")
    sensor = get_sensor(sensor_type, sensor_name)
    if not sensor:
        print("Ошибка: датчик не найден для указанного типа.")
        return
    result = run_test(sensor_type, sensor_name)
    print(result)

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