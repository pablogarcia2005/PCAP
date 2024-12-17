import random

numeros = random.randint(1, 100)

def introducirNumero():
    numero = int(input("Introduce un numero del 1 al 100: "))
    return numero

numero = introducirNumero()

while numeros != numero:
    if numero < numeros:
        print("Número menor")
    elif numero > numeros:
        print("Número mayor")
    numero = introducirNumero()

print("Elegiste el", numero, "y el número correcto era el", numeros)



















