#7. Realizar un programa que solicite al usuario un número entero positivo, 
# y luego en pantalla muestre solamente los números pares desde el 1 hasta el número ingresado.
# Ej: usuario ingresa 10, en pantalla se mostrará 2 4 6 8 10

Numero = int(input("ingrese un numero posito:"))

if Numero > 0:
    for i in range (2, Numero + 1, 2):
     print(i, end=" ")
else:
    print("El número ingresado no es positivo.")