import random

sensor_library = {

    # Из рабочего на данный момент тут только 2 пути для стерео и моно камеры в 1 сцену "Сцена №1"
    # К остальным датчикам надо править пути
    
    "camera": [
        {
            "name": "duo_minilx_lv1",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "duo_minilx_lv1.launch",
            "test_scene": "Стереокамера - Комплексная сцена",
            "image_topic": "/duo_minilx_lv1/left/image_raw",
            "config_file": "camera_configs/duo_minilx_lv1.yaml",
            "tests": {
                "Тест на угол обзора": (75, 73),
                "Тест на точность стерео-глубины": (4, 8)
            }
        },
        {"name": "mono_camera", "ros_pkg": "scenario_test_pkg", "launch_file": "scenario_mono_camera.launch", "test_scene": "Сцена №1", "image_topic":"/mono_camera/image_raw", "tests": [("Тест на угол обзора", 100)]},
        {
            "name": "depth_camera",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "scenario_1_test.launch",
            "test_scene": "Сцена №1",
            "image_topic":"/depth_camera/image_raw",
            "tests": [
                ("Тест на угол обзора", 100),
                ("Тест на хуй", 10),
                ("ТЕст на похуй", 1000)
            ]
        }
    ],
    "tactile": [
        {"name": "Wacoh-Tech DynPick", "ros_launch": "test_scripts/launch_wacoh_dynpick.sh", "test_scene": "touch_scene","tests": [("Тест на угол обзора", 100)]},
        {"name": "ATI nano 25 and AMTI HE6x6 force plate", "ros_launch": "test_scripts/launch_ati_nano25.sh", "test_scene": "touch_scene", "tests": [("Тест на угол обзора", 100),("Тест на хуй", 10),]},
        {
            "name": "Leptrino force/torque sensor",
            "ros_launch": "test_scripts/launch_leptrino.sh",
            "test_scene": "touch_scene",
            "tests": [

            ]
        },
        {"name": "Nano17 6-axis force/torque sensors", "ros_launch": "test_scripts/launch_nano17.sh", "test_scene": "touch_scene"},
        {"name": "Interface to ATI NetFT sensor adapter", "ros_launch": "test_scripts/launch_ati_netft.sh", "test_scene": "touch_scene"},
        {"name": "Schunk LWA 3 Force Torque Controller based on ATI Mini 45", "ros_launch": "test_scripts/launch_schunk_lwa3.sh", "test_scene": "touch_scene"},
        {"name": "skin_driver", "ros_launch": "test_scripts/launch_skin_driver.sh", "test_scene": "touch_scene"}
    ],
    "rfid": [
        {"name": "UHF RFID Reader", "ros_pkg": "scenario_test_pkg", "launch_file": "scenario_rfid_angle_test.launch", "test_scene": "rfid"},
        {"name": "Huxi RFID Reader", "ros_launch": "test_scripts/launch_huxi_rfid.sh", "test_scene": "rfid_scene"}
    ]
}

result_data = {
    "Тест на угол обзора": 2,
    "Тест на хуй": 123
}

def get_sensor_types():
    return list(sensor_library.keys())

def get_sensors_by_type(sensor_type: str):
    return sensor_library.get(sensor_type, [])

def get_sensor(sensor_type: str, sensor_name: str):
    sensors = sensor_library.get(sensor_type, [])
    for sensor in sensors:
        if sensor["name"] == sensor_name:
            return sensor
    return None

def add_sensor(sensor_type: str, sensor_data: dict):
    if sensor_type not in sensor_library:
        sensor_library[sensor_type] = []
    sensor_library[sensor_type].append(sensor_data)

def get_tests_by_sensor(sensor_type: str, sensor_name: str):
    sensor = get_sensor(sensor_type, sensor_name)
    if sensor:
        return sensor.get("tests", [])
    return []

def get_test_results(sensor_name: str, sensor_type: str, test_name: str):
    result = random.randint(0, 2)

    if result == 0:
        return test_name, "In Progress", 0
    else:
        print("Получение результата теста:", test_name, "для сенсора:", sensor_name)
        try:
            result_value = get_result_by_name(sensor_type, sensor_name, test_name)
        except Exception as e:
            print(f"Ошибка в get_result_by_name: {e}")
            raise

        return test_name, "Success", result_value


def get_etalon_by_name(sensor_type: str, sensor_name: str, test_name: str):
    """
    Получает значение эталона для указанного теста по имени сенсора.
    """
    sensor = get_sensor(sensor_type, sensor_name)
    if sensor and "tests" in sensor:
        tests = sensor["tests"]
        if isinstance(tests, dict):  # Когда тесты представлены как словарь
            test_data = tests.get(test_name)
            if test_data and isinstance(test_data, tuple):
                return test_data[0]  # Возвращаем эталонное значение
        elif isinstance(tests, list):  # Когда тесты представлены как список
            for test in tests:
                if test_name in test:
                    # Проверяем, является ли значение теста кортежем
                    if isinstance(test[1], tuple):
                        return test[1][0]  # Первое значение — эталон
        return None  # Если тест не найден
    return None


def get_result_by_name(sensor_type: str, sensor_name: str, test_name: str):
    """
    Получает значение результата для указанного теста по имени сенсора.
    """
    sensor = get_sensor(sensor_type, sensor_name)
    if sensor and "tests" in sensor:
        tests = sensor["tests"]
        if isinstance(tests, dict):  # Когда тесты представлены как словарь
            test_data = tests.get(test_name)
            if test_data and isinstance(test_data, tuple):
                return test_data[1]  # Возвращаем значение результата
        elif isinstance(tests, list):  # Когда тесты представлены как список
            for test in tests:
                if test_name in test:
                    # Проверяем, является ли значение теста кортежем
                    if isinstance(test[1], tuple):
                        return test[1][1]  # Второе значение — результат
        return None  # Если тест не найден
    return None
