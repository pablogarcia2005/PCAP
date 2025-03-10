class Empleados:
    plantilla = []
    num_empleados = 0
    def __init__(self, nombre, apellidos, cargo, salario=25000.50):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cargo = cargo
        if self.salario >= 0:
            raise ValueError
        self.__salario = salario
        Empleados.plantilla.append(self)
        Empleados.num_empleados += 1
           
    def getSalario(self):
        return self.salario
    
    def __str__(self):
        return f"{self.nombre} ({self.cargo}) gana: {round(self.getSalario())}"

empleado1 = Empleados("Pablo", "Garcia", "Informatico", 75000)
empleado2 = Empleados("Roberto", "Linares", "Informatico", 44000)

print


