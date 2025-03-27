# 6. Dado un diccionario de personas y sus edades, crea una lista que contenga solo los
# nombres de las personas cuya edad es mayor a una edad ingresada por el usuario,
# utilizando list comprehensions.

def filtrar_por_edad(diccionario, edad_minima, nombres_usuario=None):
    if nombres_usuario is None:
        return [nombre for nombre, edad in diccionario.items() if edad > edad_minima]
    else:
        return [nombre for nombre in nombres_usuario if nombre in diccionario and diccionario[nombre] > edad_minima]

diccionario = {}
num_personas = int(input("¿Cuántas personas deseas ingresar? "))
for _ in range(num_personas):
    nombre = input("Ingresa el nombre de la persona: ")
    edad = int(input(f"Ingresa la edad de {nombre}: "))
    diccionario[nombre] = edad

edad_minima = int(input("Ingresa la edad mínima para filtrar: "))
opcion = input("¿Deseas ingresar una lista de nombres para filtrar? (s/n): ").lower()

if opcion == 's':
    nombres_usuario = input("Ingresa una lista de nombres separados por espacios: ").split()
    nombres_filtrados = filtrar_por_edad(diccionario, edad_minima, nombres_usuario)
else:
    nombres_filtrados = filtrar_por_edad(diccionario, edad_minima)

print("Las personas cuya edad es mayor a", edad_minima, "son:", nombres_filtrados)