class Book:
    book_id = -1
    id: int
    title: str
    author: str
    year: int
    status: str

    def __init__(self, title, author, year):
        self.id = Book.book_id + 1
        Book.book_id += 1
        self.title = title
        self.author = author
        self.year = year
        self.status = 'в наличии'

    def __str__(self):
        return f'{self.id}: "{self.title}" by {self.author} ({self.year}г.) - {self.status}'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
                          }