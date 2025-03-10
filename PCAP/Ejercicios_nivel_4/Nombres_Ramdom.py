import random

def generador_nombres():
    nombres = ["Arthas", "Jaina", "Thrall", "Illidan", "Sylvanas"]
    random.shuffle(nombres) #Mezcla los nombres aleatoriamente
    for nombre in nombres:
        yield nombre #Devuelbe un nombre cada vez que se llama
        
#Ejemplo de uso
generador = generador_nombres()

for _ in range(5):
    print(next(generador)) #Imprime 5 nombres aleatorios