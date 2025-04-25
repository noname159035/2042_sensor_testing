from sensor_library import *

unic_tests = []

for elem in sensor_library:
    for camera in sensor_library[elem]:
        for test in camera["tests"]:
            if not(test in unic_tests):
                unic_tests.append(test)

print(unic_tests)

line = "{\n'article': '',\n'img_url': ''\n}"
for elem in unic_tests:
    print(f"'{elem}': " + line + ",")