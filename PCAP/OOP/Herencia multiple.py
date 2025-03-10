class Saiyan:
    planeta = "Sadala"
    def __init__(self, nombre):
        self.nombre = nombre

class Humano:
    planeta = "Tierra"
    def __init__(self, nombre):
        self.nombre = nombre

class Trunks(Humano, Saiyan):
    def __init__(self, nombre, a, b):
        self.nombre = nombre
        self.progen_A = a.nombre
        self.progen_B = b.nombre

    # Imprime las superclases de la clase
    def verAncestros(self):
        for x in Trunks.__bases__:
            print(x.__name__, end=' ')
        print()

goku = Saiyan("Son Goku")
vegeta = Saiyan("Vegeta")
bulma = Humano("Bulma")

mestizo = Trunks("Trunks", vegeta, bulma)

# Imprime el nombre de la clase del objeto
print(type(mestizo).__name__)

# Imprime los atributos y métodos del objeto
print(mestizo.__dict__)

# Imprime los ancestros de la clase
print(f"El padre de {mestizo.nombre} es {mestizo.__dict__['padre']}")
print(f"La madre de {mestizo.nombre} es {mestizo.__dict__['madre']}")




# Definir la propiedad 'origen' en la clase Trunks
Trunks.origen = "Tierra"
print(f"Trunks es de {mestizo.origen}")
print(f"Goku es de {goku.planeta}")

if type(mestizo).__name__ == "Trunks":
    if issubclass(Trunks, Saiyan):
        print(f"{mestizo.nombre} puede convertirse en supersayan.")
        if issubclass(Trunks, Humano):
            print(f"{mestizo.nombre} tiene madre Humana")
    else:
        print(f"{mestizo.nombre} no puede convertirse en supersayan.")