''' Listas por "Compresion" v "Generadores"'''

'''
OJO: Si solo tiene la parte "if" (sin el "else") el "for" va primero
'''

mi_lista = [x for x in range(11) if x % 2 == 0 else None]
mi_gerenador = (x for x in range(11) if x % 2 == 0)

for v in mi_lista:
    print(v, end= " ")
print()

for v in mi_gerenador:
    print(v, end=" ")
print()