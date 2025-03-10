'''Lista por compresion (1)'''

mi_lista = []

#Lista de pares entre 0 y 10
for x in range(11):
    mi_lista.append(0 if x % 2 == 0 else 1)

print(mi_lista)

# Idem, usando una lista por compresion
mi_lista = [0 if x % 2 == 0 else 1 for x in range(11)]

print(mi_lista)