import datetime

day = datetime.datetime.now()

day_delta = datetime.timedelta(days=1)

while day.strftime('%Y') != '0001':
    if day.strftime('%A %d') == 'Friday 13':
        print(f'Friday 13th Found in {day.strftime('%B %Y')}.')
        day = day - day_delta
    else:
        day = day - day_delta
