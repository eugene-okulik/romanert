import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
lesson_path = os.path.join(homework_path, 'eugene_okulik')
file_path = os.path.join(lesson_path, 'hw_13', 'data.txt')


def modify_dates():
    with open(file_path) as eugene_file:
        for line in eugene_file:
            parts = line.strip().split(' - ')
            initial_part, action = parts[0], parts[1]
            parts = initial_part.split()
            date_part = parts[1] + ' ' + parts[2]
            date_format = '%Y-%m-%d %H:%M:%S.%f'
            date = datetime.datetime.strptime(date_part, date_format)

            if 'на неделю позже' in action:
                new_date = date + datetime.timedelta(days=7)
                print(f'Original date: {date}, A week later: {new_date}')
            elif 'день недели' in action:
                day_of_week = date.strftime('%A')
                print(f'Original date: {date}, Day of the week: {day_of_week}')
            elif 'сколько дней назад' in action:
                today = datetime.datetime.now()
                days_ago = (today - date).days
                print(f'Original date: {date}, Days ago: {days_ago}')


modify_dates()
