creditos = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total = 0
for credito in creditos:
    print("El crédito de", credito, "es de", creditos[credito])
    total += creditos[credito]
print("Créditos totales:", total)