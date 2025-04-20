from math import gamma

data = ["Иван", "Вера", "Максим", "Елена"]

glasn = ["а", "у", "о", "и", "э", "ы", "я", "ю", "е", "ё"]

for name in data:
    if (name[1] in glasn) and not(name[len(name)-1] in glasn):
        print(name)