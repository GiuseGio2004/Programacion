# Un profesor almacenó los datos de los alumnos de su materia en un archivo 
# alumnos.txt. En cada línea guardó el número de legajo del alumno y sus tres notas 
# finales (oral, escrito y trabajos prácticos). El archivo está ordenado por número de 
# legajo. 
# En otro archivo, ordenado alfabéticamente por apellido, guarda por línea, número de 
# legajo, apellido y nombre de cada uno.
# En ambos archivos los datos están separados por punto y coma ( ; ) .
# Desea escribir un programa para generar un archivo Promoción.txt con los apellidos 
# y nombres de los alumnos que promocionan la materia, esto es, alumnos que el 
# promedio de las tres notas supere los 7 puntos. 
# El archivo debe quedar ordenado alfabéticamente

ruta_alumnos = open("Alumnos.txt", "r")
ruta_nombres = open("Nombres.txt", "r")
ruta_promocion = open("Promocion.txt", "w")

listaPromedio = []

for linea in ruta_alumnos:
    lista = linea.strip().split(";")
    if((float(lista[1]) + float(lista[2]) + float(lista[3]))/ 3 >=7):
        listaPromedio.append(lista[0])
        
for linea in ruta_nombres:
    lista = linea.strip().split(";")
    if lista[0] in listaPromedio:
        ruta_promocion.write(f"{lista[1]}, {lista[2]} \n")
        
ruta_alumnos.close()
ruta_nombres.close()
ruta_promocion.close()