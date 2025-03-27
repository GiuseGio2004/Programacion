# 14. Escriba un programa que dado un texto ingresado por el usuario cuente la cantidad 
# total de vocales que aparecen y lo muestre por pantalla.

texto = input("Ingrese un texto: ")

cantidad_vocales = 0

vocales = "aeiouAEIOU"

for caracter in texto:
    if caracter in vocales:
        cantidad_vocales += 1

print(f"La cantidad total de vocales en el texto es: {cantidad_vocales}")
