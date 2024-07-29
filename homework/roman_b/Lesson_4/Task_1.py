# Создание словаря

# Создайте словарь (и сохраните его в переменную my_dict) с такими ключами: ‘tuple’, ‘list’, ‘dict’, ‘set’.


my_dict = {
    'list': [7, 3.14, 'banana', None, 18, True],
    'tuple': (False, 812, 'chair', 2.117, 'last element'),
    'set': {2, 12, None, 'blue', 'red', True, 3.16, 12, 2},
    'dict': {'color': 'white', 'fruit': 'orange', 2: 12, 2.34: 'floating', 'boolean': True}
}

# Для того, что хранится под ключом ‘tuple’:
# выведите на экран последний элемент

my_tuple = my_dict['tuple']
print(my_tuple[-1])

# Для того, что хранится под ключом ‘list’:
# добавьте в конец списка еще один элемент
# удалите второй элемент списка

my_list = my_dict['list']
my_list.append('strawberry')
my_list.pop(1)
print(my_list)

# Для того, что хранится под ключом ‘dict’:
# добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент

my_dictionary = my_dict['dict']
my_dictionary['i am a tuple'] = 'Lie!'
my_dictionary.pop('color')
print(my_dictionary)

# Для того, что хранится под ключом ‘set’:
# добавьте новый элемент в множество
# удалите элемент из множества

my_set = my_dict['set']
my_set.add(12.43)
my_set.remove(12)
print(my_set)

print(my_dict)
