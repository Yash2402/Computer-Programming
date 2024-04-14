class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year

    def display(self):
        print(
            f"Name: {self.name}\nAuthor: {self.author}\nYear of Publication: {self.year}"
        )


class ScienceFiction(Book):
    def __init__(self, name, author, year, main_character):
        super().__init__(name, author, year)
        self.main_character = main_character

    def display(self):
        super().display()
        print(f"Main Character: {self.main_character}")


class Romance(Book):
    def __init__(self, name, author, year, main_plot):
        super().__init__(name, author, year)
        self.main_plot = main_plot

    def display(self):
        super().display()
        print(f"Main Plot: {self.main_plot}")


def Fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


fib_gen = Fibonacci()
limit = int(input("Enter no of terms of Fibonacci Series: "))
fib_series = []
for _ in range(limit):
    fib_series.append(next(fib_gen))
print(fib_series)
