diccionario = {}
palabras = input("Introduce la lista de palabras y traduciones  en formato palabra")

for i in palabras.split(","):
    clave, valor = i.split(":")
    diccionario[clave] = valor
    
frase = input("Introduce una frase en español: ")

for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=" ")
    else:
        print(i, end=" ")