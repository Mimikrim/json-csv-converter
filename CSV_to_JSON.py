
import csv
import json
def common_file(filename_csv, filename_json, red_a, red_b):
    try:
        filename_csv = filename_csv.replace(".csv", "")
        csvfile = open(filename_csv + ".csv", 'r', encoding = "UTF-8")
    except:
        print("Не удалось открыть .csv файл")
        exit()
    reader = csv.DictReader(csvfile, delimiter = ";")
    out = json.dumps( [ row for row in reader ] )

    if red_a == None and red_b == None:
        red_a = ["[", "{", ",", "      {", "},", "}]"]
        red_b = ["[\n    ", "{\n      ", ",\n     ", "    {", "\n    },", "\n    }\n]"]
        print("Файл будет создан с редактированием по умолчанию")

    try:
        i = 0
        while i < len(red_a):
            out = out.replace(red_a[i], red_b[i])
            i += 1
    except:
        print("Редактирование не удалось")
        print("Файл будет создан без редактирования")


    try:
        filename_json = filename_json.replace(".json", "")
        with open(filename_json + ".json", 'w') as f:
            f.write(out)
        print("Файл .json создан")
    except:
        if (print("Файл .json создан")):
            None
        else:
            print("Ну удалось создать .json файл")
