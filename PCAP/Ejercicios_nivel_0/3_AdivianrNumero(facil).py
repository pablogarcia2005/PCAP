'''VERSION A'''
numero = 5
adivinar = int(input("Adivina el número: "))
if adivinar == numero:
    print("Acertaste")
else:
    print("Fallaste")

'''VERSION B'''
numero = 5
intentos = 10

for i in range(intentos):
    adivinar = int(input("Adivina el número: "))
    if adivinar == numero:
        print("Acertaste")
        break
    else:
        print("Fallaste")
        print("Te quedan", intentos - i - 1, " intentos")


'''VERSION C'''
numero = 5
while True:
    adivinar = int(input("Adivina el número: "))
    if adivinar == numero:
        print("Acertaste")
        break
    else:
        print("Fallaste")