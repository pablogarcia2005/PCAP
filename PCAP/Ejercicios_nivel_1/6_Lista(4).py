asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

notaMates = int(input("Introduce tu nota de mates: "))
notaFisica = int(input("Introduce tu nota de fisica: "))
notaQuimica = int(input("Introduce tu nota de quimica: "))
notaHistoria = int(input("Introduce tu nota de historia: "))
notaLengua = int(input("Introduce tu nota de lengua: "))

if notaMates >= 5:
    asignaturas.remove("Matemáticas")
if notaFisica >= 5:
    asignaturas.remove("Física")
if notaQuimica >= 5:
    asignaturas.remove("Química")
if notaHistoria >= 5:
    asignaturas.remove("Historia")
if notaLengua >= 5:
    asignaturas.remove("Lengua")

print("Asignaturas suspensas:", asignaturas)