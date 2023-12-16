class Building:
    def __init__(self, address):
        self.address = address
class Library(Building):
    def __init__(self, address, name, books):
        Building.__init__(self, address)
        self.name = name
        self.books = books

    def SellBook(self, id):
        self.books[id].count = self.books[id].count - 1
        if self.books[id].count == 0:
            del self.books[id]

    def GetInformationAboutLibrary(self):
        print("Адрес: ", self.address)
        print("Название библиотеки: ", self.name)
        print("Ассортимент книг: ")
        for x in self.books:
            print("Название книги: ", x.name, "Автор: ",  x.author, "Жанр: ", x.category, "Стоимость: ", x.cost, "Количество книг в библиотеке: ", x.count)

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

    print("")

    b = [B1, B2]
    L1 = Library("Новый бульвар", "Книжка", b)
    L1.GetInformationAboutLibrary()