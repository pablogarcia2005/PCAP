import random

nombres = ["Arthas", "Jaina", "Thrall", "Illidan", "Sylvanas"]
clases = ["Guerrero", "Mago", "Arquero"]
niveles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
personajes = [{
    "nombre": random.choice(nombres),
    "clase": random.choice(clases),
    "nivel": random.choice(niveles)
    } for i in range(5)]

personajes_poderosos = filter(lambda p:p["nivel"] > 5, personajes)
#mostramos la lista de personajes generados
for p in personajes_poderosos:
    print(p)  