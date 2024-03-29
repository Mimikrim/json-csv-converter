import json
import csv

class js:
    
    def json_to_csv_without_id(columns, filename_json, filename_csv, delimiter):

        filename_json = filename_json.replace(".json","")
        filename_csv = filename_csv.replace(".csv","")
        # Открываем файл формата .json и помещаем в словарь python считанную из него информацию
        try:
            with open(filename_json + ".json", mode = "r", encoding = "UTF-8") as json_file:
                    data = json.load(json_file)
        except FileNotFoundError:
            raise FileNotFoundError("JSON-файл не найден")
        except Exception as e:
            raise Exception(f"Ошибка при чтении JSON-файла: {e}")
        # Работаем с будущими именами столбцов файла .csv
        col = []
    
        i = 0
        while i < len(columns):
            col.append("")
            i += 1
        id = False
        i = 0
    
        while i < len(columns):
            words = columns[i]
            j = 0
            word = ""
            while j < len(columns[i]):
                if words[j] == "/":
                    word = ""
                    id = True
                else:
                    word = word + words[j]
                j += 1
            col[i] = word
            i += 1
        if id == False:
            col = columns
        # Преобразование словаря в строку
        str_data = str(data)
        # Редактирование строки
        tran = str.maketrans(dict.fromkeys(list("[]'{:  "), ""))
        str_data = str_data.translate(tran)
        str_data = str_data.replace("},", " ")
        str_data = str_data.replace("}", "")

        i = 0
        len_сolumns = len(col)
        while i < len_сolumns:
            str_data = str_data.replace(col[i], "")
            i += 1
        # Преобразование одной строки в массив нескольких строк
        array_str_data = str_data.split()
        len_array = len(array_str_data)
        # Запись в файл формата .csv
        try:
            with open(filename_csv + ".csv", mode = "w", encoding = "UTF-8") as csv_file:
                file_writer = csv.writer(csv_file, delimiter = delimiter, lineterminator = "\r")
                file_writer.writerow(columns)
                i = 0
                while i < len_array:
                    array_worlds = array_str_data[i].split(",")
                    file_writer.writerow(array_worlds)
                    i += 1
        except Exception as e:
            raise Exception(f"Ошибка при записи в CSV-файл: {e}")

    def json_to_csv_with_id(identifiers, filename_json, filename_csv,  delimiter):

        filename_json = filename_json.replace(".json","")
        filename_csv = filename_csv.replace(".csv","") + "_"
        # Открываем файл формата .json и помещаем в словарь python считанную из него информацию
        try:
            with open (filename_json + ".json", "r") as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            raise FileNotFoundError("JSON-файл не найден")
        except Exception as e:
            raise Exception(f"Ошибка при чтении JSON-файла: {e}")

        i = 0
        # В цикле один файл формата .json конвертируется в несколько файлов в формате .csv по указанными идентификаторам
        while i < len(identifiers):
            ids = data[identifiers[i]]
            try:
                with open (filename_csv + identifiers[i] + ".csv", "w", newline = "") as csv_file:
                    fieldnames = ids[0].keys()
                    writer = csv.DictWriter(csv_file, delimiter = delimiter, fieldnames = fieldnames)
                    writer.writeheader()
                    for id in ids:
                        writer.writerow(id)
            except Exception as e:
                raise Exception(f"Ошибка при записи в CSV-файл: {e}")
            i += 1

class cs:

    def common_csv(filename_csv, filename_json, red_a, red_b, delimiter):
        # Открываем файл формата .csv
        try:
            filename_csv = filename_csv.replace(".csv", "")
            csvfile = open(filename_csv + ".csv", 'r', encoding = "UTF-8")
        except FileNotFoundError:
            raise FileNotFoundError("CSV-файл не найден")
        except Exception as e:
            raise Exception(f"Ошибка при чтении CSV-файла: {e}")

        # Преобразуем информацию из переменной csvfile формата csv в одну строку
        reader = csv.DictReader(csvfile, delimiter = delimiter)
        out = json.dumps( [ row for row in reader ] )
        # Используемые параметры редактирования, если они не заданы при вызове функции 
        if red_a == None and red_b == None:
            red_a = ["[", "{", ",", "      {", "},", "}]"]
            red_b = ["[\n    ", "{\n      ", ",\n     ", "    {", "\n    },", "\n    }\n]"]
            print("Файл будет создан с редактированием по умолчанию")
        # Применение параметров редактирования
        try:
            i = 0
            while i < len(red_a):
                out = out.replace(red_a[i], red_b[i])
                i += 1
        except Exception as e:
            print(f"Редактирование не удалось: {e}")

        # Создание файла в формате .json и запись в него обработанной информации
        try:
            filename_json = filename_json.replace(".json", "")
            with open(filename_json + ".json", 'w') as f:
                f.write(out)
            print("Файл .json создан")
        except Exception as e:
            print(f"Ошибка при записи в JSON-файл: {e}")

    def csv_to_json_several_files(filenames_csv, identifiers, filename_json, delimiter):
        # Переменная kol_file это количество преобразуемых csv файлов в файл json
        kol_file = 0
        while kol_file < len(filenames_csv):
            # Открытие файла в формате .csv
            try:
                filenames_csv[kol_file] = filenames_csv[kol_file].replace(".csv", "")
                csvfile = open(filenames_csv[kol_file] + ".csv", 'r', encoding = "UTF-8")
            except FileNotFoundError:
                print(f"CSV-файл '{filenames_csv[kol_file]}' не найден.")
                continue
            except Exception as e:
                raise Exception(f"Ошибка при чтении CSV-файла: {e}")

            # Преобразуем информацию из переменной csvfile формата csv в одну строку    
            reader = csv.DictReader(csvfile, delimiter = delimiter)
            out = json.dumps( [ row for row in reader ] )
            # Редактирование информации
            if kol_file == 0:
                red_a = ['{', '",', '}, {\n            ', '[',': ']
                red_b = ['{\n            ', '",\n           ', '\n        },\n        {\n            ', '{\n    "' + identifiers[kol_file] + '":[\n        ', ' : ']

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
                except Exception as e:
                    print(f"Редактирование не удалось: {e}")

            if kol_file != 0:
                red_a = ['{', '",', '}, {\n            ', '[',': ']
                red_b = ['{\n            ', '",\n           ', '\n        },\n        {\n            ', '    "' + identifiers[kol_file] + '":[\n        ', ' : ']
                
                if kol_file == (len(filenames_csv) - 1):
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
                except Exception as e:
                    print(f"Редактирование не удалось: {e}")

            try:
                filename_json = filename_json.replace(".json", "")
                # Создание файла в формате .json и запись в него обработанной информации
                if kol_file == 0:
                    with open(filename_json + ".json", "w") as f:
                        f.write(out)
                    print("Файл .json создан")
                else:
                # Дозапись в файл в формата .json обработанной информации    
                    with open(filename_json + ".json", "a") as f:
                        f.write(out)
                    print("Файл .json дописан")
            except Exception as e:
                print(f"Ошибка при записи в JSON-файл: {e}")
            kol_file += 1
