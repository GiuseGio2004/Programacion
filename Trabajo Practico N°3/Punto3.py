# 3. Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas
# las líneas del archivo, utilizando list comprehensions.

def leer_archivo_en_lista(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = [linea.strip() for linea in archivo]  # strip() elimina los saltos de línea
    return lineas

# Ejemplo de uso:
nombre_archivo = "datos.txt"
lineas_del_archivo = leer_archivo_en_lista(nombre_archivo)
print("Las líneas del archivo son:", lineas_del_archivo)