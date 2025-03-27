#. Escriba un programa que permita al usuario ingresar las medidas de 2 lados de un
# rectángulo, y que luego mediante la impresión repetida de un caracter (ej: *) lo dibuje
# en la pantalla. Para este ejercicio tomaremos un máximo de 40 para el lado más
# largo, con el fin de evitar problemas de visualización en la consola. 
# Verificar en los datos de entrada que se cumpla este requisito.

lado1 = int(input("Ingrese la longitud del primer lado del rectángulo (máximo 40): "))
lado2 = int(input("Ingrese la longitud del segundo lado del rectángulo (máximo 40): "))

if 1 <= lado1 <= 40 and 1 <= lado2 <= 40:
    # Determinar cuál lado es más largo
    for i in range(lado1):  # Repetir por la cantidad de filas (lado1)
        print('*' * lado2)  # Imprimir '*' lado2 veces en cada fila
else:
    print("Ambos lados deben ser positivos y no deben exceder de 40.")
