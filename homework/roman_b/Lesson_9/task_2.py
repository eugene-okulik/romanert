temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
    22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

hot_days = list(filter(lambda x: x > 28, temperatures))

if hot_days:
    average_temp = round(sum(hot_days) / len(hot_days), 2)
    max_temp = max(hot_days)
    min_temp = min(hot_days)
    print(f'These are the hot days: {hot_days}')
    print(f'The average temperature on hot days is {average_temp} degrees')
    print(f'The highest temperature on hot days is {max_temp} degrees')
    print(f'The lowest temperature on hot days is {min_temp} degrees')
else:
    print("There are no hot days above 28 degrees!")
