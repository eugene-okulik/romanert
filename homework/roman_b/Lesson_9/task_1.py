import datetime

my_time = "Jan 15, 2023 - 12:05: 33"

try:
    python_date = datetime.datetime.strptime(my_time, '%b %d, %Y - %H:%M:%S')
    print(python_date.strftime('%B'))
    print(python_date.strftime('%d.%m.%Y, %H:%M'))
except ValueError as e:
    print(f'Unable to parse the date: {e}')
