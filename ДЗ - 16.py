# Класс Книга должен содержать информацию о названии, авторе и жанре книги

class Book:
    def __init__(self, title=None, author=None, year=None):
        self.title = title
        self.author = author
        self.year = year
    def display(self):
        text = ""
        if self.title != None: text = text + self.title[0:30] + " "
        if self.author != None: text = text + self.author[0:20] + " "
        if self.year != None: text = text + str(self.year)[0:5] + ""
        print(text)

book = Book('War and Peace.', 'Leo Tolstoy.', 1828)
book.display()
