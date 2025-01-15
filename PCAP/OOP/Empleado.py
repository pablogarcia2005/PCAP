class Empleados:
    def __init__(self, nombre, apellidos, cargo, salario=1000):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        self.salario = salario
    
    def getSalario(self):
        return self.salario
    
    # String de representaciones del objeto 
    def __str__(self):
        return f"{self.nombre} ({self.cargo}) gana: {round(self.getSalario())}"


listaEmpleados = [
    Empleados("Pablo", "Garcia", "Informatico", 75000),
    Empleados("Roberto", "Linares", "Informatico", 44000),
    Empleados("Raul", "Moreno", "Informatico", 39000),
    Empleados("Luis", "Morales", "Informatico", 94000)
]

# Seleccionar empleados cuyo salario sea > 50k al año
empleados_vip = [empleado for empleado in listaEmpleados if empleado.getSalario() > 50000]

# Imprimir empleados VIP
for empleado in empleados_vip:
    print(empleado)