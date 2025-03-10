def pedir_datos():
    datos = {}
    while True:
        clave = input("Introduce el tipo de dato, nombre, edad, sexo, teléfono, correo electrónico): ")
        valor = input(f"Introduce el {clave}: ")
        datos[clave] = valor
        print(datos)
        
        continuar = input("¿Quieres añadir más información (Si/No)? ")
        if continuar != 'si':
            break

pedir_datos()