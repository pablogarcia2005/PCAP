tablero = []
sudoku_ok = False
for  i in range(9):
    fila = input("Linea " + str(i) + ": ")
    if not fila.isnumeric():
        print("Error, no se puede ingresar texto")
        break
    #Verificar que el Sudoku es valido (3 condiciones)
    elif sorted(fila) != list("123456789"):
        print(sorted(fila))
        print("La lista debe obtener todos los digitos del intervalo")
        break
    else:
        sudoku_ok = True
        tablero.append(fila)
if sudoku_ok:
    print("El sudoku SI es valido")
else:
    print("El sudoku NO es valido")