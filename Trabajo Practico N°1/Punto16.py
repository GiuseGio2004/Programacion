# 16. Escriba un programa que para un texto ingresado nos muestre cual es la palabra 
# más larga dentro de ese texto y cuántas letras tiene.

texto = input("Ingrese un texto: ")

palabras = texto.split()

palabra_mas_larga = ""
longitud_maxima = 0

for palabra in palabras:
    if len(palabra) > longitud_maxima:
        palabra_mas_larga = palabra
        longitud_maxima = len(palabra)

print(f"La palabra más larga es: '{palabra_mas_larga}' con {longitud_maxima} letras.")