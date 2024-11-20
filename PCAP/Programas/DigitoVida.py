#El difito de la vida

'''
Se suman todos los digitos de fecha introducida
Si el resultado contiene mas de un digito, se repite la suma hasta obtener exactamente un
Ej 1 Enero 2017 = 2017 01 01 ;
'''

fecha = ''

while True:
    fecha = input("Introduce tu fecha de nacimiento: ")
    if fecha.isnumeric():
        break
    print("debes introducir una fecha en formato AAAAMMDD")
    
digito = 0
suma = 0

for c in fecha:
    suma += int(digito)
    if suma < 10:
        digito = suma
        break
print("Digito de vida es: " , digito)