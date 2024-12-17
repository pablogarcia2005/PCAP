abecedario = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

resultados = []
for i in range(len(abecedario)):
    if i % 3 == 0:
       resultados.append(i)

print("Lista resultante:", resultados)
