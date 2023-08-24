import re
import json
import os

from itertools import chain

regex = r"(?P<ip>\S*).*\[(?P<date>\S*)\s+(?P<timezone>\S*)]\s+\"(?P<request_type>\S*)\s+(?P<url>\S*)\s+" \
        r"(?P<protocol>\S*)\"\s+(?P<status_code>\d*)\s+(?P<byte>[\d\-]*)\s\"(?P<referer_url>.*)\"\s+\"" \
        r"(?P<headers>.*)\"\s+(?P<duration>\d*)"

# файл с результатами работы
path_result = "log/result.json"
# каталогс файлами
path_log = "log"
# файл данных
filename_log = ""

# результат в формате json
result_json = {}
# кол-во запросов по типам
result_requests = {}
# запросы по ip
result_ip = {}
# максимально "долгие" запросы
result_time_max = []
# лог сервера
data_log = []

# вывод информации в файл
def write_file_json(path, json_file):
    with open(path, "w") as file:
        json.dump(json_file, file, indent = 4, ensure_ascii = False)

# считывание содержимого файла
def read_file(filename):
    with open(file = filename, mode = "r") as file:
        for f in file:
            yield f
            
# читаем каталог или определенный файл
for filelist in os.listdir(path_log):
    # читаем один файл
    if (filelist == filename_log or filename_log == '') and filelist.endswith(".log"):
        data_log = chain(data_log, read_file('log' + '/' + filelist))

# цикл по данным 
for i, arr_elmnt in enumerate(data_log, start = 1):
    
    # кол-во элементов
    cnt_req = i
    
    # парсим строку по шаблону регуляного выражения
    matches = re.search(regex, arr_elmnt)
    
    host_req = matches.group(1)
    date_req = matches.group(2)
    type_req = matches.group(4)
    url_req = matches.group(5)
    duration_req = int(matches.group(11))
    
    # типы запросов
    result_requests.update({type_req: result_requests.get(type_req, 0) + 1})

    # ip
    result_ip.update({host_req: result_ip.get(host_req, 0) + 1})

    value_for_max_duration = (duration_req, type_req, url_req, host_req, date_req)
    if len(result_time_max) < 3:
        result_time_max.append(value_for_max_duration)
    elif min_value_in_result_time_max[0] < duration_req:
        result_time_max[index_min_value] = value_for_max_duration

    result_time_max = sorted(result_time_max, key=lambda x: x[0], reverse=True)
    min_value_in_result_time_max = min(result_time_max, key=lambda x: x[0])
    index_min_value = result_time_max.index(min_value_in_result_time_max)

top_3_ip = dict(sorted(result_ip.items(), reverse = True)[:3])

result_json = {"count_requests":    {"name": "Общее количество запросов",       "value": cnt_req},
               "result_requests":   {"name": "Количество запросов по типу",     "value": result_requests},
               "top_3_ip":          {"name": "Топ 3 IP адресов",                "value": top_3_ip},
               "result_time_max":   {"name": "Топ 3 IP адресов",                "value": result_time_max}}

write_file_json(path_result, result_json)

print(result_json)
