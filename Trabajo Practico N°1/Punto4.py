#4. Pedir 3 números enteros e implementar un algoritmo para determinar 
# cuál es el mayor de los 3 y mostrar un mensaje por pantalla.

# Solicitar tres números enteros al usuario
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

# Comparar los números para encontrar el mayor
if numero1 >= numero2 and numero1 >= numero3:
    mayor = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    mayor = numero2
else:
    mayor = numero3

# Mostrar el mayor de los tres números
print(f"El mayor de los tres números es: {mayor}")