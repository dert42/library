from book import Book
from library import Library


def main():
    library = Library()

    while True:
        print('\n--- Библиотека ---')
        print('1. Добавить книгу')
        print('2. Просмотреть все книги')
        print('3. Найти книгу')
        print('4. Удалить книгу')
        print('5. Изменить статус книги')
        print('6. Выйти')
        choice = input('Выберите действие (1-6): ')

        if choice == '1':
            try:
                title = str(input('Введите название книги: '))
                author = str(input('Введите автора книги: '))
                year = int(input('Введите год издания книги: '))
                book = Book(title, author, year)
                library.add_book(book)
            except ValueError:
                print('\n!________Некорректный ввод________!')

        elif choice == '2':
            library.list_books()

        elif choice == '3':
            print('\n--- Поиск книги  ---')
            print('1. Поиск по названию')
            print('2. Поиск по году')
            print('3. Поиск по автору')
            choice = input('Выберите действие (1-3): ')
            if choice == '1':
                title = str(input('Введите название книги: '))
                library.search_book_by_title(title)

            elif choice == '2':
                try:
                    year = int(input('Введите год издания книги: '))
                    library.search_book_by_year(year)
                except ValueError:
                    print('\n!________Некорректный ввод________!')

            elif choice == '3':
                author = str(input('Введите автора книги: '))
                library.search_book_by_author(author)
            else:
                print('\nНекорректный ввод. Пожалуйста, выберите действие от 1 до 3.')

        elif choice == '4':
            try:
                book_id = int(input('Введите id книги для удаления: '))
                library.remove_book(book_id)
            except ValueError:
                print('\n!________Некорректный ввод________!')

        elif choice == '5':
            try:
                book_id = int(input('Введите id книги для изменения статуса: '))
                library.change_status(book_id)
            except ValueError:
                print('\n!________Некорректный ввод________!')

        elif choice == '6':
            print('Выход из программы.')
            break

        else:
            print('\nНекорректный ввод. Пожалуйста, выберите действие от 1 до 6.')


if __name__ == '__main__':
    main()
