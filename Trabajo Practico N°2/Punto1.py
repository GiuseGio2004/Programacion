# 1. Escribir un procedimiento “reverso” que permita ingresar como parámetro una
# cadena, y devuelva la cadena invertida (“hola” se convierte en “aloh”). Escribir luego
# un programa que determine si una cadena de caracteres es un palíndromo (un
# palíndromo es un texto que se lee igual en sentido directo y en inverso, ej.: “radar”).
# Sugerencia: para evitar diferencias entre mayúsculas y minúsculas en las cadenas,
# utilice la función del tipo string .upper() ó .lower() en las cadenas, ya que Radar es
# distinto a radaR

def reverso(cadena):
    return cadena[::-1]

def es_palindromo(cadena):
    # Convertir la cadena a minúsculas para evitar diferencias entre mayúsculas y minúsculas
    cadena = cadena.lower()
    # Obtener la cadena invertida usando el procedimiento reverso
    cadena_invertida = reverso(cadena)
    # Verificar si la cadena original es igual a la invertida
    return cadena == cadena_invertida

cadena = input("Ingresa una palabra: ")

if es_palindromo(cadena):
    print(f'"{cadena}" es un palíndromo.')
else:
    print(f'"{cadena}" no es un palíndromo.')