frutas = {"Platano": 1.35, "Manzana":0.8, "Pera":0.85, "Naranja":0.7}

nombre = input("Que fruta desea: ").title()
peso = float(input("Indique el peso: "))

if nombre in frutas:
    print(peso, " kilos de ", nombre ," son ", peso * frutas[nombre])
else:
    print("Lo siento, no tenemos esa fruta.")