# 3. Escriba un programa que permita leer de un archivo distancias.txt (cada renglón
# tiene una distancia válida) las distancias recorridas por el vehículo de una empresa,
# luego calcular cual es la distancia promedio, y mostrar por pantalla el promedio y
# todas las distancias mayores al promedio.
# Ej del contenido del archivo:
# 150
# 120
# 50
# 34
# 250
# Salida: “La distancia promedio de los viajes es … y los viajes con distancia mayor
# son: … , … , …. , …. “

# Función para leer las distancias desde un archivo
def leer_distancias(archivo):
    with open(archivo, 'r') as file:
        distancias = [float(linea.strip()) for linea in file]
    return distancias

# Función para calcular la distancia promedio
def calcular_promedio(distancias):
    return sum(distancias) / len(distancias)

# Función principal
def main():
    # Leer las distancias desde el archivo
    archivo = "Distancias.txt"
    distancias = leer_distancias(archivo)
    
    # Calcular la distancia promedio
    promedio = calcular_promedio(distancias)
    
    # Filtrar las distancias mayores al promedio
    distancias_mayores = [distancia for distancia in distancias if distancia > promedio]
    
    # Mostrar el resultado
    print(f"La distancia promedio de los viajes es {promedio:.2f}")
    print(f"Los viajes con distancia mayor son: {', '.join(map(str, distancias_mayores))}")

# Llamar a la función principal
if __name__ == "__main__":
    main()