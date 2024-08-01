import sys

sys.set_int_max_str_digits(21000)


def fibonacci(limit=1000000):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


fib = fibonacci()

number_5 = None
number_200 = None
number_1000 = None
number_100000 = None

for i, num in enumerate(fib):
    if i == 4:
        number_5 = num
    elif i == 199:
        number_200 = num
    elif i == 999:
        number_1000 = num
    elif i == 99999:
        number_100000 = num
        break


print(f"5th number: {number_5}")
print(f"200th number: {number_200}")
print(f"1000th number: {number_1000}")
print(f"100000th number: {number_100000}")
