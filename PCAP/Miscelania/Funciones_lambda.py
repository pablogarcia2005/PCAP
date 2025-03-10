'''Funciones lambda (1)'''

def imprimir_funcion(args, fun):
    for x in args:
        print('f(' , x,')=', fun(x), sep='')
        
#La funcion lambda nos ahorra definir una funcion que solo se usa 1 vez
def funcion_grado2(x):
    return 2 * x**2 - 4 * x + 2

# f(x) = x^2

imprimir_funcion([x for x in range(-2, 3)], funcion_grado2)

#Codigo mas corto, claro y legible
imprimir_funcion([x for x in range(-2, 3)], lambda x:2 * x**2 -4 * x +2)