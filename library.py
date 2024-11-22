import json

from book import Book


class Library:
    books: list

    def __init__(self):
        self.books = []
        with open('data/books.json', 'r') as file:
            books_dct = json.load(file)
        for book in books_dct:
            self.books.append(Book(book['title'], book['author'], int(book['year'])))

    def add_book(self, book):
        self.books.append(book)
        print(f'Книга "{book.title}" добавлена в библиотеку.')
        self.save()

    def search_book_by_title(self, title):
        found_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                found_books.append(book)
        if found_books:
            print('\n_________Найденные книги:__________')
            for book in found_books:
                print(str(book))
        else:
            print('\n_________Книги не найдены.__________')

    def search_book_by_author(self, author):
        found_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                found_books.append(book)
        if found_books:
            print('\n_________Найденные книги:__________')
            for book in found_books:
                print(str(book))
        else:
            print('\n_________Книги не найдены.__________')

    def search_book_by_year(self, year):
        found_books = []
        for book in self.books:
            if book.year == year:
                found_books.append(book)
        if found_books:
            print('\n_________Найденные книги:__________')
            for book in found_books:
                print(str(book))
        else:
            print('\n_________Книги не найдены.__________')

    def list_books(self):
        if not self.books:
            print('\n_________Библиотека пуста.__________')
        else:
            print('\n_________Список книг в библиотеке:_________')
            for book in self.books:
                print(str(book))

    def remove_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                self.save()
                print(f'Книга с id:"{book_id}" удалена из библиотеки.')
                return
        print(f'Книга с id:"{book_id}" не найдена.')

    def change_status(self, book_id):
        for book in self.books:
            if book.id == book_id:
                if book.status == 'в наличии':
                    book.status = 'выдана'
                    self.save()
                    print(f'Статус книги с id:{book_id} изменён на: "выдана"')
                    return
                if book.status == 'выдана':
                    book.status = 'в наличии'
                    self.save()
                    print(f'Статус книги с id:{book_id} изменён на: "в наличии"')
                    return
        print(f'Книги с id:{book_id} - не найдена')

    def save(self):
        json_books = []
        for book_ in self.books:
            json_books.append(book_.to_json())
        with open('data/books.json', 'w') as file:
            json.dump(json_books, file)
