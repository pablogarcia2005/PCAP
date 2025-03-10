'''Funcion map() y lambda'''

# Enteros de 0 a 4
lista_numerica = [ x for x in range(5)]

'''
Con map() y lambda creamos una nueva lista de potencias de 2
elevado a los exponentes sacados de lista_numerica = [0, 1, 2, 3, 4].
'''
lista_cuadrados = list(map(lambda x:2 ** x, lista_numerica))

print(lista_cuadrados)

'''
Con lambda elevamos al cuadrado cada elemento de lista_ cuadrados = [0, 2, 4, 8, 16]
a partir de los valores calculados, con map() obtemenos un gerenador
para ser usado en el bucle for
'''
for x in map(lambda x: x * x, lista_cuadrados):
    print(x, end=' ')
print()
