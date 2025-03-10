
'''
    Ejercicio de clase.

    Crear una clase Empleado que modele trabajadores con un nombre y apellidos, un cargo y un salario.
    El salario debe ser (obligatoriamente) un atributo privado.

'''

class Empleado:
    def __init__(self, nombre, apellidos, cargo, salario):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.__salario = salario  # atributo privado

    def get_salario(self):
        return self.__salario

    def __str__(self):
        return f"{self.nombre} {self.apellidos}, {self.cargo}, Salario: {self.__salario}"

# Crear lista de empleados
listaEmpleados = [
    Empleado("Juanma", "García", "Director", 75000),
    Empleado("Teresa", "Martínez", "Presidenta", 80000),
    Empleado("Ana", "López", "Administrativo", 25000),
    Empleado("Mario", "Pérez", "Conserje", 20000)
]

# Seleccionar los empleados cuyo salario sea > 50k al año
empleados_vip = list(filter(lambda emp: emp.get_salario() > 50000, listaEmpleados))

# Mostrar los empleados seleccionados
for ev in empleados_vip:
    print(ev)
print("Pablo García Moreno")


