class Flowers:
    def __init__(self, freshness, stem_length, price, lifetime):
        self.freshness = freshness
        self.stem_length = stem_length
        self.price = price
        self.lifetime = lifetime


class Roses(Flowers):
    def __init__(self, freshness, stem_length, price, lifetime, color):
        super().__init__(freshness, stem_length, price, lifetime)
        self.color = color


class Lilies(Flowers):
    def __init__(self, freshness, stem_length, price, lifetime, color):
        super().__init__(freshness, stem_length, price, lifetime)
        self.color = color


class Chrysanthemums(Flowers):
    def __init__(self, freshness, stem_length, price, lifetime, color):
        super().__init__(freshness, stem_length, price, lifetime)
        self.color = color


class Orchids(Flowers):
    def __init__(self, freshness, stem_length, price, lifetime, color):
        super().__init__(freshness, stem_length, price, lifetime)
        self.color = color


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, new_flower):
        self.flowers.append(new_flower)

    def total_cost(self):
        return f'The total cost of your bouquet is {sum(flower.price for flower in self.flowers)} shillings'

    def bouquet_lifetime(self):
        total_lifetime = sum(flower.lifetime for flower in self.flowers)
        return f'Your bouquet will last {total_lifetime / len(self.flowers)} days'

    def sort_flowers(self, attribute):
        return sorted(self.flowers, key=lambda flower: getattr(flower, attribute))

    def find_flowers_by_attribute(self, attribute, value):
        return (flower for flower in self.flowers if getattr(flower, attribute) == value)


my_bouquet = Bouquet()
my_bouquet.add_flower(Lilies(8, 60, 120, 8, 'yellow'))
my_bouquet.add_flower(Chrysanthemums(10, 40, 60, 10, 'purple'))
my_bouquet.add_flower(Orchids(6, 30, 195, 6, 'pink'))
my_bouquet.add_flower(Roses(7, 45, 100, 7, 'red'))

print(my_bouquet.bouquet_lifetime())
print(my_bouquet.total_cost())

sorted_by_price = my_bouquet.sort_flowers('price')
print('\n'"Flowers sorted by price:")
for flower in sorted_by_price:
    print(f'{type(flower).__name__}: Color={flower.color}, Price={flower.price}')

flowers_with_specific_lifetime = my_bouquet.find_flowers_by_attribute('lifetime', 8)
print('\n'''"Flowers with a lifetime of 8 days:")
for flower in flowers_with_specific_lifetime:
    print(f'{type(flower).__name__}: Color={flower.color}, Lifetime={flower.lifetime}')
