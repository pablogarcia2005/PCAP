import random

def generador_personajes():
    nombres = ["Arthas", "Jaina", "Thrall", "Illidan", "Sylvanas"]
    clases = ["Guerrero", "Mago", "Arquero"]
    niveles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    while True:
        nombre = random.choice(nombres)
        clase = random.choice(clases)
        nivel = random.choice(niveles)
        yield {"nombre": nombre, "clase": clase, "nivel": nivel}

# Ejemplo de uso
generador = generador_personajes()

for _ in range(5):
    print(next(generador)) # Imprime 5 personajes aleatorios