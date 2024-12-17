'''
    "raise" es equivalente a la palabra reservada "trows" de Java
    *Sin argumento, solo puede invocars dentro del bloque except (si no, da Error)
    * Lo que hace es volver a generar la excepcion para que otro se encargue de manejarla.
'''

import sys

def mal_asunto(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        #Regenera la excepcion
try:
    mal_asunto(0)
except ArithmeticError:
    print("Ya veo")
    sys.exit()

print("FIN.")
    