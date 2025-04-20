sensor_library = {

    # Из рабочего на данный момент тут только 2 пути для стерео и моно камеры в 1 сцену "Сцена №1"
    # К остальным датчикам надо править пути
    
    "camera": [
        {"name": "duo_minilx_lv1", "ros_pkg": "scenario_test_pkg", "launch_file": "duo_minilx_lv1.launch", "test_scene": "Стереокамера - Комплексная сцена", "image_topic": "/duo_minilx_lv1/left/image_raw", "config_file": "camera_configs/duo_minilx_lv1.yaml"},
        {"name": "mono_camera", "ros_pkg": "scenario_test_pkg", "launch_file": "scenario_mono_camera.launch", "test_scene": "Сцена №1", "image_topic":"/mono_camera/image_raw"},
        {"name": "depth_camera", "ros_pkg": "scenario_test_pkg", "launch_file": "scenario_1_test.launch", "test_scene": "Сцена №1", "image_topic":"/depth_camera/image_raw"}
    ],
    "tactile": [
        {"name": "Wacoh-Tech DynPick", "ros_launch": "test_scripts/launch_wacoh_dynpick.sh", "test_scene": "touch_scene"},
        {"name": "ATI nano 25 and AMTI HE6x6 force plate", "ros_launch": "test_scripts/launch_ati_nano25.sh", "test_scene": "touch_scene"},
        {"name": "Leptrino force/torque sensor", "ros_launch": "test_scripts/launch_leptrino.sh", "test_scene": "touch_scene"},
        {"name": "Nano17 6-axis force/torque sensors", "ros_launch": "test_scripts/launch_nano17.sh", "test_scene": "touch_scene"},
        {"name": "Interface to ATI NetFT sensor adapter", "ros_launch": "test_scripts/launch_ati_netft.sh", "test_scene": "touch_scene"},
        {"name": "Schunk LWA 3 Force Torque Controller based on ATI Mini 45", "ros_launch": "test_scripts/launch_schunk_lwa3.sh", "test_scene": "touch_scene"},
        {"name": "skin_driver", "ros_launch": "test_scripts/launch_skin_driver.sh", "test_scene": "touch_scene"}
    ],
    "rfid": [
        {"name": "UHF RFID Reader", "ros_launch": "test_scripts/launch_uhf_rfid.sh", "test_scene": "rfid_scene"},
        {"name": "Huxi RFID Reader", "ros_launch": "test_scripts/launch_huxi_rfid.sh", "test_scene": "rfid_scene"}
    ]
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