import subprocess
import datetime
from _datetime import date
 
#output = subprocess.check_output(['ps', 'aux']).decode('utf-8')

# пришлось генерировать строку
output = r"USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND"
output = output + chr(13) + r"root         1  300.3  0.0   4608  3648 pts/0    Ss   06:15   0:00 bash" 
output = output + chr(13) + r"root         7  100  0.7   8536  4256 pts/0    R+   06:15   0:00 ps aux"
output = output + chr(13) + r"test         8  101  0.1   8536  4256 pts/0    R+   06:15   0:00 ps aux"
 
lines = output.splitlines()

users = {}
proc = {}
cpu = 0
mem = 0

arr_cpu = {}
arr_mem = {}

cnt = 0

report = {}

report = 'Отчёт о состоянии системы:'

for line in lines:
    
    cnt = cnt + 1

    if cnt == 1:
        continue
    
    parts = line.split()
 
    user = parts[0]
    
    users.update({user: users.get(user, 0) + 1})
    
    cpu = cpu + float(parts[2])
    mem = mem + float(parts[3])

    arr_cpu.update({parts[1]: arr_cpu.get(parts[1], 0) + float(parts[2])})
    arr_mem.update({parts[1]: arr_mem.get(parts[1], 0) + float(parts[3])})
    
report = report + chr(13) + 'Пользователи системы:'
for i, users_elmnt in enumerate(users):
    report = report + chr(13) + users_elmnt

report = report + chr(13) + 'Процессов запущено:' + "   " + str(cnt - 1)

report = report + chr(13) + 'Пользовательских процессов:'
for i, users_elmnt in enumerate(users):
    report = report + chr(13) + users_elmnt + "   " + str(users.get(users_elmnt))

report = report + chr(13) + 'Всего CPU используется %:' + "  " + str(cpu)

print('Всего памяти используется %:' + "  " + str(mem))

top_cpu = dict(sorted(arr_cpu.items(), key=lambda x: x[1], reverse = True)[:1])
top_mem = dict(sorted(arr_mem.items(), key=lambda x: x[1], reverse = True)[:1])
report = report + chr(13) + 'Больше всего памяти использует:' + "  " + str(top_cpu)
report = report + chr(13) + 'Больше всего CPU использует:' + "  " + str(top_mem)

print(report)

with open('result_' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.txt', 'w') as my_file:
    my_file.writelines(report)
