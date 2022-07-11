from datetime import datetime, timedelta, timezone
from parse import parse
import matplotlib.pyplot as plt

file = 'C:/Users/shige/AppData/Local/VirtualStore/Windows/SysWOW64/mikatype.log'
file = './mikatype.log'
with open(file, mode='r', encoding='sjis') as f:
    lines = f.readlines()

x_data = []
y_data = []
sum = 0.0
dt_now = datetime.now()
for line in lines:
    split_line = line.split(' ')
    print(split_line[0])
    dt_date = datetime.strptime(split_line[0], '%y/%m/%d')
    date = (dt_date - dt_now).days
    time_dur = ''.join(split_line[4:])
    print(time_dur.rstrip())
    res = parse("{hour:d}時間{min:d}分{sec:d}秒", time_dur.rstrip())
    print(res)
    if res == None:
        print(split_line)
        res = parse("{min:d}分{sec:d}秒", time_dur.rstrip())
        time = res["min"]+res["sec"]/60.0
    else:
        time = 60*res["hour"]+res["min"]+res["sec"]/60.0

    sum += time
    x_data.append(date)
    y_data.append(sum)

print(x_data)
print(y_data)

plt.plot(x_data, y_data)
plt.show()
