def convertir_peso():
    peso = float(input("Introduce tu peso: "))
    unidad = input("¿(K)g o (L)bs? ").strip().upper()

    if unidad == 'K':
        peso_en_libras = peso * 2.20462
        print(f"Tu peso en libras es: {peso_en_libras:.2f} lbs")
    elif unidad == 'L':
        peso_en_kilos = peso / 2.20462
        print(f"Tu peso en kilos es: {peso_en_kilos:.2f} kg")
    else:
        print("Unidad no reconocida. Por favor, introduce 'K' para kilos o 'L' para libras.")

convertir_peso()