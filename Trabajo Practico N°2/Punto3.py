# 3. Escriba un programa que permita cargar las notas de exámenes, primero debe
# permitir ingresar por teclado la cantidad de notas que desea cargar, y luego
# cargarlas en una lista, y posteriormente debe buscar la nota más alta, mostrarla, e
# indicar en qué índice del arreglo se encuentra.

cantidad_notas = int(input("Ingresa la cantidad de notas que deseas cargar: "))

notas = []

for i in range(cantidad_notas):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

# Buscar la nota más alta y su índice
nota_maxima = max(notas)
indice_nota_maxima = notas.index(nota_maxima)

print(f"La nota más alta es {nota_maxima} y se encuentra en el índice {indice_nota_maxima}.")