class Book:
    material = 'plain paper'
    text = True

    def __init__(self, book_name, author, number_of_pages, isbn, is_reserved=False):
        self.book_name = book_name
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.is_reserved = is_reserved


def display_book(book):
    reserve_status = ', reserved' if book.is_reserved else ''
    print(f'Title: {book.book_name}, Author: {book.author}, '
          f'pages: {book.number_of_pages}, material: {book.material}{reserve_status}')


book_1 = Book('Idiot', 'Dostoevsky', 640, '978-0-306-40615-7', True)
book_2 = Book(
    'War and Peace', 'Tolstoy', 1225, '978-1-4028-9462-6')
book_3 = Book(
    'The Master and Margarita', 'Bulgakov', 384,
    '978-3-16-148410-0')
book_4 = Book('Anna Karenina', 'Tolstoy', 864,
              '978-0-14-311638-7', True)
book_5 = Book('Crime and Punishment', 'Dostoevsky', 672,
              '978-0-679-64198-2')


books = [book_1, book_2, book_3, book_4, book_5]

for single_book in books:
    display_book(single_book)
