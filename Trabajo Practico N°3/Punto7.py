# 7. Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de
# vocales en ella. El programa deberá pedirle palabras al usuario hasta que éste
# introduzca la palabra “salir”.

def contar_vocales(palabra):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for letra in palabra if letra in vocales)

while True:
    palabra = input("Ingresa una palabra (o escribe 'salir' para terminar): ")
    if palabra.lower() == "salir":
        print("Programa terminado.")
        break
    cantidad_vocales = contar_vocales(palabra)
    print(f"La palabra '{palabra}' tiene {cantidad_vocales} vocales.")