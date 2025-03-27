# 15. Escriba un programa que, dada una oración ingresada muestre por pantalla:
# a. El número total de caracteres en la oración
# b. La cantidad total de letras (consonantes y vocales, sin signos de puntuación)
# c. La cantidad de palabras separadas por uno o más espacios

import string

oracion = input("Ingrese una oración: ")

total_caracteres = len(oracion)

total_letras = sum(1 for caracter in oracion if caracter.isalpha())

total_palabras = len(oracion.split())

print(f"Número total de caracteres en la oración: {total_caracteres}")
print(f"Cantidad total de letras en la oración: {total_letras}")
print(f"Cantidad de palabras en la oración: {total_palabras}")