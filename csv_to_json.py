
import csv
import json

def common_csv(filename_csv, filename_json, red_a, red_b, delimiter):
    try:
        filename_csv = filename_csv.replace(".csv", "")
        csvfile = open(filename_csv + ".csv", 'r', encoding = "UTF-8")
    except:
        print("Не удалось открыть .csv файл")
        exit()
    reader = csv.DictReader(csvfile, delimiter = delimiter)
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

def csv_to_json_several_files(filenames_csv, identifiers, filename_json, delimiter):
    file = 0
    while file < len(filenames_csv):
        try:
            filenames_csv[file] = filenames_csv[file].replace(".csv", "")
            csvfile = open(filenames_csv[file] + ".csv", 'r', encoding = "UTF-8")
        except:
            print("Не удалось открыть .csv файл")
            exit()
        reader = csv.DictReader(csvfile, delimiter = delimiter)
        out = json.dumps([ row for row in reader ])

        
        if file == 0:
            red_a = ['{', '",', '}, {\n            ', '[',': ']
            red_b = ['{\n            ', '",\n           ', '\n        },\n        {\n            ', '{\n    "' + identifiers[file] + '":[\n        ', ' : ']

            if len(filenames_csv) == 1:
                red_a.append('}]')
                red_b.append('\n        }\n    ]\n}')

            else:
                red_a.append('}]')
                red_b.append('\n        }\n    ],\n')

            try:
                i = 0
                while i < len(red_a):
                    out = out.replace(red_a[i], red_b[i])
                    i += 1
            except:
                print("Редактирование не удалось")
                print("Файл будет создан без редактирования")

        if file != 0:
            red_a = ['{', '",', '}, {\n            ', '[',': ']
            red_b = ['{\n            ', '",\n           ', '\n        },\n        {\n            ', '    "' + identifiers[file] + '":[\n        ', ' : ']

            if file == (len(filenames_csv) - 1):
                red_a.append('}]')
                red_b.append('\n        }\n    ]\n}')

            else:
                red_a.append('}]')
                red_b.append('\n        }\n    ],\n')
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
            if file == 0:
                with open(filename_json + ".json", "w") as f:
                    f.write(out)
                print("Файл .json создан")
            else:
                with open(filename_json + ".json", "a") as f:
                    f.write(out)
                print("Файл .json дописан")
        except:
            if (print("Файл .json создан")):
                None
            else:
                print("Ну удалось создать .json файл")
        file += 1