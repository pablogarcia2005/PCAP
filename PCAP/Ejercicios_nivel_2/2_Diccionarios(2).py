nombre = str(input("Introduce tu nombre: "))
edad = int(input("Introduce tu edad: "))
direccion = str(input("Introduce tu direccion: "))
telefono = str(input("Introduce tu telefono: "))

datos = {"nombre": nombre, "edad": edad, "direccion": direccion, "telefono": telefono}
print(datos["nombre"], "tiene", datos["edad"], "años, vive en", datos["direccion"], "y su teléfono es", datos["telefono"])