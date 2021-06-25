Здесь представлены функции для конвертации файлов в формате json в формат csv и csv в json.
На Pypi создана библиотека converter_json_to_csv_and_c_j(https://pypi.org/project/converter-json-to-csv-and-c-j/). Установить можно pip install converter-json-to-csv-and-c-j.

Код содержится в файле converter_json_to_csv_and_c_j.py

Содержимое приведённых ниже файлов можно посмотреть в папках files и test_files.

Функция json_to_csv_without_id может преобразовать файл common_json_file.json из папки files в файл test_common_json_file.csv из папки test_files.

Функция json_to_csv_without_id может преобразовать файл uncommon_json_file.json из папки files в файл test_uncommon_json_file.csv из папки test_files.

Функция json_to_csv_with_id может преобразовать файл File_with_attachments_with_ID.json из папки files в 2 файла File_with_attachments_with_ID.json и File_with_attachments_with_ID_names_of_animal_owners.csv из папки test_files.

Функция common_csv может преобразовать файл common_csv_file.csv из папки files в файл test_common_csv_file.json из папки test_files.

Функция csv_to_json_several_files может преобразовать 2 файла File_with_attachments_with_ID.json и File_with_attachments_with_ID_names_of_animal_owners.csv из папки files в файл test_several_csv_files.json из папки test_files.

Перед вызовом функций НУЖНО отдельно указать директорию в которой будет осуществлятся поиск файлов.
