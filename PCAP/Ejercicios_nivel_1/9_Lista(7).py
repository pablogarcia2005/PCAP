palabra = input("Introduce la palabra: ")

vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',]

for vocal in vocales:
    total = palabra.count(vocal)
    print("Tiene la", vocal, total, "veces")