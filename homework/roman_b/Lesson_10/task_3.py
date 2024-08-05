def choose_operation(func):

    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        return func(first, second, operation)
    return wrapper


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))


@choose_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return round(first / second, 3)
    elif operation == '*':
        return first * second
    else:
        print("Your numbers don't satisfy the criteria! ")


result = calc(first_number, second_number)
print(f"Your result is {result}")
