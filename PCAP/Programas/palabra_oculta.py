#Encuentra la Palabra oculta

'''
Tenemos 2 cadenas: una palabra (perro) y un grupo de caracteres desordenados 
¿El grupo de caracteres contiene la palabra?
Ej:
vzvcghdepjhjhevrrjho   => SI
'''

palabra = input("introduce palabra a buscar: ").upper()
grupo = input("Introduce grupo de caracteres: ")

contiene = True
inicio = 0

for c in palabra:
	posicion = grupo.find(c, inicio)    #Devuelve -1 si no esta
	if posicion < 0:
		contiene = False                #Si un caracter no esta, terminamos,
		break
	inicio = posicion + 1
if contiene:
	print("Si esta")
else:
	print("No esta ")