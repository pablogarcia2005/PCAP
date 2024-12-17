def read_int(prompt, min, max):
    while True:
        try:
            valor = int(input(prompt))
            if min <= valor <= max:
                return valor
            else:
                print("Error: el valor no está dentro del rango")
        except ValueError:
            print("Error: el valor ingresado no es un número entero")

v = read_int("Ingresa un número entre -10 a 10: ", -10, 10)
print("El número es:", v)