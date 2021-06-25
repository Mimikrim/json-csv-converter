import json
import csv

def json_to_csv_without_id(columns, filename_json, filename_csv, delimiter):
    filename_json = filename_json.replace(".json","")
    filename_csv = filename_csv.replace(".csv","")
    # Открываем файл формата .json и помещаем в словарь python считанную из него информацию
    try:
        with open(filename_json, mode = "r", encoding = "UTF-8") as json_file:
                data = json.load(json_file)
    except:
        print("Не удалось открыть .json файл")
        exit()
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
        with open(filename_csv, mode = "w", encoding = "UTF-8") as csv_file:
            file_writer = csv.writer(csv_file, delimiter = delimiter, lineterminator = "\r")
            file_writer.writerow(columns)
    except:
        print("Не удалось создать .csv файл")
        exit()
    i = 0
    while i < len_array:
        array_worlds = array_str_data[i].split(",")
        file_writer.writerow(array_worlds)
        i += 1

def json_to_csv_with_id(identifiers, filename_json, filename_csv,  delimiter):

    filename_json = filename_json.replace(".json","")
    filename_csv = filename_csv.replace(".csv","") + "_"
    # Открываем файл формата .json и помещаем в словарь python считанную из него информацию
    try:
        with open (filename_json + ".json", "r") as json_file:
            data = json.load(json_file)
    except:
        print("Не удалось открыть .json файл")
        exit()

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
        except:
            print("Не удалось создать .csv файл")
            exit()
        i += 1
