output = [
    'operation result: 42',
    'operation result: 514',
    'program work result: 9',
    'result: 2'
]


# First option using indexes
def update_results():
    for line in output:
        index = line.index(':') + 2
        print(f'{line[:index]}{int(line[index:]) + 10}')


update_results()


# Second option using split()
def update_results_2():
    for line in output:
        parts = line.split(':')
        print(f'{parts[0]}: {int(parts[1].strip()) + 10}')


update_results_2()
