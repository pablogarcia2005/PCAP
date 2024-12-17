'''
El orden de las excepciones importa:
*Coloca los tipos de excepciones mas generales al final.
*Si no, el codigo para excepciones mas concretas sera inalcanzable.
*prueba a cambiar el orden de las excepciones para comprobarlo
'''

try:
    y = 1 / 0

#Excepciones más concreta
except (ZeroDivisionError,  ArithmeticError):
    print("Hubo un problema al hacer la operacion")
except: #Excepcion (sin nombre)
    #Todo lo demas cae aqui
    print("Algo ha cascado aqui...")
    
print("FIN.")