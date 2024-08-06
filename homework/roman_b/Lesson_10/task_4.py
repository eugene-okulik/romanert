PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

price_dict = {item.split()[0]: int(item.split()[1].strip('р')) for item in PRICE_LIST.splitlines()}

print(price_dict)
