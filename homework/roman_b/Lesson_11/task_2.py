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


class TextBook(Book):

    def __init__(self, book_name, author, number_of_pages, isbn, subject,
                 school_grade, is_reserved=False, is_homework=True):
        super().__init__(book_name, author, number_of_pages, isbn, is_reserved)
        self.subject = subject
        self.school_grade = school_grade
        self.is_homework = is_homework


def display_textbook(textbook):
    reserve_status = ', reserved' if textbook.is_reserved else ''
    print(f'Title: {textbook.book_name}, Author: {textbook.author}, '
          f'pages: {textbook.number_of_pages}, subject: {textbook.subject}, '
          f'grade: {textbook.school_grade}{reserve_status}')


algebra = TextBook('Algebra', 'Ivanov', 215,
                   '978-1-4028-1462-6', 'Math', 9)
physics = TextBook('Wonderful Physics', 'Smith',
                   320, '918-1-4028-9412-6', 'Physics', 10)
history = TextBook('Amazing History', 'Johnson', 199,
                   '778-1-4028-9462-3', 'History', 8)
biology = TextBook('Secrets of Biology', 'Davis',
                   281, '978-3-4028-9462-6', 'Biology', 10, True)


textbooks = [algebra, physics, history, biology]

for single_textbook in textbooks:
    display_textbook(single_textbook)
