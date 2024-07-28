
# Даны 2 числа a и b. Получить их сумму, разность и произведение

def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('This is not a valid input! Enter an integer!')


a = get_integer('Please enter the first number: ')
b = get_integer('Please enter the second number: ')

sum_result = a + b
difference_result = a - b
product_result = a * b

print(f'The sum of your numbers is {sum_result}')
print(f'The difference between your numbers is {difference_result}')
print(f'The product of your numbers is {product_result}')
