'''Lista por compresion (1)'''

lista_1 = []

#Lista de potencias de 10 (10º a 10 elevado a 5)
for n in range(6):
    lista_1.append(10 ** n)
    
# Idem, usando un alista por compresion
lista_2 = [10 ** n for n in range(6)]

print(lista_1)
print(lista_2)