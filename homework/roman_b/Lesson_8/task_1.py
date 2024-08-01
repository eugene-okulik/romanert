import random


def get_salary(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Enter only a whole number, no spaces')


salary = get_salary("What is your current salary per year? ")
bonus = bool(random.getrandbits(1))


def calc_bonus():
    if bonus:
        salary_updated = salary + random.randrange(100, 50001)
        return salary_updated
    else:
        return salary


print(f"{salary}, {bonus} - '${calc_bonus()}'")
