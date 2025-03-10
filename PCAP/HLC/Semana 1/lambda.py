''' Funciones lambda (0) '''


# (1) Función lambda que calcula el área de un triángulo
area_triangulo = lambda base, altura: (base * altura) / 2

print(area_triangulo(10, 30))

# (2) Función lambda que calcula el cubo de un número entero
al_cubo = lambda x: x ** 3

print(al_cubo(5))

# (3) Función lambda que modifica la salida de una cadena (string)
destacar_valor = lambda comision: f" {comision}€ comisiones"

comision_empleado_1 = 15500

print(destacar_valor(comision_empleado_1))
print("Pablo García Moreno")

