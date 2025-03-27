# 1. Implemente una función que, dada una lista de números, devuelva una nueva lista
# que contenga el cuadrado de cada número utilizando list comprehensions.

def cuadrados_lista(numeros):
    return [n ** 2 for n in numeros]

# Ejemplo de uso:
numeros = list(map(int, input("Ingresa una lista de números separados por espacios: ").split()))
cuadrados = cuadrados_lista(numeros)
print("La lista de cuadrados es:", cuadrados)