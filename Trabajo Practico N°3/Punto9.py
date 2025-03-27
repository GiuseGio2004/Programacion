# 9. Dada una lista de números, crea dos listas separadas: una que contenga los
# números pares y otra que contenga los números impares utilizando list
# comprehensions

def separar_pares_impares(numeros):
    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]
    return pares, impares

numeros = list(map(int, input("Ingresa una lista de números separados por espacios: ").split()))
pares, impares = separar_pares_impares(numeros)
print("Números pares:", pares)
print("Números impares:", impares)