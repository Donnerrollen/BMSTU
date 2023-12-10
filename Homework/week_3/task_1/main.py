class Library:
    def __init__(self, address, name, books):
        self.address = address
        self.name = name
        self.books = books

    def SellBook(self, id):
        self.books[id].count = self.books[id].count - 1
        if self.books[id].count == 0:
            del self.books[id]

    def GetInformationAboutLibrary(self):
        print(self.address, self.name)
        for x in self.books:
            print(x.name, x.author, x.category, x.cost)

class Book:
    def __init__(self, id, name, author, category, cost, count):
        self.id = id
        self.name = name
        self.author = author
        self.category = category
        self.cost = cost
        self.count = count

    def GetInformationAboutBook(self):
        print(self.name, self.author, self.category, self.cost)

if __name__ == "__main__":
    B1 = Book(1, "Красная шапочка", "Кто-то там", "Сказки", 1000, 50)
    B1.GetInformationAboutBook()
    B2 = Book(2, "Три поросенка", "Кто-то там", "Сказки", 800, 25)
    B2.GetInformationAboutBook()

    b = [B1, B2]
    L1 = Library("1", "Книжка", b)
    L1.GetInformationAboutLibrary()