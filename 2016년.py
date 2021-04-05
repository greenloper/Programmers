a=5
b=24
day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(day[(sum(mon[:a - 1]) + b) % 7])