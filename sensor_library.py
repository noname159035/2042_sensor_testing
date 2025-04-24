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
                "Тест на точность стерео-глубины": (10,  9),
                "Параллакс (коэффициент p=B·F/Z)": (2.25,    2.20),
                "Разница погрешностей гладкий/текстурный (%)": (15.00,   12.00),
                "MSE (Среднекв. ошибка карты глубины)": (0.02,    0.015)
            }
        },
        {
            "name": "mono_camera",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "scenario_mono_camera.launch",
            "test_scene": "Сцена №1",
            "image_topic":"/mono_camera/image_raw",
            "tests": {
                "Тест на угол обзора": (75.4, 75.4),
                "Тест на разрешение": ("640×480",    "640×480"),
                "Оценка Фокуса и Глубины Резкости (DoF)": (4, 3.9)
            }
        },
        {
            "name": "uvc_camera",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "scenario_uvc_camera.launch",
            "test_scene": "Сцена №1",
            "image_topic": "/uvc_camera/image_raw",
            "tests": {
                "Тест на угол обзора": (60.0, 58.0),
                "Тест на разрешение": ("640×480", "640×480"),
                "Оценка Фокуса и Глубины Резкости (DoF, м)": (0.586, 0.603)
            }
        },
        {
            "name": "matrixvision_bluefox",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "scenario_bluefox_camera.launch",
            "test_scene": "Сцена №1",
            "image_topic": "/matrixvision_bluefox/image_raw",
            "tests": {
                "Тест на угол обзора": (60.0, 58.0),
                "Тест на разрешение": ("640×480", "640×480"),
                "Оценка Фокуса и Глубины Резкости (DoF, м)": (0.586, 0.603)
            }
        },
        {
            "name": "occam_omni_mono",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "occam_omni_mono.launch",
            "test_scene": "Сцена №1",
            "image_topic": "/occam_omni_mono/image_raw",
            "tests": {
                "Тест на угол обзора": (90.0, 88.0),
                "Тест на разрешение": ("1280×720", "1280×720"),
                "Оценка Фокуса и Глубины Резкости (DoF, м)": (0.432, 0.438)
            }
        },
        {
            "name": "trifo_ironsides",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "trifo_ironsides_mono.launch",
            "test_scene": "Сцена №1",
            "image_topic": "/trifo_ironsides/image_raw",
            "tests": {
                "Тест на угол обзора": (67.0, 53.0),
                "Тест на разрешение": ("1920×1080", "1920×1080"),
                "Оценка Фокуса и Глубины Резкости (DoF, м)": (0.963, 0.957)
            }
        },
        {
            "name": "usb_cam",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "usb_cam.launch",
            "test_scene": "Сцена №1",
            "image_topic": "/usb_cam/image_raw",
            "tests": {
                "Тест на угол обзора": (60.0, 58.0),
                "Тест на разрешение": ("640×480", "640×480"),
                "Оценка Фокуса и Глубины Резкости (DoF, м)":    (0.586, 0.593)
            }
        },
        {
            "name": "wge100_camera",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "wge100_camera.launch",
            "test_scene": "Сцена №1",
            "image_topic": "/wge100_camera/image_raw",
            "tests": {
                "Тест на угол обзора": (60.0,       60.0),
                "Тест на разрешение": ("1280×720", "1280×720"),
            }
        },

        {
            "name": "videre_stereo_cam",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "videre_stereo_cam.launch",
            "test_scene": "Стереокамера - Комплексная сцена",
            "image_topic": "/videre_stereo_cam/left/image_raw",
            "config_file": "camera_configs/videre_stereo_cam.yaml",
            "tests": {
                "Тест на угол обзора":                         (60.0,   58.0),
                "Точность стерео-глубины (%)":                 (5.0,    6.0),
                "Параллакс (коэффициент p=B·F/Z)":              (2.25,   2.10),
                "Разница погрешностей гладкий/текстурный (%)":  (15.0,   12.0),
                "MSE (Среднекв. ошибка карты глубины)":         (0.02,   0.015)
            }
        },

        {
            "name": "gevicam_stereo",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "gevicam_stereo.launch",
            "test_scene": "Стереокамера - Комплексная сцена",
            "image_topic": "/gevicam_stereo/left/image_raw",
            "config_file": "camera_configs/gevicam_stereo.yaml",
            "tests": {
                "Тест на угол обзора": (75, 74),
                "Тест на точность стерео-глубины (%)": (8, 7),
                "Параллакс (коэффициент p=B·F/Z)": (2.25, 2.22),
                "Разница погрешностей гладкий/текстурный (%)": (15.00, 10.00),
                "MSE (Среднекв. ошибка карты глубины)": (0.02, 0.012)
            }
        },
        {
            "name": "occam_omni_stereo",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "occam_omni_stereo.launch",
            "test_scene": "Стереокамера - Комплексная сцена",
            "image_topic": "/occam_omni_stereo/left/image_raw",
            "config_file": "camera_configs/occam_omni_stereo.yaml",
            "tests": {
                "Тест на угол обзора":                         (90,    88),
                "Тест на точность стерео-глубины (%)":          (8,     7),
                "Параллакс (коэффициент p=B·F/Z)":               (2.25,  2.20),
                "Разница погрешностей гладкий/текстурный (%)":   (15.00, 12.00),
                "MSE (Среднекв. ошибка карты глубины)":          (0.02,  0.012)
            }
        },
        {
            "name": "bumblebee2",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "bumblebee2.launch",
            "test_scene": "Стереокамера - Комплексная сцена",
            "image_topic": "/bumblebee2/left/image_raw",
            "config_file": "camera_configs/bumblebee2.yaml",
            "tests": {
                "Тест на угол обзора":                         (62.0,   60.5),
                "Точность стерео-глубины (%)":                 (5.0,    4.2),
                "Параллакс (коэффициент p=B·F/Z)":              (2.25,   2.10),
                "Разница погрешностей гладкий/текстурный (%)":  (15.0,   11.5),
                "MSE (Среднекв. ошибка карты глубины)":         (0.02,   0.017)
            }
        },
        {
            "name": "chameleon",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "chameleon.launch",
            "test_scene": "Стереокамера - Комплексная сцена",
            "image_topic": "/chameleon/left/image_raw",
            "config_file": "camera_configs/chameleon.yaml",
            "tests": {
                "Тест на угол обзора":                              (60,     58),
                "Тест на точность стерео-глубины (%)":               (5.0,    6.0),
                "Параллакс (коэффициент p=B·F/Z)":                    (2.25,   2.10),
                "Разница погрешностей гладкий/текстурный (%)":        (15.0,   13.0),
                "MSE (Среднекв. ошибка карты глубины)":               (0.02,   0.018)
            }
        },

        {
            "name": "depth_camera",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "scenario_1_test.launch",
            "test_scene": "Сцена №1",
            "image_topic":"/depth_camera/image_raw",
            "tests": {
                "Тест на угол обзора": (75, 73),
                "Тест на точность глубины": (3, 4),
                "Определение разрешающей способности камеры": ("5 см", "6 см")
            }
        }
    ],
    "tactile": [
        {
            "name": "Wacoh-Tech DynPick",
            "ros_launch": "test_scripts/launch_wacoh_dynpick.sh",
            "test_scene": "touch_scene",
            "tests": {
                "Тест на оценку пиковой силы": (1000, 990),
                "Тест на точность момента": ('0.09', '0.09'),
                "Тест на дрейф и шум": ('Стабильно', 'Стабильно'),
                "Тест на диапазон измерений": ('200-1000', '230-990')
            }
        },
        {
            "name": "ATI nano 25",
            "ros_launch": "test_scripts/launch_ati_nano25.sh",
            "test_scene": "touch_scene",
            "tests": {
                "Тест на оценку пиковой силы": (125, 120),
                "Тест на точность момента": ('0.3', '0.3'),
                "Тест на дрейф и шум": ('Стабильно', 'Стабильно'),
                "Тест на диапазон измерений": ('1/24-125', '0-125')
            }
        },
        {
            "name": "AMTI HE6x6 force plate",
            "ros_launch": "test_scripts/launch_leptrino.sh",
            "test_scene": "touch_scene",
            "tests": {
                "Тест на оценку пиковой силы": (89, 90),
                "Тест на дрейф и шум": ('Стабильно', 'Стабильно'),
                "Тест на диапазон измерений силы": ('4.4-89', '4-90')
            }
        },
        {
            "name": "Leptrino force/torque sensor",
            "ros_launch": "test_scripts/launch_leptrino.sh",
            "test_scene": "touch_scene",
            "tests": {
                "Тест на оценку пиковой силы": (100, 110),
                "Тест на дрейф и шум": ('Стабильно', 'Стабильно'),
                "Тест на диапазон измерений": ('1/2000-100', '1/1500-100')
            }
        },
        {
            "name": "Nano17 6-axis force/torque sensors",
            "ros_launch": "test_scripts/launch_nano17.sh",
            "test_scene": "touch_scene",
            "tests": {
                "Тест на оценку пиковой силы": (50, 49),
                "Тест на точность момента": ('0.08', '0.08'),
                "Тест на дрейф и шум": ('Стабильно', 'Стабильно'),
                "Тест на диапазон измерений": ('0-50', '0-50')
            }
        },
        {
            "name": "Schunk LWA 3 Force Torque Controller based on ATI Mini 45",
            "ros_launch": "test_scripts/launch_schunk_lwa3.sh",
            "test_scene": "touch_scene",
            "tests": {
                "Тест на оценку пиковой силы": (800, 800),
                "Тест на точность момента": ('0.1', '0.1'),
                "Тест на дрейф и шум": ('Стабильно', 'Стабильно'),
                "Тест на диапазон измерений": ('0-800', '100-800')
            }
        }
    ],

    "rfid": [
        {
            "name": "UHF RFID Reader",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "scenario_rfid_angle_test.launch",
            "test_scene": "rfid",
            "tests": {
                "Определение максимальной дальности считывания": (7.5, 7.2),
                "Тестирование угла считывания": (45, 43),
                "Массовое считывание RFID-меток": ("5 с/7.3%", "5.2 с/96.0%"),
                "Определение минимального расстояния надежного считывания(м)": (0.15, 0.18)
            }
        },
        {
            "name": "Huxi RFID Reader",
            "ros_pkg": "scenario_test_pkg",
            "launch_file": "scenario_rfid_angle_test.launch",
            "test_scene": "rfid",
            "tests": {
                "Определение эффективного угла обзора": (45,  43),
                "Процент успешных считываний при 0, 30, 45, 60, 90°": (90, 87),
                "Минимальный угол с успешными считываниями >90%": (0,   0)
            }
        }
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

def get_test_results(test_name: str):
    result = random.randint(0, 2);


    if result == 0:
        return (test_name, "In Progress", 0)
    else:
        return (test_name, "Success", result_data[test_name])
    # else:
    #     return (test_name, "Fail", "Ошибка")