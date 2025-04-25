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
                "Точность стерео-глубины (%)": (10,  9),
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
                "Оценка Фокуса и Глубины Резкости (DoF, м)": (4, 3.9)
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
                "Точность стерео-глубины (%)": (8, 7),
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
                "Точность стерео-глубины (%)":          (8,     7),
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
                "Точность стерео-глубины (%)":               (5.0,    6.0),
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

modal_data = {
    "sensors": {
        'Тест на угол обзора': {
            'article': 'Измеряет фактический угол поля зрения камеры и сравнивает его с заявленным, проверяя способность охвата сцены по горизонтали и вертикали.',
            'img_url': 'type\\Тест на угол обзора.png'
        },
        'Точность стерео-глубины (%)': {
            'article': 'Оценивает, насколько точно стереокамера вычисляет расстояние до объектов, сравнивая рассчитанную глубину с их истинным положением.',
            'img_url': 'type\\Точность стерео-глубины (%).png'
        },
        'Параллакс (коэффициент p=B·F/Z)': {
            'article': 'Проверяет зависимость параллакса (сдвига изображения между двумя камерами) от расстояния, используя формулу p = B·F/Z.',
            'img_url': 'type\\Параллакс (коэффициент p=B·F/Z).png'
        },
        'Разница погрешностей гладкий/текстурный (%)': {
            'article': 'Сравнивает относительную погрешность измерения глубины перед гладкой и текстурной поверхностями, чтобы оценить влияние текстуры фона.',
            'img_url': 'type\\Разница погрешностей гладкий/текстурный (%).png'
        },
        'MSE (Среднекв. ошибка карты глубины)': {
            'article': 'Вычисляет среднеквадратичную ошибку между эталонной картой глубины и тестовой, оценивая шум и артефакты.',
            'img_url': 'type\\MSE (Среднекв. ошибка карты глубины).png'
        },
        'Тест на разрешение': {
            'article': 'Проверяет способность камеры различать мелкие объекты, оценивая число пикселей, на которых видна минимальная деталь.',
            'img_url': 'type\\Тест на разрешение.png'
        },
        'Оценка Фокуса и Глубины Резкости (DoF, м)': {
            'article': 'Измеряет конкретные значения ближней и дальней границ глубины резкости в метрах при заданном фокусном расстоянии.',
            'img_url': 'type\\Оценка Фокуса и Глубины Резкости (DoF, м).png'
        },
        'Тест на точность глубины': {
            'article': 'Проверяет абсолютную и относительную погрешность глубинных измерений моно-камеры или глубинного сенсора.',
            'img_url': 'type\\Тест на точность глубины.png'
        },
        'Определение разрешающей способности камеры': {
            'article': 'Оценивает минимальное расстояние между объектами, при котором камера все еще различает их как отдельные глубинные пятна.',
            'img_url': 'type\\Определение разрешающей способности камеры.png'
        },
        'Тест на оценку пиковой силы': {
            'article': 'Измеряет максимальную силу, которую может корректно зафиксировать датчик, и сравнивает с эталонным значением.',
            'img_url': 'type\\Тест на оценку пиковой силы.png'
        },
        'Тест на точность момента': {
            'article': 'Проверяет погрешность измерения момента сил датчиком, сравнивая измеренные значения с известными нагрузками.',
            'img_url': 'type\\Тест на точность момента.png'
        },
        'Тест на дрейф и шум': {
            'article': 'Оценивает стабильность показаний датчика во времени, измеряя дрейф нуля и уровень шумовых флуктуаций.',
            'img_url': 'type\\Тест на дрейф и шум.png'
        },
        'Тест на диапазон измерений': {
            'article': 'Определяет минимальное и максимальное измеряемые значения датчика, проверяя соответствие спецификации.',
            'img_url': 'type\\Тест на диапазон измерений.png'
        },
        'Тест на диапазон измерений силы': {
            'article': 'Проверяет рабочий диапазон силового датчика, фиксируя начало и конец стабильных измерений.',
            'img_url': 'type\\Тест на диапазон измерений силы.png'
        },
        'Определение максимальной дальности считывания': {
            'article': 'Находит максимальное расстояние, на котором RFID-ридер сохраняет ≥95% успешных считываний.',
            'img_url': 'type\\Определение максимальной дальности считывания.png'
        },
        'Тестирование угла считывания': {
            'article': 'Измеряет процент успешных считываний RFID-меток при разных углах поворота относительно ридера.',
            'img_url': 'type\\Тестирование угла считывания.png'
        },
        'Массовое считывание RFID-меток': {
            'article': 'Оценивает время и долю успешно считанных меток при одновременной работе множества меток.',
            'img_url': 'type\\Массовое считывание RFID-меток.png'
        },
        'Определение минимального расстояния надежного считывания(м)': {
            'article': 'Фиксирует минимальное расстояние, при котором RFID-ридер стабильно читает метку в 100% случаев.',
            'img_url': 'type\\Определение минимального расстояния надежного считывания(м).png'
        },
        'Определение эффективного угла обзора': {
            'article': 'Определяет максимальный угол, при котором RFID-ридер сохраняет высокий процент успешных считываний.',
            'img_url': 'type\\Определение эффективного угла обзора.png'
        },
        'Процент успешных считываний при 0, 30, 45, 60, 90°': {
            'article': 'Публикует результаты процентного успешного считывания RFID-меток на различных углах.',
            'img_url': 'type\\Процент успешных считываний при 0, 30, 45, 60, 90°.png'
        },
        'Минимальный угол с успешными считываниями >90%': {
            'article': 'Указывает наименьший угол, при котором ридер обеспечивает ≥90% успешных считываний.',
            'img_url': 'type\\Минимальный угол с успешными считываниями >90%.png'
        },
    },
    "type": {
        "camera": {
            "article": "Объектив фокусирует свет на светочувствительный CMOS/CCD-сенсор, который преобразует его в цифровой сигнал. Процессор камеры затем корректирует цвет, убирает шум и сохраняет изображение.",
            "img_url": "type\\camera.jpg",
        },
        "tactile": {
            "article": "Тактильные датчики преобразуют механическое давление или деформацию поверхности в электрические сигналы: в резистивных типах нагрузка изменяет сопротивление, в ёмкостных – меняет ёмкость между электродами, в пьезоэлектрических – генерируется напряжение при деформации кристалла, а в оптических – изменяется светопроводимость внутри волокна; считав эти изменения, электроника определяет силу и место контакта.",
            "img_url": "type\\tactile.jpg",
        },
        "rfid": {
            "article": "RFID-система состоит из метки и считывателя: считыватель излучает радиочастотное поле, метка, попав в него, получает энергию (пас­сивная метка) или использует собственный источник питания (активная), активирует микрочип и модулирует (бэк­скаттерингом) отражённый сигнал с закодированным уникальным ID; считыватель улавливает эту модуляцию и декодирует данные, определяя идентификатор и, при необходимости, дополнительную информацию (датчики, память и т. д.).",
            "img_url": "type\\rfid.jpg",
        }
    }
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
