# sensor_library.py

sensor_library = {
    "camera": [
        {"name": "stereo_camera", "ros_launch": "test_scripts/launch_stereo.sh", "test_scene": "scene1"},
        {"name": "mono_camera", "ros_launch": "test_scripts/launch_mono.sh", "test_scene": "scene1"},
        {"name": "depth_camera", "ros_launch": "test_scripts/launch_depth.sh", "test_scene": "scene1"}
    ],
    "tactile": [
        {"name": "simple_touch", "ros_launch": "test_scripts/launch_touch.sh", "test_scene": "touch_scene"},
        {"name": "multi_touch", "ros_launch": "test_scripts/launch_multi_touch.sh", "test_scene": "touch_scene"}
    ],
    "rfid": [
        {"name": "rfid_basic", "ros_launch": "test_scripts/launch_rfid.sh", "test_scene": "rfid_scene"},
        {"name": "rfid_long_range", "ros_launch": "test_scripts/launch_rfid_long.sh", "test_scene": "rfid_scene"}
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