sensor_library = {
    "camera": [
        {"name": "stereo_camera", "ros_launch": "test_scripts/launch_stereo.sh", "test_scene": "scene1"},
        {"name": "mono_camera", "ros_launch": "test_scripts/launch_mono.sh", "test_scene": "scene1"},
        {"name": "depth_camera", "ros_launch": "test_scripts/launch_depth.sh", "test_scene": "scene1"}
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
        ['Тестирвание угла обзора'],
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