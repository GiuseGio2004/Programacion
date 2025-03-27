# Escriba un programa que permita el ingreso de números enteros positivos para 
# calcular su promedio, el ingreso finaliza cuando el usuario ingresa un número 
# negativo. Luego mostrar el promedio y la cantidad de valores que se ingresaron. 
# Ej: “El promedio es ….. con un total de …. ingresos.

suma = 0
cantidad = 0

while True:
    numero = int(input("Ingrese un número entero positivo (o un número negativo para finalizar): "))
    if numero < 0:
        break
    suma += numero
    cantidad += 1  

if cantidad > 0:
    promedio = suma / cantidad
    print(f"El promedio es {promedio:.2f} con un total de {cantidad} ingresos.")
else:
    print("No se ingresaron números positivos.")