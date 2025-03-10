# Lista con los ataques base de varios personajes
ataques_base = [30, 55, 70, 45, 80, 25, 60]

# Usar map() con una función lambda para incrementar el daño en un 20% si el ataque es mayor de 50
ataques_incrementados = list(map(lambda x: x * 1.2 if x > 50 else x, ataques_base))

# Imprimir la lista de ataques incrementados
print("Ataques mejorados: ", ataques_incrementados)  