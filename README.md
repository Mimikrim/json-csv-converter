Здесь представлены функции для конвертации файлов в формате json в формат csv и csv в json.
На Pypi создана библиотека converter_json_to_csv_and_c_j(https://pypi.org/project/converter-json-to-csv-and-c-j/). Установить можно pip install converter-json-to-csv-and-c-j. 

Функция json_to_csv_without_id может преобразовать файлы формата json:
[
{
    "ID" : "001",
    "name" : "Jim",
    "animal ID" : "001",
    "animal" : "cat",
    "service" : "treatment"
},
{
    "ID" : "002",
    "name" : "Fred",
    "animal ID" : "003",
    "animal" : "dog",
    "service" : "treatment"
},
{
    "ID" : "003",
    "name" : "Bob",
    "animal ID" : "003",
    "animal" : "dog",
    "service" : "overseas animal"
    
},
{
    "ID" : "004",
    "name" : "Jil",
    "animal ID" : "003",
    "animal" : "dog",
    "service" : "overseas animal"
}
]
в формат csv:
ID;name;animal ID;animal;service
001;Jim;001;cat;treatment
002;Fred;003;dog;treatment
003;Bob;003;dog;overseas
004;Jil;003;dog;overseas
.