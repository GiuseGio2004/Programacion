#8. Desarrollar un programa que permita al usuario indicar cuantos valores quiere
# ingresar, luego que permita la carga de los valores por teclado y nos muestre
# posteriormente la suma de los valores ingresados y su promedio.

cantidad = int(input("¿Cuántos valores desea ingresar? "))

suma = 0

for i in range(cantidad):
    valor = float(input(f"Ingrese el valor {i+1}: "))
    suma += valor

promedio = suma / cantidad

print(f"La suma de los valores ingresados es: {suma:.2f}")
print(f"El promedio de los valores ingresados es: {promedio:.2f}")