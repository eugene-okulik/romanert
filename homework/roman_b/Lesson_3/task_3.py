
# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел

import math


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('This is not a valid input! Enter an integer!')


first_number = get_integer('Please enter the first number: ')
second_number = get_integer('Please enter the second number: ')

arithmetic_mean = (first_number + second_number) / 2

geometric_mean = math.sqrt(first_number * second_number)

print(f'The arithmetic value of your numbers is: {arithmetic_mean}')
print(f'The geometric value of your numbers is: {geometric_mean}')
