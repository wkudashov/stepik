import datetime

i = list(map(int, input().split()))
date = datetime.date(i[0], i[1], i[2]) + datetime.timedelta(days=int(input()))

print(date.year, date.month, date.day)
