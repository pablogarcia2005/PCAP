class Item:
    def __init__(self, nombre, tipo, rareza):
        self.nombre = nombre
        self.tipo = tipo
        self.rareza = rareza

class Persona:
    def __init__(self, inventario):
        self.inventario = inventario

    def agregar_item(self, item):
        if len(self.inventario) < 5:
            self.inventario.append(item)
        else:
            raise ValueError ("InventarioLLenoError")
    
    def eliminar_item(self, item):
        if item in self.inventario:
            self.inventario.remove(item)
        else:
            raise ValueError ("Item no esta en el inventario")
        
    def mostrar_item(self):
        for item in self.inventario:
            print(f"Nombre: {item.nombre}, Tipo: {item.tipo}, Rareza: {item.rareza}")
            

item1 = Item("Espada", "Arma", "Raro")
item2 = Item("Escudo", "Arma", "Comun")

persona = Persona([])

persona.agregar_item(item1)
persona.agregar_item(item2)

persona.mostrar_item()

persona.eliminar_item(item2)
persona.mostrar_item()
    
