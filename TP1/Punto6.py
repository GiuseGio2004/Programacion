#6. Realizar un programa que solicite al usuario un número entero positivo, y luego en
# pantalla muestre la secuencia de números desde el 1 hasta el número ingresado.
# Ej: usuario ingresa 10, en pantalla se mostrará 1 2 3 4 5 6 7 8 9 10

Numero = int(input("ingrese un numero posito:"))

if Numero > 0:
    for i in range (1, Numero + 1 ):
     print(i, end=" ")
else:
    print("El número ingresado no es positivo.")