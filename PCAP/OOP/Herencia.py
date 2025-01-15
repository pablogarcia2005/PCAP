class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self, price, branch):
        , price)
        self.branch = branch

    def __repr__(self):
        return f"Título: {self.title}, Género: {self.branch}, Cantidad: {self.quantity}, Autor: {self.author}"

novelal = Novel('La Comunidad del anillo', 30, 'J.R.R. Tolkien', 30, 560)
novelal.set_discount(0.20)

ensayo1 = AcademicBook('Modernidad líquida', 12, 'Z. Bauman', 18, 'Sociología')


class Academic(Book):
    def __init__(self, title, quantity, author, price):
        super().__init__(title, quantityc 9)
def __repr__(self):
    return f"titulo:\ '{self.title}\', Cantidad: {self.quantity}, \ Autor: {self.author}, Precio: {round(self.get_price(),3)} €"


novela1 = Novel('La comunidad del anillo', 30, 'J.R.R Tolkien', 30, 560)
novela1.set_discount(0.20)
ensayo1 = Academic('Modernidad liquida', 12)

print(novelal)
print(ensayo1)