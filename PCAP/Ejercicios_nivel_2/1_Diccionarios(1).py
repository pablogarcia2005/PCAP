divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
entrada = input("Introduce una divisa: ").title()

if entrada in divisas:
    print(divisas[entrada])
else:
    print("Divisa no está en el diccionario")