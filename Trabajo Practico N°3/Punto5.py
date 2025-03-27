# 5. Dado un rango de números, crea una lista que contenga todos los números primos 
# dentro de ese rango utilizando list comprehensions.

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos_en_rango(inicio, fin):
    return [n for n in range(inicio, fin + 1) if es_primo(n)]

# Ejemplo de uso:
inicio = int(input("Ingresa el inicio del rango: "))
fin = int(input("Ingresa el fin del rango: "))
numeros_primos = primos_en_rango(inicio, fin)
print("Los números primos en el rango son:", numeros_primos)