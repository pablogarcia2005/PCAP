"""
 En Python, un método especial es una función definida que
 comienza y termina con dos guiones bajos (__thisway__) y
 se invoca automáticamente cuando se cumplen ciertas condiciones.
"""

class Book:

    # Constructor 
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        # Encapsulacion: atributos privados
        self.__price = price
        self.__discount = None
    
    #Setter metodo
    def set_discount(self, discount):
        self.__discount = discount
    
    #Metodo Getter
    def get_price(self):
        if self.__discount: # si esta definido
            return self.__price * (1-self.__discount)
        return self.__price

    # Return a printable representation of the object
    def __repr__(self):
        return f"titulo:\ '{self.title}\', Cantidad: {self.quantity}, \ Autor: {self.author}, Precio: {round(self.get_price(),3)} €"


book1 = Book('El Señor de los anillos', 30, 'J.R.R. Tolkien', 22)
book2 = Book('El cuento de la criada', 28, 'Margaret Atwood', 30)
book3 = Book('Reina roja', 25, 'Juan Gómez Jurado', 28)

print(book1)
print(book2)
print(book3)

print(book1.title)
print(book1.quantity)
print(book1.author)


