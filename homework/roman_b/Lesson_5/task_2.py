output = [
    'operation result: 42',

    'operation result: 514',

    'program work result: 9'
]

for line in output:
    index = line.index(':') + 2
    number = int(line[index:])
    result = number + 10
    new_output = f'{line[:index]}{result}'
    print(new_output)
