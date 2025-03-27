# 13. Se desea realizar una aplicación que solicite al usuario un caracter y un número 
# natural N, y que la aplicación muestre en pantalla dicho carácter repetido N veces 
# consecutivas.
# Ej: Ingrese un caracter: +
# Ingrese la cantidad de repeticiones: 15
# +++++++++++++++

caracter = input("Ingrese un carácter: ")

N = int(input("Ingrese la cantidad de repeticiones: "))

if N > 0:
    resultado = caracter * N
    print(resultado)
else:
    print("La cantidad de repeticiones debe ser un número natural mayor que 0.")