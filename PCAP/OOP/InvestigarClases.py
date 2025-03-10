'''
Ejemplo de las propiedades de introspeccion y refelxion del lenguaje python
'''

class MyClass:
    pass

# Pueden añadirse atributos ...
# ¡¡ en tiempo de ejecucion !!

obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5

'''
La funcion toma un objeto cualquiera, busca en si interior atributos enteros 
con nombres que empiecen por "i", y los incremente en uno.
'''

def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)