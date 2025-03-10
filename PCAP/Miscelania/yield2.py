'''Funcion generadora'''
def potencias_de_2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

for p in potencias_de_2(5):
    print(p)
    
'''Alternativa (1) usando una lista de compresión '''
x = [p for p in potencias_de_2(5)]
print(x)

'''Alternativa (2) usando la funcion list() '''
x = list(potencias_de_2(5))
print(x)