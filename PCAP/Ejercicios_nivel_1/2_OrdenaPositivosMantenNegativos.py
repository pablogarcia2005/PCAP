def ordena_positivos(lista):
    # Filtrar los números positivos y ordenarlos
    positivos_ordenados = sorted([num for num in lista if num > 0])
    
    # Crear un iterador para los positivos ordenados
    iterador_positivos = iter(positivos_ordenados)
    
    # Construir la nueva lista manteniendo los negativos en su posición original
    nueva_lista = [next(iterador_positivos) if num > 0 else num for num in lista]
    
    return nueva_lista

# Ejemplo de uso
lista_original = [3, -1, 2, -7, 5, -3]
lista_ordenada = ordena_positivos(lista_original)
print(lista_ordenada)  # Salida: [2, -1, 3, -7, 5, -3]