import random
'''
Ejemplo simple de uso de filtro (filter).
'''

# Genera una lista de números aleatorios entre -10 y 10
num_aleatorios = [random.randint(-10, 10) for _ in range(20)]

# Crea un filtro que seleccione los números pares positivos
pares_positivos = list(filter(lambda x: x > 0 and x % 2 == 0, num_aleatorios))

# Muestra el resultado en pantalla
print(num_aleatorios)
print(pares_positivos)
print("Pablo García Moreno")


