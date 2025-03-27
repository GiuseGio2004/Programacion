# 2. Implemente una función que, dada una lista de nombres, devuelva una nueva lista
# que contenga solo los nombres que tengan una longitud mayor o igual a una
# cantidad de caracteres pasada por parámetro, utilizando list comprehensions.

def filtrar_nombres_por_longitud(nombres, longitud_minima):
    return [nombre for nombre in nombres if len(nombre) >= longitud_minima]

# Ejemplo de uso:
nombres = input("Ingresa una lista de nombres separados por espacios: ").split()
longitud_minima = int(input("Ingresa la longitud mínima: "))
nombres_filtrados = filtrar_nombres_por_longitud(nombres, longitud_minima)
print("Los nombres con una longitud mayor o igual a", longitud_minima, "son:", nombres_filtrados)