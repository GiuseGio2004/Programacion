# 4. Escriba un programa que permita ingresar un número, se debe validar que
# realmente se haya ingresado un número, y crear una lista para almacenar por
# separado los dígitos del número. Luego recorrer la lista y mostrar el índice que
# contiene el dígito mayor.

# Función para validar si la entrada es un número
def es_numero_valido(numero):
    return numero.isdigit()

numero = input("Ingresa un número: ")

while not es_numero_valido(numero):
    print("Entrada no válida. Por favor, ingresa un número válido.")
    numero = input("Ingresa un número: ")

digitos = [int(digito) for digito in numero]

# Buscar el dígito mayor y su índice
digito_maximo = max(digitos)
indice_digito_maximo = digitos.index(digito_maximo)

# Mostrar el índice que contiene el dígito mayor
print(f"El dígito mayor es {digito_maximo} y se encuentra en el índice {indice_digito_maximo}.")