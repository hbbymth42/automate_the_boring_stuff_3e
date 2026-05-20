import datetime

day = datetime.datetime.now()
day_delta = datetime.timedelta(days=1)

num_days = 0

while num_days < 11:
    if day.strftime('%A %d') == 'Friday 13':
        print(f'Friday 13th Found in {day.strftime('%B %Y')}.')
        num_days = num_days + 1
        day = day + day_delta
    else:
        day = day + day_delta
